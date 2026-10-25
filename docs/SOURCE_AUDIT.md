# Systems Edition source audit for Console Edition

Original repository: https://github.com/Cardsmageanime/RetroVerse

| Source | Existing state | Plan |
| --- | --- | --- |
| interface/neon-showcase, interface/title-screen | Browser UI prototype | Port navigation and interaction patterns; new platform adapters |
| library/scan_library.py, removable_discovery.py, library_ui_server.py | Opt-in, local read-only scanning on mounted Linux directories | Use permission-aware storage abstraction; no console internal filesystem access |
| library/README.md | Drive picker, offline metadata JSON with embedded artwork | Retain local metadata schema concept and explicit user selection |
| online/protocol.py | Local JSON message validator, version 1 | Adapt message contracts and add security tests |
| online/server/lobby_server.py | Loopback-only asyncio JSON-lines room/chat prototype, ephemeral state | Reference behavior only; never deploy on public network as-is |
| docs/ONLINE_FOUNDATION.md | Auth, cheats, lobby security specs | Maintain as normative requirements |
| docs/ONLINE_AND_ARM_UI_MILESTONE.md | Explicit prototype limitations and integration gates | Adopt readiness gates |
| tests/test_gamepad.js, tests/test_controller_detection.js, tests/test_music.js | Existing interface/input/music tests | Adapt tests to new runtime |
| boot/, kernel/, hardware/, rootfs/ | ARM boot infrastructure | DO NOT COPY (Systems Edition only) |

Working prototypes are not demonstrated compatible with retail consoles. No ROMs, BIOS images or third-party core binaries are included.
