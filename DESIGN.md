---
name: Le Nguyen Thanh Ha — AI Product Engineer
description: A personal hiring page built as a piece of field detection equipment.
colors:
  ground: "#0b0d10"
  surface: "#12161b"
  surface-raised: "#171c23"
  hairline: "#242c36"
  hairline-interactive: "#566981"
  bone: "#f0e9df"
  bone-secondary: "#98a1ac"
  muted: "#7c8794"
  signal-red: "#ff2f43"
  on-signal: "#0b0d10"
  ground-light: "#f0ece4"
  surface-light: "#fffdf9"
  surface-raised-light: "#e7e1d5"
  hairline-light: "#aca291"
  hairline-interactive-light: "#877f72"
  bone-light: "#16171b"
  bone-secondary-light: "#43474f"
  muted-light: "#5d6470"
  signal-red-light: "#c30a1c"
  on-signal-light: "#fffdf9"
typography:
  display:
    fontFamily: "Bricolage Grotesque, Bricolage fallback, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(32px, 10.2vw, 104px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "-0.035em"
    fontVariation: "'wdth' 86"
  headline:
    fontFamily: "Bricolage Grotesque, Arial, sans-serif"
    fontSize: "clamp(23px, 5.2vw, 74px)"
    fontWeight: 800
    lineHeight: 0.94
    letterSpacing: "-0.035em"
    fontVariation: "'wdth' 88"
  title:
    fontFamily: "Bricolage Grotesque, Arial, sans-serif"
    fontSize: "1.1875rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 92"
  body:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.09375rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  label:
    fontFamily: "JetBrains Mono, ui-monospace, Menlo, monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "0.13em"
  label-small:
    fontFamily: "JetBrains Mono, ui-monospace, Menlo, monospace"
    fontSize: "0.6875rem"
    fontWeight: 400
    letterSpacing: "0.12em"
  label-wide:
    fontFamily: "JetBrains Mono, ui-monospace, Menlo, monospace"
    fontSize: "0.78125rem"
    fontWeight: 400
    letterSpacing: "0.13em"
  body-compact:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  body-note:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "0.90625rem"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  caption: "5px"
  print-card: "8px"
  step: "9px"
  schematic: "10px"
  frame: "12px"
  portrait: "14px"
  panel: "16px"
  card: "18px"
  pill: "999px"
spacing:
  section: "124px"
  section-compact: "72px"
  card: "32px"
  stack: "26px"
  inline: "12px"
components:
  button-primary:
    backgroundColor: "{colors.signal-red}"
    textColor: "{colors.on-signal}"
    rounded: "{rounded.hairline-chip}"
    padding: "0 28px"
    height: "52px"
    typography: "{typography.label}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.bone}"
    rounded: "{rounded.hairline-chip}"
    padding: "0 28px"
    height: "52px"
  card-work:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.bone-secondary}"
    rounded: "{rounded.card}"
    padding: "32px 30px 28px"
  chip-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.hairline-chip}"
    padding: "5px 11px"
    typography: "{typography.label}"
  step-indicator:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "9px"
    size: "34px"
  step-indicator-current:
    backgroundColor: "{colors.signal-red}"
    textColor: "{colors.on-signal}"
---

# Design System: Le Nguyen Thanh Ha — AI Product Engineer

## Overview

**Creative North Star: "The Field Instrument"**

The page is built as a piece of detection equipment rather than as a portfolio. Its subject builds computer-vision systems that watch a room and report what they saw, and the interface performs that same job on itself: a reticle tracks the cursor, a canvas acquires ambient targets behind the headline, a fixed instrument in the corner locks onto whichever section you have reached and names it, and brackets close around the heading you jump to. The bracket is the system's single motif and it appears at every scale — favicon, cursor, hero canvas, the overlay on the shelf photograph, the card schematics, the portrait's corner marks, the arrival mark.

