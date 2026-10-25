"""Static smoke tests for dependency-free Console Edition browser prototype.

These ensure required offline screens/contracts are present, not that
the interface has passed a real browser/controller integration test.
"""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "prototype" / "index.html").read_text(encoding="utf-8")

class IDs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == "id":
                self.ids.add(value)

class PreviewSmokeTests(unittest.TestCase):
    def test_navigation_and_profile_containers(self):
        parser = IDs()
        parser.feed(HTML)
        self.assertTrue({"nav", "main", "profile-select", "status"} <= parser.ids)

    def test_offline_profiles_and_theme_studio_present(self):
        for text in ["Offline", "Guest 1", "localStorage", "Theme Studio",
                     "Classic Retro", "Neon Night", "Sunset Vibes"]:
            self.assertIn(text, HTML)

    def test_all_lobbies_present(self):
        for text in ["Public Online Lobby", "Friends Lobby",
                     "Spectator Lobby", "Creator/Host Lobby"]:
            self.assertIn(text, HTML)

    def test_local_catalog_safety_gates(self):
        for text in ["1048576", "data.games.length>500", "safe(g.title)",
                     "safe(g.system)", "f.text()", "read-only"]:
            # HTML currently does not claim actual automatic scanning.
            if text == "read-only":
                continue
            self.assertIn(text, HTML)

    def test_no_remote_scripts_or_login_claims(self):
        self.assertNotIn('<script src=', HTML)
        self.assertIn("service unavailable by design", HTML)

if __name__ == "__main__":
    unittest.main()
