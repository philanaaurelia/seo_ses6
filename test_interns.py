import unittest
from intern_manager import InternManager

class TestInternManager(unittest.TestCase):
  def setUp(self):
    self.manager = InternManager()
    
  def test_add_intern(self):
    self.assertTrue(self.manager.add_intern("Nicole"))
    self.assertFalse(self.manager.add_intern("Nicole"))
    
  def test_get_intern(self):
    self.manager.add_intern("William")
    self.manager.add_intern("Nathan")
    intern_list = self.manager.get_intern_list()
    self.assertIn("William", intern_list)
    self.assertIn("Nathan", intern_list)
    