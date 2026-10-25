# Console Edition roadmap

## M0: baseline and traceability
- [x] Keep separate repository.
- [x] Record source components, product rules and supported/unsupported distinctions.
- [x] Create platform-neutral mode/lobby policy model and tests.
- [ ] Audit licenses of original code, RetroArch and each core before redistribution.

## M1: functional Linux desktop development harness
- [ ] Port original Neon Showcase navigation to dedicated Console Edition UI.
- [ ] Controller-based navigation, focus and accessible display scaling.
- [ ] Local permitted-game library and metadata workflow.
- [ ] Theme presets, UI colors, backgrounds, sound and music settings.
- [ ] Persistent user settings and local save system.
- [ ] Unit and integration tests using Linux Mint.

## M2: connectivity / social prototype
- [ ] OS connectivity observer (Wi-Fi or Ethernet through host APIs).
- [ ] Offline-first state transitions, reconnect and graceful degradation.
- [ ] Four lobby UIs and room membership/permissions.
- [ ] Authenticated TLS service, chat, friends, invitations and moderation.
- [ ] Server-side enforcement of ban, permissions and no-cheat multiplayer policy.
- [ ] Spectator data path with read-only permission checks.
- [ ] Compatibility testing; netplay integration only after real gameplay tests.

## M3: emulator + packaging
- [ ] Document licenses, core compatibility and game content rights.
- [ ] Legal local emulator adapter where permitted.
- [ ] Update/save preservation, runtime failure recovery, release signing pipeline.

## M4: official consoles (conditional)
- [ ] Seek official PlayStation partner/SDK authorization.
- [ ] Seek official Nintendo developer/SDK authorization.
- [ ] Seek official Xbox platform approval and retail distribution route.
- [ ] Implement isolated platform adapters only within authorized APIs.
- [ ] Validate storage, network, input and store compliance on each supported device.

No public release or compatibility claims until tests and authorization pass.
