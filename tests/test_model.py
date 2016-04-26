import unittest
from datetime import datetime

from models.Mvp import Mvp


class MvpTest(unittest.TestCase):
    """Testing class for Mvp."""

    def setUp(self):
        self.mvp = Mvp("Atroce", 120, 'ra_field03')

    def test_time_before_spawn(self):
        now = datetime.now()
        self.mvp.last_death = datetime(now.year, now.month, now.day, now.hour-1,
                                       minute=now.minute)
        self.assertAlmostEqual(self.mvp.next_respawn(), 60, delta=2)

    def test_time_after_spawn(self):
        now = datetime.now()
        self.mvp.last_death = datetime(now.year, now.month, now.day, now.hour-3,
                                       minute=now.minute)
        self.assertAlmostEqual(self.mvp.next_respawn(), -60, delta=2)

    def test_time_uninitialized(self):
        value = self.mvp.next_respawn()
        self.assertEqual(value, None,
                         "Mvp next respawn returned {}!".format(value))

if __name__ == '__main__':
    unittest.main()
