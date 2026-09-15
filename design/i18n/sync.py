#!/usr/bin/env python3
"""Mirror design/i18n/{vi,ja,zh}.json into landing.html, checking parity first.

There is deliberately no en.json. English is the authored markup, and the
runtime reads it out of the DOM at boot, so the contract a translation has to
satisfy is the set of data-i18n* keys in landing.html plus the handful of keys
owned by the scripts. Both are extracted here rather than duplicated.

    python3 design/i18n/sync.py            # check and mirror
    python3 design/i18n/sync.py --check    # check only, write nothing

Exit 1 on any parity failure.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAGE = ROOT / "landing.html"
LOCALES = ("vi", "ja", "zh")

# Values that are an array in every dictionary, and how many entries they must
# have. Headlines are one entry per authored .ln in the markup; the marquee is
# one entry per item. A short array would silently drop a headline line.
ARRAY_LENGTHS = {
    "hero.h1": 3, "what.h2": 3, "work.h2": 3,
    "method.h2": 3, "stack.h2": 3, "close.h2": 3,
    "ticker.items": 8,
}

TAG = re.compile(r"<[^>]+>")
BLOCK = re.compile(
    r'(<script type="application/json" id="i18n-(%s)">)(.*?)(</script>)' % "|".join(LOCALES),
    re.S,
)
# A key is lowercase-initial and always dotted, which is what keeps this from
# matching getContext('2d'), closest('.slab') or new Event('themechange').
KEY = r"[a-z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)+"


def markup_keys(html: str) -> set:
    """Every key the page asks for: element bindings plus script-owned strings."""
    keys = set(re.findall(r'data-i18n(?:-html|-lines)?="(%s)"' % KEY, html))
    # data-i18n-attr carries semicolon-separated "attr:key" pairs. Anchoring on
    # the first pair would let a second one go unchecked, which is exactly the
    # kind of key that then goes missing from one dictionary unnoticed.
    for group in re.findall(r'data-i18n-attr="([^"]+)"', html):
        keys |= {p.split(":", 1)[1].strip() for p in group.split(";")
                 if ":" in p and re.fullmatch(KEY, p.split(":", 1)[1].strip())}
    # resolved at runtime rather than bound to an element
    keys |= set(re.findall(r"""\btr?\(\s*['"](%s)['"]""" % KEY, html))
    keys |= set(re.findall(r"""'(work\.c\d\.viz)'""", html))
    return keys


def load(code: str) -> dict:
    return json.loads((ROOT / "design/i18n" / f"{code}.json").read_text(encoding="utf-8"))


def check(html: str, dicts: dict) -> list:
    problems = []
    wanted = markup_keys(html)
    reference = sorted(dicts[LOCALES[0]])

    for code in LOCALES:
        d = dicts[code]
        missing = sorted(wanted - set(d))
        if missing:
            problems.append(f"{code}: markup asks for keys the dictionary lacks: {missing}")
        if sorted(d) != reference:
            only = sorted(set(d) ^ set(dicts[LOCALES[0]]))
            problems.append(f"{code}: key set differs from {LOCALES[0]}: {only}")
        for key, n in ARRAY_LENGTHS.items():
            v = d.get(key)
            if not isinstance(v, list) or len(v) != n:
                problems.append(f"{code}: {key} must be an array of {n}, got {v!r:.60}")

    # The inline markup inside a value is structural: a translator dropping a
    # </b> or an hl span silently changes what the page emphasises.
    base = dicts[LOCALES[0]]
    for code in LOCALES[1:]:
        for key, v in base.items():
            w = dicts[code].get(key)
            if isinstance(v, str) and isinstance(w, str) and TAG.findall(v) != TAG.findall(w):
                problems.append(f"{code}: {key} tag sequence differs from {LOCALES[0]}")
            if isinstance(v, list) and isinstance(w, list):
                for i, (a, b) in enumerate(zip(v, w)):
                    if TAG.findall(a) != TAG.findall(b):
                        problems.append(f"{code}: {key}[{i}] tag sequence differs")

    orphans = sorted(set(base) - wanted)
    if orphans:
        problems.append(f"keys in every dictionary that nothing consumes: {orphans}")
    return problems


def mirror(html: str, dicts: dict) -> str:
    def sub(m):
        body = json.dumps(dicts[m.group(2)], ensure_ascii=False, separators=(",", ":"))
        return m.group(1) + body.replace("</", "<\\/") + m.group(4)

    out, n = BLOCK.subn(sub, html)
    if n != len(LOCALES):
        raise SystemExit(f"expected {len(LOCALES)} inline dictionary blocks, found {n}")
    return out


def main() -> int:
    html = PAGE.read_text(encoding="utf-8")
    dicts = {c: load(c) for c in LOCALES}

    problems = check(html, dicts)
    for p in problems:
        print("FAIL", p, file=sys.stderr)
    if problems:
        return 1

    print(f"parity ok: {len(markup_keys(html))} keys requested, "
          f"{len(dicts[LOCALES[0]])} per dictionary, {len(LOCALES)} locales")

    if "--check" in sys.argv:
        return 0

    out = mirror(html, dicts)
    if out == html:
        print("landing.html already matches the dictionaries")
    else:
        PAGE.write_text(out, encoding="utf-8")
        print("landing.html inline dictionaries updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
