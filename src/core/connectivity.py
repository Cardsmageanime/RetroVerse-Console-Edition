"""Deterministic, host-neutral connectivity state and bounded recovery decisions.

No sockets, credentials, network drivers or background worker are created here.
A host adapter supplies verified service reachability and authentication facts.
"""
from dataclasses import dataclass
from enum import Enum

class ConnectionState(str, Enum):
    OFFLINE = "offline"
    NETWORK_ONLY = "network_only"
    AUTH_REQUIRED = "authentication_required"
    ONLINE = "online"

@dataclass(frozen=True)
class Connectivity:
    network_available: bool
    service_reachable: bool
    authenticated: bool

    @property
    def state(self) -> ConnectionState:
        if not self.network_available:
            return ConnectionState.OFFLINE
        if not self.service_reachable:
            return ConnectionState.NETWORK_ONLY
        if not self.authenticated:
            return ConnectionState.AUTH_REQUIRED
        return ConnectionState.ONLINE

def retry_delay_seconds(attempt: int) -> int:
    """Bounded exponential delays, intended for host-driven retries, not sleep."""
    if not isinstance(attempt, int) or attempt < 0:
        raise ValueError("attempt must be a nonnegative integer")
    return min(60, 2 ** min(attempt, 6))

def offline_features_accessible(state: ConnectionState) -> bool:
    """Network transitions never disable host-permitted offline features."""
    return state in ConnectionState
