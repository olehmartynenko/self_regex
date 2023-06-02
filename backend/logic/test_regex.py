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

    def test_is_alternate(self):
        self.assertTrue(is_alternate('(a|b)'))
        self.assertFalse(is_alternate('a'))
    
    def test_is_set(self):
        self.assertTrue(is_set('[XYZ]'))
        self.assertFalse(is_set('a'))
    
    def test_is_unit(self):
        self.assertTrue(is_unit('.'))
        self.assertTrue(is_unit('[XYZ]'))
        self.assertTrue(is_unit('\\a'))
        self.assertFalse(is_unit('('))
    
    def test_split_alternate(self):
        self.assertEqual(split_alternate('(a|b)'), ['a', 'b'])
        self.assertEqual(split_alternate('(a)'), ['a'])
        self.assertEqual(split_alternate('(a|b|c|d|e)'), ['a', 'b', 'c', 'd', 'e'])
    
    def test_split_set(self):
        self.assertEqual(split_set('[XYZ]'), ['X', 'Y', 'Z'])
        self.assertEqual(split_set('[357]'), ['3', '5', '7'])
    
    def test_does_unit_match(self):
        self.assertTrue(does_unit_match('a', 'a'))
        self.assertTrue(does_unit_match('.', 'a'))
        self.assertTrue(does_unit_match('[abc]', 'a'))
        self.assertFalse(does_unit_match('[xyz]', 'a'))
    
    def test_match_multiple(self):
        self.assertTrue(match_multiple('a', 'a', 0))
        self.assertTrue(match_multiple('a*', 'aaaa', 0))
        self.assertTrue(match_multiple('a*', '', 0))
    
    def test_match_plus(self):
        self.assertTrue(match_plus('a+', 'aaaa', 0))
        self.assertFalse(match_plus('a+', '', 0)[0])
    
    def test_match_question(self):
        self.assertTrue(match_question('a?', 'a', 0))
        self.assertTrue(match_question('a?', '', 0))
    
    def test_match_star(self):
        self.assertTrue(match_star('a*', 'aaaa', 0))
        self.assertTrue(match_star('a*', '', 0))
    
    def test_match_alternate(self):
        self.assertTrue(match_alternate('(a|b)', 'a', 0))
        self.assertTrue(match_alternate('(a|b)', 'b', 0))
        self.assertFalse(match_alternate('(a|b)', 'c', 0)[0])

    def test_match_expression(self):
        self.assertTrue(match_expression('abc*', 'abccc'))
        self.assertTrue(match_expression('a[bc](x|y)+', 'abxxxyy'))
        self.assertFalse(match_expression('a[bc]z+', 'abxxxyyz')[0])

    def test_match(self):
        self.assertEqual(match('abc*', 'abccc'), ['abccc'])
        self.assertEqual(match('a[bc](x|y)+', 'abxxxyy'), ['abxxxyy'])
        self.assertEqual(match('a+[bc]?', 'aaaxaaxab'), ['aaa', 'aa', 'ab'])
    
    def test_replace_matches(self):
        self.assertEqual(replace_matches('abc*', 'abccc', 'XYZ'), 'XYZ')
        self.assertEqual(replace_matches('a[bc](x|y)+', 'abxxxyy', 'XYZ'), 'XYZ')
        self.assertEqual(replace_matches('a+[bc]?', 'aaaxaaaaaxab', 'XYZ'), 'XYZxXYZxXYZ')
        