The ground is a cold near-black lit by one warm aubergine bloom, with warm cream text that is never pure white and a single signal red used sparingly enough that it always means *look here*. A 22px dot lattice and a fine grain sit under everything, so the background reads as a sensor surface rather than as a void. Nothing is decorative twice: the photography is real public-domain surveillance and kitchen-line material, shipped pre-desaturated and tinted by blend mode so one file serves both themes.

The confirmed anti-reference is the AI-SaaS marketing page: gradient text, glass panels, pastel abstractions, icon-heading-paragraph card grids, and stock illustration of "AI". Every claim on the page is attached to a number and a route to verify it, and the visual system exists to make that posture legible before a word is read.

**Key Characteristics:**
- One motif — the acquisition bracket — carried through eight surfaces
- Cold ground, warm ink, one signal colour
- Instrumentation over decoration: labels are monospace and measured, prose is serif
- Evidence typography: every figure is tabular, every claim ends in a checkable number
- Four locales as a first-class constraint, not a retrofit

## Colors

A cold near-black lit from one source, warm cream ink, and a single red that is never used twice on the same screen for two different reasons.

### Primary
- **Signal Red** (`#ff2f43` dark / `#c30a1c` light): The detector's own colour. Reserved for acquisition marks, the current state, one primary action per view, and figures that are the point of a sentence. Never a background for body copy.

### Neutral
- **Ground** (`#0b0d10` / `#f0ece4`): The page floor. Near-black is chosen for the use scene — this page is read at night, on a phone, by someone deciding whether to reply.
- **Surface** (`#12161b` / `#fffdf9`): Cards, chrome, the instrument panel.
- **Surface Raised** (`#171c23` / `#e7e1d5`): Hover state and the explanation overlay.
- **Bone** (`#f0e9df` / `#16171b`): Primary ink. Warm cream, never pure white; pure white on this ground reads as a screen defect.
- **Bone Secondary** (`#98a1ac` / `#43474f`): Body copy inside cards, lede paragraphs.
- **Muted** (`#7c8794` / `#5d6470`): Monospace labels and metadata.
- **Hairline** (`#242c36` / `#aca291`): Structural dividers.
- **Hairline Interactive** (`#566981` / `#877f72`): Boundaries of things you can act on. ≥3:1 against every surface.

### Named Rules

**The One Signal Rule.** Red marks exactly one thing per view: the action, the current position, or the figure being claimed. When two elements both want it, one of them is wrong about its importance.

**The Warm Ink Rule.** No pure white and no pure black as ink. `#f0e9df` on `#0b0d10`, never `#fff` on `#000`. The only pure values in the system are the image outline and the inset highlight, where a tinted neutral would read as dirt on a photograph.

## Typography

**Display Font:** Bricolage Grotesque (variable; `wdth` 80–92, `wght` 700–800)
**Body Font:** Source Serif 4 (variable; optical sizing on)
**Label/Mono Font:** JetBrains Mono (400 / 500 / 700)

**Character:** A condensed grotesque shouting at display size, a warm serif speaking at reading size, and a monospace measuring at label size. The three voices never trade jobs: the serif never becomes a label, the mono never becomes a sentence.

### Hierarchy
- **Display** (800, `clamp(32px, 10.2vw, 104px)`, 0.9): The page's four or five headline moments. Uppercase, `wdth` 86, authored line breaks inside `.ln` wrappers that clip for the reveal.
- **Headline** (800, `clamp(23px, 5.2vw, 74px)`, 0.94): Section headings.
- **Title** (700, `1.1875rem`, `wdth` 92): Card and row headings, uppercase.
- **Body** (400, `1.09375rem`, 1.6): Serif. Measure capped at 56–62ch depending on column.
- **Label** (400, `0.75rem`, `0.13em`, uppercase): Metadata, section eyebrows, chips, the instrument readout.

### Named Rules

