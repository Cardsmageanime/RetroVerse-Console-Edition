# RetroVerse Console Edition roadmap

**Status:** Planning and portable policy foundation (v0.1.0). This is a separate application project from RetroVerse Systems Edition's ARM bootable OS. Dates are targets, not guarantees; retail console support depends on manufacturer authorization.

## Implementation update — 2026-10-25 (Desktop Preview 0.2.0-alpha)

- [x] Added a **dependency-free offline browser preview** at [prototype/index.html](../prototype/index.html), preserving distinct Console Edition identity and keeping Systems Edition untouched.
- [x] Added first-pass page navigation for Home, Game Library, Online, Lobbies, Friends, Spectator, Themes, Profiles and Settings.
- [x] Added **prototype** guest profiles (up to eight), browser-local preference persistence, eight theme presets and per-profile accent customization.
- [x] Added **prototype** user-selected, read-only JSON catalog import; no ROM access, scanner or emulator launch.
- [x] Added **preview-only** representations of all four lobbies, explicitly not connected to a server.
- [x] Added basic Gamepad API navigation and static smoke tests (not yet verified on user hardware).
- [ ] Manual browser and controller acceptance tests, accessibility review and automated JavaScript runtime tests are still needed.
- [ ] Full Theme Studio editor/export, real game scanning, music, controller mapping and robust on-disk guest profiles are **not complete**.
- [ ] M2–M6 online services, secure authentication, multiplayer, compatibility matrix and official console ports remain outstanding.

See [preview launch instructions](../prototype/README.md). All original milestones below remain applicable; prototype checkmarks do not imply their completion.

## Implementation update — 2026-10-25 (Theme Studio and connectivity groundwork)

- [x] Add **custom, per-profile color theme presets** to the offline browser preview (save, select, and export/import structured JSON with color validation and size limits).
- [x] Add host-neutral **Connection Recovery state model** distinguishing offline, network-only, authentication-required and online, with capped retry policy and offline access invariants.
- [x] Add unit tests for the connectivity state model.
- [ ] Theme Studio backgrounds, sounds, icon packs and controller-tested editing still outstanding.
- [ ] Real Wi-Fi/Ethernet OS events, secure session restoration, deployed service and real console permissions still outstanding.
- [ ] Manual desktop/browser hardware validation remains outstanding; do not treat this as completed M1.5 or M2.

## Additional foundation work — 2026-10-25

- [x] Theme Studio now exposes accent, background and panel color controls in its offline preview, including JSON theme import/export.
- [x] Added JavaScript parser check for browser preview as a CI unit test (runtime UI behavior still requires manual testing).
- [x] Added evidence-based Game Compatibility Center data model and tests; untested configurations cannot be advertised as verified.
- [ ] No actual emulator/core/platform compatibility has yet been validated; registry contains no real support claims.
- [ ] Manual browser/gamepad verification on Linux Mint is now the first useful owner-assisted acceptance gate.

## Delivery sequence and acceptance gates

### M0 — Baseline, architecture and traceability (October 2026)
- [x] Maintain separate repository from Systems Edition.
- [x] Document source components, feature contracts and platform limitations.
- [x] Create platform-neutral mode/lobby policy model and initial tests.
- [ ] Audit licensing for original RetroVerse code, RetroArch, Libretro cores and distributed assets.
- **Gate:** a traceable feature inventory, clear separation of OS-specific code, and green baseline tests.

### M1 — Offline desktop foundation and guest profiles (November–December 2026)
- [ ] Port original Neon Showcase concepts into an independent Console Edition desktop app, starting on Linux Mint.
- [ ] Implement controller-first Home, Game Library, Profiles, Themes, Settings and placeholder lobby navigation, including focus and display scaling.
- [ ] Support explicit user-approved game directories, local metadata/artwork, favorites and library search; obey host filesystem permissions.
- [ ] Add persistent per-profile settings and local saves.
- [ ] **Offline Guest Profiles:** allow multiple local guest profiles, separate controller mapping, preferences and saves without accounts; define selection, switching and deletion behavior.
- [ ] Keep offline startup fully functional without networking; available solo play remains playable and local multiplayer blocks cheats.
- [ ] Unit/integration tests on Linux Mint.
- **Gate:** disconnect the machine, start Console Edition, switch guest profiles and navigate/game-library browse using a controller, with per-profile settings intact.

### M1.5 — RetroVerse Theme Studio (December 2026–January 2027)
- [ ] Preserve theme presets and original visual identity while giving Console Edition its own interface.
- [ ] **RetroVerse Theme Studio:** create, preview, save, duplicate, export/import permitted theme configurations with color palettes, local backgrounds, UI accents, icons, sound effects and per-profile preferences.
- [ ] Include eight proposed presets: Classic Retro, Neon Night, Anime Style, Cyber Grid, Forest Calm, Space Galaxy, Dark Mode and Sunset Vibes; names are planning proposals, not shipped assets.
- [ ] Provide music shuffle/continuous playback and safe defaults for missing/incompatible content.
- [ ] Respect copyright, accessibility, platform asset rules, performance constraints and sandbox permissions.
- **Gate:** controller-only theme creation, save/reload, per-profile isolation and offline theme operation.

