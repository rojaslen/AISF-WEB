---
title: "Appendix 4: CDA: Copilot Digital Accessibility Tool"
parent: "Appendices"
nav_order: 5
---

# Appendix 4: CDA: Copilot Digital Accessibility Tool

**License:** CC0 1.0 Universal Public Domain Dedication
**Download:** [Copilot Digital Accessibility v1.0](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-CDA-v1.0){: target="_blank" rel="noopener noreferrer" }

---

## What It Does

The Copilot Digital Accessibility app (CDA) is a lightweight Windows utility that sends a WCAG 2.1 AA compliance directive directly to your clipboard, ready to paste into any AI chat platform. Named for Microsoft Copilot where it was first deployed, but it's platform-agnostic and works with any AI interface that accepts typed or pasted input. 

- Works with Copilot, ChatGPT, Claude, Gemini, and other AI chat platforms
- No installation required; standalone .exe, approximately 76 KB
- No dependencies; no network calls; no data access
- Silent operation; no configuration needed
- Simple 3-step (open-close-paste) workflow

### Directive Contents

>Single‑session ADA/§508 request with silent‑compliance: apply but never mention accessibility unless requested or compliance is impossible.
>Apply mandatory WCAG 2.1 A Floor to all AI output; the AI cannot alter tiers without user approval.
>User may adjust the tier (AA or AAA) but never below floor, and all output must meet the resulting tier without exception.
>Rules:
>- Email/Summary → WCAG 2.1 A structural clarity.
>- UI/Docs → WCAG 2.1 AA technical practices.
>- Image generation → ALT text mandatory.
>- Image‑related output → descriptive ALT text required.
>- Language alignment: auto‑translate only when needed for accessibility alignment; verify consistency; honor explicit user language.

![CDA application window displaying the ready-to-paste WCAG 2.1-AA accessibility compliance block, with a Close button at the bottom](/assets/images/cdapopup.jpg)

## Origin

CDA is a sub-branch of the [AI Stability Framework](https://leonardrojas.com){: target="_blank" rel="noopener noreferrer" }, an independent personal project. The Framework is a client-side middleware system for AI behavioral compliance; CDA is its accessibility layer, extracted, simplified for general use, and donated to the public domain. It was built as a simple, practical tool for coworkers and IT support staff, not designed as a commercial product. The full project is a separate, far larger body of work and remains a personal project; CDA is a public gift derived from it.

## Validation and Deployment

CDA has been independently tested and validated by a blind JAWS screen reader user, who subsequently proposed statewide deployment within the organization (a state government disability services agency). The application and its source code were reviewed and approved by the agency's enterprise IT security team, and it is now in active production use by multiple JAWS users. It cleared ITSEC review because its simple design has nothing to hide and leaves nothing to review: no network functions, no data access or storage, no elevated permissions, no installation.

## License

CC0 1.0 Universal Public Domain Dedication. No attribution required. Free for any use -- personal, commercial, government, or institutional -- without restriction.

[Download CDA v1.0](https://github.com/rojaslen/AISF-downloads/releases/tag/AISF-CDA-v1.0){: target="_blank" rel="noopener noreferrer" }

<nav>
<div class="toc-link"><a href="/#toc">Table of Contents</a></div>
</nav>

---

*Part of the AI Stability Framework(tm), (c)2025-2026 Leonard Rojas. All rights reserved.*
*AI Stability Framework wordmark and logo are trademarks of Leonard Rojas*
*(USPTO Serial Nos. 99664948 and 99749758, registration pending).*
