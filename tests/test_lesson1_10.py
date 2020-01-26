import unittest
import stepik67.lesson1_10 as L1_10


class SleepAndYearTestCase(unittest.TestCase):
    def test_sleep_for_health_less(self):
        self.assertEqual(L1_10.sleep_for_health(10, 15, 5), 'Недосып')

    def test_sleep_for_health_more(self):
        self.assertEqual(L1_10.sleep_for_health(10, 15, 25), 'Пересып')

    def test_sleep_for_health_normal(self):
        self.assertEqual(L1_10.sleep_for_health(10, 15, 12), 'Это нормально')

    def test_is_year_vis_true(self):
        self.assertEqual(L1_10.is_year_vis(2000), 'Високосный')
        self.assertEqual(L1_10.is_year_vis(2004), 'Високосный')

    def test_is_year_vis_false(self):
        self.assertEqual(L1_10.is_year_vis(1900), 'Обычный')
        self.assertEqual(L1_10.is_year_vis(3000), 'Обычный')
        self.assertEqual(L1_10.is_year_vis(2100), 'Обычный')


if __name__ == "__main__":
    unittest.main()