### M2 — Connectivity foundation and Connection Recovery (January–February 2027)
- [ ] Observe host OS network availability (Wi-Fi/Ethernet), without custom network drivers, firmware modifications or platform restriction bypasses.
- [ ] **Connection Recovery:** distinguish local connection, reachable internet, authenticated RetroVerse service and disconnected/error states.
- [ ] Preserve offline library/themes/saves when online services are unavailable; avoid forced sign-in for local use.
- [ ] Implement bounded retry/backoff, connectivity-change responses, secure session resume where tokens and server policy permit, explicit logout and no misleading 'online' indicators.
- [ ] Test Wi-Fi/Ethernet switching, cable unplug/replug, server outages, sleep/wake, token expiry and intermittent connectivity.
- **Gate:** network disruptions never break local mode; recovery neither exposes credentials nor silently bypasses login.

### M3 — Authenticated RetroVerse Online and lobbies (February–April 2027)
- [ ] Implement authenticated, TLS-protected service with secure tokens, rate limits, abuse controls, privacy and moderation.
- [ ] Implement Friends, presence, invitations, room creation/join/leave, and chat.
- [ ] Preserve all four lobby classes: **Public Online Lobby**, **Friends Lobby**, **Spectator Lobby**, **Creator/Host Lobby**; private invite rooms default private.
- [ ] Enforce room roles and permissions on the server; spectators are read-only and cannot inject game inputs.
- [ ] Enforce cheat prohibition in all multiplayer sessions, including local/private sessions, before joining/launching; online policy is server authoritative.
- [ ] **Universal Room Browser:** browse/search/filter compatible public rooms, permitted friends' rooms and spectator-enabled rooms; show accurate game/platform/core-version compatibility, access/privacy, player/spectator counts, and join eligibility.
- [ ] Graceful online/offline transitions integrate with M2 connectivity recovery.
- **Gate:** authenticated test clients create, discover and join authorized rooms; unauthorized users cannot enter private rooms or elevate spectator rights; recovery and moderation tests pass.

### M4 — Game Compatibility Center and compatible gameplay (April–July 2027)
- [ ] **Game Compatibility Center:** maintain a verified matrix of host platform, app version, emulator/core version, game/content identifier, controller capability, network mode and tested status.
- [ ] Present only verified support states (e.g., tested compatible, tested incompatible, untested); preserve evidence and last-tested version/date.
- [ ] Never infer working compatibility solely from CPU architecture, console branding, matching extensions or another emulator's claim.
- [ ] Add legally usable emulator adapters where platform authorization and upstream license permit.
- [ ] Prototype compatible multiplayer synchronization and spectator viewing; no claims of rollback or cross-emulator play until proved.
- [ ] Test latency, disconnect/rejoin, role enforcement, input integrity, saves and platform/core interoperability.
- **Gate:** a documented reproducible compatibility suite and real two-client session tests; unsupported combinations are clearly shown as such.

### M5 — Packaging, stability and safe updates (August–October 2027)
- [ ] Verify licenses, content distribution rights and assets.
- [ ] Preserve profiles, saves, theme configurations and library metadata through app upgrades where platform APIs permit.
- [ ] Add crash reporting with consent, accessibility/performance testing, backup/restore and release checks.
- [ ] Keep application updates distinct from console firmware updates; never promise automatic compatibility with unsupported console firmware.
- **Gate:** reproducible desktop package, clean-install/upgrade tests and no save-loss regressions.

### M6 — Manufacturer-authorized console tracks (late 2027–2028; conditional)
- [ ] Seek Sony/PlayStation partner and SDK authorization.
- [ ] Seek Nintendo developer and SDK authorization.
- [ ] Seek Microsoft/Xbox authorized retail distribution and SDK route (not mandatory Developer Mode in retail experience).
- [ ] Build isolated platform adapters only using permitted SDKs, APIs, network/storage paths and signed distribution.
- [ ] Test platform-specific restrictions on themes, storage, networking, emulation, accounts, chat and updates.
- [ ] Publish only on platforms explicitly approved and tested; mark others unsupported.
- **Gate:** documented permissions, certification/compliance and successful hardware tests per platform.

## Non-negotiable requirements
- No jailbreaks, exploits, bootloader modification, custom console firmware, or unauthorized USB boot.
- Console Edition is an application, **not** the ARM USB/SD operating system.
- Offline use requires no RetroVerse account or internet for eligible local content.
- Online services depend on network access, authentication, server availability and host-platform policy; either Wi-Fi or Ethernet may transport permitted traffic.
- Multiplayer cheats prohibited without exceptions; spectators have no game-input authority.
- Original Systems Edition's kernel, bootloaders, DTBs, Versus Tree, root filesystem and hardware-boot tests remain in its repository unchanged.
- The current Systems Edition UI, local chat service and library scanner are **prototypes**, not production console functionality.
- No public console availability or cross-platform netplay claims before authorization and real testing.
