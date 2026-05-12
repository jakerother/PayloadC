# test_payloadcms.py
"""
Tests for PayloadCMS module.
"""

import unittest
from payloadcms import PayloadCMS

class TestPayloadCMS(unittest.TestCase):
    """Test cases for PayloadCMS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PayloadCMS()
        self.assertIsInstance(instance, PayloadCMS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PayloadCMS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
