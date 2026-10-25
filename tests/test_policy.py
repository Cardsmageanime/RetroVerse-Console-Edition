import unittest
from src.core.policy import Mode, Lobby, Session, can_access_online, spectator_can_send_game_input

class PolicyTests(unittest.TestCase):
    def test_solo_offline_cheats(self):
        Session(Mode.OFFLINE, cheats_enabled=True).validate_launch()

    def test_local_multiplayer_cheats_blocked(self):
        with self.assertRaises(ValueError):
            Session(Mode.OFFLINE, local_players=2, cheats_enabled=True).validate_launch()

    def test_online_multiplayer_cheats_blocked(self):
        with self.assertRaises(ValueError):
            Session(Mode.ONLINE, online_players=1, cheats_enabled=True).validate_launch()

    def test_offline_cannot_have_online_players(self):
        with self.assertRaises(ValueError):
            Session(Mode.OFFLINE, online_players=1)

    def test_requires_connection_account_and_service(self):
        for c, a, s in [(False, True, True), (True, False, True), (True, True, False)]:
            self.assertFalse(can_access_online(connected=c, authenticated=a, service_available=s))
        self.assertTrue(can_access_online(connected=True, authenticated=True, service_available=True))

    def test_four_lobby_types(self):
        self.assertEqual(len(Lobby), 4)

    def test_spectators_never_send_game_input(self):
        self.assertFalse(spectator_can_send_game_input())

if __name__ == "__main__":
    unittest.main()
