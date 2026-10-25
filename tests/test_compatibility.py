import unittest
from datetime import date
from src.core.compatibility import Evidence, Verdict, verified_support

class CompatibilityTests(unittest.TestCase):
    def test_untested_is_never_supported(self):
        record = Evidence("Linux desktop","example-core","0.1","homebrew-01",Verdict.UNTESTED)
        self.assertFalse(verified_support(record))

    def test_claim_requires_evidence(self):
        with self.assertRaises(ValueError):
            Evidence("Xbox","core","1","game",Verdict.COMPATIBLE)
        with self.assertRaises(ValueError):
            Evidence("PlayStation","core","1","game",Verdict.INCOMPATIBLE, date(2026,10,25))

    def test_evidenced_result(self):
        record = Evidence("Linux desktop","example-core","0.1","homebrew-01",Verdict.COMPATIBLE,date(2026,10,25),"test-log/example-001")
        self.assertTrue(verified_support(record))
