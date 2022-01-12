import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should indicate you are eating healthy"""
        self.assertEqual(
            eat("brocoli", is_healthy=True),
            "I'm eating brocoli, because my body is a temple."
        )
    def test_eat_unhealhly(self):
        """eat should indicate you are eating unhealthy"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )
    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        """Long naps should be discouraging """
        self.assertEqual(
            nap(3),
            "Ugh I overslept. I didn't mean to nap for 3 hours"
        )

if __name__ == "__main__":
    unittest.main()
