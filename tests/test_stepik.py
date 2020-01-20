import unittest
import stepik67.lesson1 as L1


class MyTest(unittest.TestCase):
    def test_minutesToHM_1(self):
        self.assertEqual(L1.minutes_from_hm(7, 30), 450)

    def test_minutesToHM_2(self):
        self.assertEqual(L1.minutes_from_hm(0, 42), 42)

    def test_minutes_to_hm_1(self):
        self.assertEqual(L1.minutes_to_hm(480), (8, 0))

    def test_minutes_to_hm_2(self):
        self.assertEqual(L1.minutes_to_hm(512), (8, 32))


if __name__ == "__main__":
    unittest.main()
