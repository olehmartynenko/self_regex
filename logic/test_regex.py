import unittest
from regex import *

class RegexMatcherTests(unittest.TestCase):
    def test_is_start(self):
        self.assertTrue(is_start('^'))
        self.assertFalse(is_start('a'))

    def test_is_end(self):
        self.assertTrue(is_end('$'))
        self.assertFalse(is_end('a'))

    def test_is_star(self):
        self.assertTrue(is_star('*'))
        self.assertFalse(is_star('a'))

    def test_is_plus(self): 
        self.assertTrue(is_plus('+'))
        self.assertFalse(is_plus('a'))  

    def test_is_question(self):             
        self.assertTrue(is_question('?'))
        self.assertFalse(is_question('a'))
    
    def test_is_operator(self): 
        self.assertTrue(is_operator('*'))
        self.assertTrue(is_operator('+'))
        self.assertTrue(is_operator('?'))
        self.assertFalse(is_operator('a'))
        