**The Two Unit Rule.** Text sizes are `rem` so the page answers the reader's own browser font size. Display type is the deliberate exception and stays `px + vw`: those lines are authored to break on specific words and live inside `overflow:hidden`, so a doubled root font would clip them silently instead of reflowing.

**The Short Caps Rule.** Uppercase is for labels, never for sentences. Keys are uppercase; their values are not. Under `:lang(ja)` and `:lang(zh)` uppercase and wide tracking are removed entirely — they do nothing to a CJK glyph and pull a run of them into loose beads.

## Layout

A single 1280px `.wrap` with 30px gutters (22px below 560px). Sections breathe at 124px, compacting to 72px below 1000px. Three responsive tiers, gated on height as well as width: the work reel pins and scrubs horizontally only above `1001px × 840px`, because a pinned card on a short viewport clips its own outcome figure.

The chrome is a fixed budget, not a layout: at 360px roughly 330px of width is shared by five controls, and they are ranked by whether the device can do the job without them. Jump links go first (the section is one scroll away), then the theme toggle (the OS setting already covers it); the language control never goes, because nothing else selects it for a reader who was sent the link.

Touch targets are 44px below 980px, the page's own convention, and 24px minimum above it.

## Elevation & Depth

Hybrid, and mostly not shadow. Depth comes from tonal layering (ground → surface → surface-raised), a 1px inset highlight that gives cards a lit top edge, and a real 3D transform layer on pointer-capable devices where cards rotate toward the cursor and lift from the rail.

### Shadow Vocabulary
- **Lift** (`--lift`: `0 26px 60px -24px rgba(0,0,0,.6)` dark / `rgba(0,0,0,.22)` light): The only shadow in the system. Hover and focus on a work card.

### Named Rules

**The Lit Edge Rule.** A surface reads as material because of `inset 0 1px 0 var(--inset-hi)`, not because of a drop shadow. Any rule that sets `box-shadow` on a card must re-state the inset — `box-shadow` is one property, and a bare elevation shadow silently drops the material.

## Shapes

Radii climb with the element's size and importance: 9px on a step indicator, 10px on a schematic, 12px on a photographic frame, 16px on the instrument panel, 18px on a work card, and a full 999px pill on anything that is pressed. Borders are structural, not decorative: 1px `--hairline` for dividers, 1px `--hairline-interactive` for anything actionable. Photographic edges use `outline` at a flat 10–12% of pure white or pure black rather than a tinted border, which would pick up the surface beneath and read as grime on the image.

The recurring silhouette is the four-corner bracket: never a full rectangle, always four L-shaped corners drawn at a fixed 17px regardless of the box they surround.

## Components

### Buttons
- **Shape:** Full pill (`999px`), 52px tall.
- **Primary:** Signal red fill, ground-coloured ink (5.32:1 dark / 6.11:1 light), 28px horizontal padding, mono label at `0.75rem` / `0.15em`.
- **Hover / Focus:** Fill shifts 12% toward bone; press scales to `0.96`.
- **Ghost:** Transparent with a `--hairline-interactive` border; a bone fill wipes upward from the bottom edge on hover over 0.36s.

### Chips (technology tags)
- **Style:** Transparent, 1px hairline, pill, mono `0.75rem`, muted ink.
- **State:** Border and ink brighten on hover and focus; each carries a plain-language explanation as `.sr-only` text read inline by assistive technology and surfaced in the card's overlay for everyone else.

### Cards (work)
- **Corner:** 18px. **Background:** surface → surface-raised on hover.
- **Border:** 1px `--hairline-interactive`; signal red on hover and focus-within.
- **Shadow:** `--lift`, always alongside the inset highlight.
- **Padding:** 32px 30px 28px.
- **Distinctive:** Each card opens with a hand-drawn SVG schematic of its own architecture — deliberately geometric so it can never be mistaken for camera output — and closes with a figure and a route to verify it.

