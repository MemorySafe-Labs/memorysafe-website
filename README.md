# Cross-assistant animation preview

SOURCE OF THE LIVE SITE since 28 Oct 2026 (last deploy 3 Nov 2026: Pricing page with live Stripe links; see ../README.md). Derived from claudete-preview-2026-10-22. Build with `python3 build.py`; deploy = `public/` minus `preview-mobile.html`, zipped and uploaded with Netlify Drop.

The homepage animation now demonstrates Claude Desktop saving a fictional Aurora/Vue preference to MemorySafe and Codex retrieving it in a new conversation. A persistent memory card and directional light pulses connect the assistants. English and Portuguese copy included. Manual step selection pauses; playback pauses offscreen and when hidden; reduced motion starts at the completed scene. No memory tools or API calls are made by this demonstration.

Build: `python3 build.py`
Preview: `python3 -m http.server 4199 --bind 127.0.0.1 --directory public`

Changes: hero_demo and playback controller in build.py; scoped handoff styles at the end of public/style.css. Generated homepage HTML and site.js are rebuilt. Other site content is inherited, not updated for current hosted-product availability.

Checked: build, JavaScript syntax, browser step controls and resume, English desktop/tablet layout, Portuguese layout in a phone-width iframe, no browser error logs. Reduced-motion behavior preserved in code, not separately emulated. QA-only public/preview-mobile.html must be excluded from any deployment.

Review URL: http://127.0.0.1:4199/
Screenshot: ../../outputs/cross-agent-animation-preview.png

Publication requires Carla's go under the original website handoff. Before publication, compare against the current live source to preserve any intervening edits; copy only the animation changes into the selected release.

App logo assets: Claude from /Applications/Claude.app/Contents/Resources/electron.icns; Codex from /Applications/ChatGPT.app/Contents/Resources/app.icns. Converted to PNG and resized proportionally with sips. Original marks preserved.
