# AISF-WEB Changelog

## 2026-04-03

### Site infrastructure
- Replaced Just the Docs remote theme with custom accessible layout
  - `_layouts/default.html`: semantic HTML, proper `<main>`, skip link, Liquid nav, no JS on desktop
  - `assets/css/style.css`: CSS custom properties, system light/dark via prefers-color-scheme
  - `_config.yml`: stripped to essentials; layout default set globally
- Added Inter variable font (self-hosted, SIL OFL): `assets/fonts/Inter-Variable/web/InterVariable.woff2`
- Mobile nav collapse via `<details>`/`<summary>` + minimal JS (removes `open` attr at narrow viewport)
- Link colors deferred to browser/system defaults (accessibility: user customizations respected)

### AT testing
- JAWS 2026 + Firefox 149: virtual buffer fails site-wide (platform regression, not site bug)
  - Insert+F7 links list returns "must be in a virtual document"
  - JAWS not entering browse mode at all in Firefox 149
  - F5 refresh does not resolve
  - ZoomText component (same Fusion install) reads normally
  - Chrome/Chromium: virtual buffer works correctly with JAWS 2026
- iOS VoiceOver + Safari: confirmed working
- Chrome, DuckDuckGo browser (iOS): confirmed working
