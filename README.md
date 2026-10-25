# RetroVerse Console Edition

**Status: Foundation v0.1.0 (planning + initial portable policy code). Not a released console app.**

RetroVerse Console Edition is a separate cross-platform application track inspired by the original [RetroVerse Systems Edition](https://github.com/Cardsmageanime/RetroVerse). It targets officially authorized console environments **without** jailbreaks, exploits, modified firmware, or a required Developer Mode in the retail experience. PlayStation, Nintendo and Xbox retail compatibility **is not currently established**; official SDK, licensing and distribution approval are prerequisites.

## Runnable desktop preview (0.2.0-alpha)

A first **offline browser-based Console Edition prototype** is available at [prototype/index.html](prototype/index.html). Download the repository or the file and open it in a modern browser on Linux Mint/Windows. It includes guest profiles, theme presets, a local JSON game-catalog viewer, basic gamepad navigation and offline placeholder lobby screens.

Read [preview setup, controls and limitations](prototype/README.md). It is not an emulator, online service, or authorized retail console app; these remain roadmap work.

## Features we are building
- Controller-first fullscreen home screen, Game Library, Profiles, Friends, Online Play, Spectator, Themes and Settings.
- Eight established theme presets, customizable colors/backgrounds/icons/sounds, and optional music shuffle.
- Offline local solo gaming with no RetroVerse account or connection required (subject to permitted content and host APIs).
- Optional RetroVerse Online with Public, Friends, Spectator and Creator/Host lobbies, permissions, chat and invitations.
- Host-provided Ethernet/Wi-Fi access, resilient online/offline transitions, secure connection handling.
- Local multiplayer and online multiplayer **must block cheats**; spectators cannot inject inputs.
- Shared game metadata and compatible emulator adapters where licensed and allowed by the platform.

## Technical status
The original project contains browser UI, library scanning and loopback-only chat/lobby prototypes. This new repository **does not yet include** their ported user interface, public online service, working emulator, or console SDK builds.

The initial portable policy model is in [src/core/policy.py](src/core/policy.py) with tests in [tests/test_policy.py](tests/test_policy.py).

## Documents
- [Foundation and feature contracts](docs/FOUNDATION.md)
- [Development roadmap](docs/ROADMAP.md)
- [Original repository audit](docs/SOURCE_AUDIT.md)
- [Platform authorization requirements](docs/PLATFORM_REQUIREMENTS.md)

Run initial local tests on Python 3: `python3 -m unittest discover -s tests -v`

## Project separation
ARM-specific kernel, device trees, bootloader, hardware profiles, and root filesystem stay exclusively in the original Systems Edition repository. Console Edition contains a host application and may reuse reviewed portable logic, tests, service contracts, and UI concepts.

**Safety:** no proprietary console SDKs, copyrighted games, BIOS files or emulator binaries have been included. License and platform review required before redistribution.
