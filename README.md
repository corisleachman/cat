# Catherine Leachman — Counselling, Psychotherapy & Career Coaching

Single-page site. One self-contained `index.html`: no build step, no
framework, no dependencies beyond Google Fonts.

Live: https://corisleachman.github.io/cat/

## Still to do

1. **Connect the enquiry form.** In `index.html`, find
   `action="https://formspree.io/f/YOUR_FORM_ID"` and replace it with a real
   endpoint (Formspree, Basin, or Netlify Forms). Until then the form shows a
   message on submit instead of failing silently.

2. **Replace the two image placeholders.** Search for `class="slot"`. Each one
   is captioned with the ratio and pixel size it expects:
   - 16:9 landscape, ~2000 × 1125 — something quiet: a room, a window, light
   - 4:5 portrait, ~1200 × 1500 — a second, softer portrait

   Swap the whole `<div class="slot">…</div>` for `<img src="…" alt="…"/>`.

3. **Set the Open Graph image to an absolute URL** once the domain is live —
   `<meta property="og:image">` near the top of the file.

4. **Confirm Catherine's qualification wording** in the About section. It
   currently reads "trained at … working towards accreditation", which is
   accurate whether or not the PGDip has formally been awarded.

## Notes

- All motion respects `prefers-reduced-motion`.
- Colours use CSS relative colour syntax (`oklch(from …)`), which needs a
  2023-or-later browser.
