import unittest
from leap_year_checker import is_valid_year, is_leap_year, classify_years, classify_years_counter

class TestLeapYearChecker(unittest.TestCase):
    #test is_valid_year
    def test_valid_year_data(self):
        years = [2024,1,9999]
        for year in years:
            self.assertTrue(is_valid_year(year))
    
    def test_invalid_year_data(self):
        with self.assertRaises(ValueError):
            is_valid_year(0)
        with self.assertRaises(ValueError):
            is_valid_year(10000)
    
    #test is_leap_year
    def test_leat_year(self):
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(2000))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2023))
        self.assertFalse(is_leap_year(1900))

    #test classify_years
    
    def test_classify_years(self):
        leap_years, non_leap_years = classify_years(2000, 2004)
        self.assertEqual(leap_years, {2000, 2004})
        self.assertEqual(non_leap_years, {2001, 2002,2003})

    def test_classify_years_invalid_range(self):
        with self.assertRaises(ValueError):
            classify_years(2024,2000)

    # test classify_years_counter
    def test_classify_years_counter(self):
        leap_years, non_leap_years = classify_years_counter(2000, 2004)
        self.assertEqual(leap_years, 2)
        self.assertEqual(non_leap_years, 3)

    def test_classify_years_counter_invalid_range(self):
        with self.assertRaises(ValueError):
            classify_years_counter(2024,2000)

if __name__ == "__main__":
    unittest.main()