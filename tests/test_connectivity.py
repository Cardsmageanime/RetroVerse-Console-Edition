import unittest
from src.core.connectivity import ConnectionState, Connectivity, retry_delay_seconds, offline_features_accessible

class ConnectivityTests(unittest.TestCase):
    def test_all_states(self):
        cases = [
            ((False, False, False), ConnectionState.OFFLINE),
            ((True, False, False), ConnectionState.NETWORK_ONLY),
            ((True, True, False), ConnectionState.AUTH_REQUIRED),
            ((True, True, True), ConnectionState.ONLINE),
            ((False, True, True), ConnectionState.OFFLINE),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertEqual(Connectivity(*args).state, expected)
                self.assertTrue(offline_features_accessible(expected))

    def test_bounded_retry(self):
        self.assertEqual([retry_delay_seconds(i) for i in range(8)], [1, 2, 4, 8, 16, 32, 60, 60])
        self.assertEqual(retry_delay_seconds(100), 60)
        with self.assertRaises(ValueError):
            retry_delay_seconds(-1)
