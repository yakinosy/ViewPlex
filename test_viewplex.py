# test_viewplex.py
"""
Tests for ViewPlex module.
"""

import unittest
from viewplex import ViewPlex

class TestViewPlex(unittest.TestCase):
    """Test cases for ViewPlex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ViewPlex()
        self.assertIsInstance(instance, ViewPlex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ViewPlex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
