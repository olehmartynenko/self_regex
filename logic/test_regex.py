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

    def test_is_dot(self):
        self.assertTrue(is_dot('.'))
        self.assertFalse(is_dot('a'))
    
    def test_is_escape_sequence(self):
        self.assertTrue(is_escape_sequence('\\a'))
        self.assertFalse(is_escape_sequence('a'))
    
    def test_is_escape(self):
        self.assertTrue(is_escape('\\'))
        self.assertFalse(is_escape('a'))
    
    def test_is_open_alternate(self):
        self.assertTrue(is_open_alternate('('))
        self.assertFalse(is_open_alternate('a'))
    
    def test_is_close_alternate(self):
        self.assertTrue(is_close_alternate(')'))
        self.assertFalse(is_close_alternate('a'))
    
    def test_is_open_set(self):
        self.assertTrue(is_open_set('['))
        self.assertFalse(is_open_set('a'))
    
    def test_is_close_set(self):
        self.assertTrue(is_close_set(']'))
        self.assertFalse(is_close_set('a'))
    
    def test_is_literal(self):
        self.assertTrue(is_literal('a'))
        self.assertTrue(is_literal('1'))
        self.assertTrue(is_literal(' '))
        self.assertTrue(is_literal(':'))
        self.assertTrue(is_literal('/'))
        self.assertFalse(is_literal('*'))
    