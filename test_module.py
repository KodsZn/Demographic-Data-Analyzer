import unittest
import pandas as pd
import demographic_data_analyzer as dda


class TestDemographicDataAnalyzer(unittest.TestCase):
    
    def test_race_count(self):
        """Test that race_count is a series with correct values"""
        self.assertIsInstance(dda.race_count, pd.Series)
        self.assertEqual(dda.race_count['White'], 27816)
    
    def test_average_age_men(self):
        """Test average age of men is rounded to nearest tenth"""
        self.assertEqual(dda.average_age_men, 39.4)
    
    def test_percentage_bachelors(self):
        """Test percentage of people with bachelor's degree"""
        self.assertEqual(dda.percentage_bachelors, 16.4)
    
    def test_percentage_advanced_over_50k(self):
        """Test percentage of people with advanced education earning >50K"""
        self.assertEqual(dda.percentage_advanced_over_50k, 46.5)
    
    def test_percentage_no_advanced_over_50k(self):
        """Test percentage of people without advanced education earning >50K"""
        self.assertEqual(dda.percentage_no_advanced_over_50k, 17.4)
    
    def test_min_hours_per_week(self):
        """Test minimum hours per week"""
        self.assertEqual(dda.min_hours_per_week, 1)
    
    def test_percentage_min_hours_over_50k(self):
        """Test percentage of minimum hours workers earning >50K"""
        self.assertEqual(dda.percentage_min_hours_over_50k, 10.0)
    
    def test_highest_earning_country(self):
        """Test country with highest earning percentage"""
        self.assertEqual(dda.highest_earning_country, 'Iran')
    
    def test_highest_earning_country_percentage(self):
        """Test percentage of highest earning country"""
        self.assertEqual(dda.highest_earning_country_percentage, 41.9)
    
    def test_most_popular_occupation_india(self):
        """Test most popular occupation for >50K earners in India"""
        self.assertEqual(dda.most_popular_occupation_india, 'Prof-specialty')


if __name__ == '__main__':
    unittest.main()
