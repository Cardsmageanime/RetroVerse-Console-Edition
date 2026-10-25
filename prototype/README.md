# RetroVerse Console Edition — offline desktop browser preview

Open `prototype/index.html` in a modern browser on Linux Mint or Windows; the file requires no server, account, network, downloads or proprietary console SDKs. It is **not a working emulator** and does not connect to RetroVerse Online.

Implemented in the preview:
- Home, Game Library, Online, Lobbies, Friends, Spectator, Themes, Profiles and Settings pages.
- Eight theme presets plus individually saved accent colors.
- Up to eight local guest profiles with per-profile catalog/preferences, stored in the browser's localStorage.
- Explicit JSON game-catalog import (max 1 MB / 500 entries, names/systems only; no ROM access or launching).
- Four nonfunctional lobby preview panels labeled as offline placeholders.
- Navigation with mouse/keyboard and basic Gamepad API controls: LB/RB moves between pages, D-pad Up/Down cycles focused controls, A activates focused controls. Browser support varies.
- No telemetry or network requests.

Sample catalog:
```json
{"games":[{"title":"My Homebrew Game","system":"SNES"},{"title":"Another Game","system":"Genesis"}]}
```

Limitations:
- This version is a **browser prototype**; controller support, localStorage persistence, accessibility and profile integrity still need real desktop testing.
- No local filesystem scanning, games, core loading, saves, audio playback, online account, TLS service, lobby membership, matchmaking, netplay or spectating implementation.
- Browser storage may be unavailable or cleared in private browsing.
- No claimed compatibility with retail PlayStation, Xbox or Nintendo hardware.
- Keep original ARM boot development in the separate Systems Edition repository.

Automated static + portable policy checks: `python3 -m unittest discover -s tests -v` from the repository root. Browser/manual tests are still required.
