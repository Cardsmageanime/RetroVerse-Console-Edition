"""Platform-neutral product policy for RetroVerse Console Edition.

This model does not authenticate users or enable console execution.
"""
from dataclasses import dataclass
from enum import Enum

class Mode(str, Enum):
    OFFLINE = "offline"
    ONLINE = "online"

class Lobby(str, Enum):
    PUBLIC = "public_online"
    FRIENDS = "friends"
    SPECTATOR = "spectator"
    CREATOR = "creator_host"

@dataclass(frozen=True)
class Session:
    mode: Mode
    local_players: int = 1
    online_players: int = 0
    cheats_enabled: bool = False

    def __post_init__(self):
        if self.local_players < 1 or self.online_players < 0:
            raise ValueError("invalid player count")
        if self.mode is Mode.OFFLINE and self.online_players:
            raise ValueError("offline session cannot have online players")

    @property
    def multiplayer(self) -> bool:
        return self.local_players + self.online_players > 1

    def validate_launch(self) -> None:
        if self.multiplayer and self.cheats_enabled:
            raise ValueError("cheats prohibited in all multiplayer modes")


def can_access_online(*, connected: bool, authenticated: bool, service_available: bool) -> bool:
    return connected and authenticated and service_available


def spectator_can_send_game_input() -> bool:
    return False
