# Console Edition foundation v0.1.0

## Source of truth and separation
Derived from Cardsmageanime/RetroVerse (Systems Edition), especially docs/ONLINE_FOUNDATION.md, docs/ONLINE_AND_ARM_UI_MILESTONE.md, library/README.md, online/protocol.py, and interface/neon-showcase. Original ARM kernel, rootfs, DTB, SD/USB boot, and Versus Tree work remains in Systems Edition. No bootloader, kernel, rootfs, or machine-specific drivers are copied into Console Edition.

## Product
Console Edition is an application, not a bootable USB operating system. Host firmware must remain unchanged. Retail PlayStation/Nintendo/Xbox builds are targets conditional on official SDK access, code signing, licenses and manufacturer approval; never assume a working retail distribution channel. No jailbreaks, exploits, modified firmware, or mandatory Developer Mode.

## Feature contracts
- Controller-first UI: Home, Game Library, Online Play, Friends, Lobbies, Spectator, Profiles, Themes, Settings.
- Customization: Classic Retro, Neon Night, Anime Style, Cyber Grid, Forest Calm, Space Galaxy, Dark Mode, Sunset Vibes; backgrounds, colors, icons, sounds, optional generated backgrounds, shuffle/continuous music, respect licensed assets and host policies.
- Library: explicitly user-approved directories and platform-permitted storage, local game labels, artwork metadata, favorites, saves. No scanning internal console partitions or bypassing storage permissions.
- Offline: no online account, Wi-Fi or Ethernet needed for available solo games, controller mapping, settings, locally installed themes, local saves, and single-player cheats where permitted.
- Online: requires connection and RetroVerse Online account; expose Public Online, Friends, Spectator, Creator/Host lobbies with room metadata, privacy, invitations, game/platform compatibility and chat.
- Multiplayer security: no cheats in *any* multiplayer session (local or online); deny launch/join if cheats enabled, server enforces online policy; spectators read-only and cannot inject inputs. Default private for invite-only rooms.
- Transport: OS-provided Wi-Fi/Ethernet connectivity; network-state observer handles online/offline/reconnection, never administers or overrides platform networking. TLS, authentication, token handling, room permissions, moderation and rate limits before internet exposure.
- Updates: app update only through approved stores/distribution paths, preserve local saves/settings subject to host sandbox constraints.
- Netplay and cross-platform spectatorship are future capabilities; require compatible cores, input synchronization, permissions, network tests and platform approval. No guarantee all emulators/consoles can play each other.

## Existing evidence
Systems Edition has a Neon browser UI prototype, a loopback-only room/chat prototype, protocol validation, drive selection, library scan, and automated tests. The original README says it is not a bootable ready-to-flash image. Reuse concepts/tests and port safe modules after code review; do not describe these as production-ready console implementations.
