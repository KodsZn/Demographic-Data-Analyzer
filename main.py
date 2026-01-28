"""
Main test file - runs the tests from test_module
"""
import unittest
from test_module import TestDemographicDataAnalyzer

if __name__ == '__main__':
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDemographicDataAnalyzer)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
