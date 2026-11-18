# Catherine Leachman — Counselling, Psychotherapy & Career Coaching

Single-page site. One self-contained `index.html`: no build step, no
framework, no dependencies beyond Google Fonts.

Live (Vercel, serves the `alt/` design at the root): https://catherine-leachman.vercel.app
Older GitHub Pages copy: https://corisleachman.github.io/cat/

## Hosting and the enquiry form

- Vercel project `catherine-leachman` deploys automatically on every push to `main`.
  `vercel.json` builds `public/` from `alt/index.html` plus the images.
- The form posts to `api/contact.js`, which emails enquiries to
  catherineleachmanwellness@gmail.com via Resend (sender: enquiries@corisleachman.com,
  reply-to: the enquirer). It needs `RESEND_API_KEY` set in Vercel; `CONTACT_TO` and
  `CONTACT_FROM` env vars can override the recipient and sender.

## Still to do

1. **Enquiry form on the original `index.html`** still points at a placeholder;
   the live (alt) design is wired up. Point it at `/api/contact` if it is ever used.

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