### Navigation
- **Dock:** Fixed pill, centred above 980px and left-anchored below, 1px interactive hairline over 94% surface with a 14px backdrop blur. Links are mono `0.75rem` uppercase, muted, bone when current, with a 1px signal underline pinned to the text centre.
- **Reel stepper:** Four 34px numbered buttons under the pinned card rail; each takes its accessible name from its own card's heading, so it localises with no strings of its own. Arrow keys and `Home`/`End` walk it.

### The Instrument (signature component)
A fixed panel, bottom-left, that follows the scroll, locks onto the section you reach, names it, and shows travel through the document as a hairline. It carries one line of guide copy per section, retracting after a dwell computed from the length of the string in front of the reader. It is `pointer-events: none` — a tour is never worth intercepting a click on a call to action — and it stands down entirely when the contact section enters the viewport.

## Do's and Don'ts

### Do:
- **Do** attach every claim to a number and a route to check it. The page's posture is verifiability; a sentence without evidence weakens the ones that have it.
- **Do** re-state `inset 0 1px 0 var(--inset-hi)` in any rule that sets `box-shadow` on a card.
- **Do** use `rem` for anything a reader reads and `px + vw` for display lines that are authored to break on a specific word.
- **Do** gate pointer-driven depth behind `@media (hover:hover) and (pointer:fine)`. A touch device fires `:hover` on tap and holds it, which leaves a card stuck tilted.
- **Do** keep uppercase to labels, and remove it entirely under `:lang(ja)` and `:lang(zh)`.
- **Do** name any new curve against `--ease-out` rather than introducing a second ease-out.

### Don't:
- **Don't** put body copy on the signal red, or use red for two different meanings on one screen.
- **Don't** use pure white or pure black as ink; the only pure values in the system are the image outline and the inset highlight.
- **Don't** add a tinted border to a photograph. Use `outline` with `--img-outline`.
- **Don't** add a string without adding it to all three translation dictionaries and running `python3 design/i18n/sync.py`, which fails on a missing key, a mismatched array length, a diverged inline-tag sequence, or an orphan.
- **Don't** animate a layout property, and don't let any decorative animation survive `prefers-reduced-motion` — but do keep `opacity` and `visibility` transitions, which are not vestibular motion.
- **Don't** introduce a third-party origin on the critical path. Fonts, motion library and imagery are all self-hosted; the identity is the typography and a locked-down network must not be able to strip it.

## Recorded exceptions to the craft floor

Four rules are knowingly broken. Each is load-bearing, and each will keep
reappearing in an automated scan — they are decisions, not residue.

- **Eyebrows above headings.** The floor bans them; this page keeps eight,
  because they are not decoration. The instrument reads its section labels
  out of `.eyebrow .sr-only` (`labelFor()`, and the `targets` filter that
  builds the tour). Delete the eyebrows and the readout and the seven-stop
  tour silently lose their names. If they ever go, move the labels onto
  `aria-label` on each `<section>` **first**, then remove the markup.
- **Display type in `px + vw`, not `rem`.** See The Two Unit Rule above.
  `h1 .ln` / `h2 .ln` are `overflow:hidden` and their lines are authored to
  break on chosen words per locale; a reader-enlarged root could wrap a line
  inside the clip and hide the second row with no other symptom.
- **SVG text in raw px.** `.viz .tag` (7.5px) and `.field .det text` (1.9px)
  are sized in viewBox user units — they scale with the drawing, not the
  document. `rem` would tie a schematic label to the reader's root size and
  break it at every drawing size.
- **`#000` in mask gradients.** A `-webkit-mask-image` stop is an alpha
  value, not a colour, and does not belong in the palette.

A fifth looks like a violation and is not: low-contrast and
undocumented-colour findings resolve CSS variables to their `@media print`
values. `--sig:#a4121f` renders on paper only. On screen the accent measures
5.32:1 (dark) and 6.11:1 (light) against its actual backgrounds.
