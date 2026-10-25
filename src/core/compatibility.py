"""Evidence-based compatibility registry (no asserted real console support)."""
from dataclasses import dataclass
from enum import Enum
from datetime import date

class Verdict(str, Enum):
    UNTESTED = "untested"
    COMPATIBLE = "tested_compatible"
    INCOMPATIBLE = "tested_incompatible"

@dataclass(frozen=True)
class Evidence:
    platform: str
    core: str
    core_version: str
    content_id: str
    verdict: Verdict
    tested_on: date | None = None
    test_reference: str | None = None

    def __post_init__(self):
        if not all((self.platform.strip(), self.core.strip(), self.core_version.strip(), self.content_id.strip())):
            raise ValueError("platform, core, version and content identity required")
        if self.verdict is not Verdict.UNTESTED and (self.tested_on is None or not self.test_reference):
            raise ValueError("tested claims require date and reproducible evidence")

def verified_support(item: Evidence) -> bool:
    return item.verdict is Verdict.COMPATIBLE and bool(item.test_reference)
