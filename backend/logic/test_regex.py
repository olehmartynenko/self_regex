import unittest
from regex import *


class RegexMatcherTests(unittest.TestCase):
    def test_is_start(self):
        # Arrange
        start = '^'
        not_start = 'a'
        # Act
        true = is_start(start)
        false = is_start(not_start)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)

    def test_is_end(self):
        # Arrange
        end = '$'
        not_end = 'a'
        # Act
        true = is_end(end)
        false = is_end(not_end)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)

    def test_is_star(self):
        # Arrange
        star = '*'
        not_star = 'a'
        # Act
        true = is_star(star)
        false = is_star(not_star)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)

    def test_is_plus(self): 
        # Arrange
        plus = '+'
        not_plus = 'a'
        # Act
        true = is_plus(plus)
        false = is_plus(not_plus)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false) 

    def test_is_question(self):             
        # Arrange
        question = '?'
        not_question = 'a'
        # Act
        true = is_question(question)
        false = is_question(not_question)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_alternate(self):
        # Arrange
        alternate = '(a|b)'
        not_alternate = 'a'
        # Act
        true = is_alternate(alternate)
        false = is_alternate(not_alternate)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_operator(self): 
        # Arrange
        operator = '*'
        not_operator = 'a'
        # Act
        true = is_operator(operator)
        false = is_operator(not_operator)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_open_count(self):
        # Arrange
        open_count = '{'
        not_open_count = 'a'
        # Act
        true = is_open_count(open_count)
        false = is_open_count(not_open_count)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_open_set(self):
        # Arrange
        open_set = '['
        not_open_set = 'a'
        # Act
        true = is_open_set(open_set)
        false = is_open_set(not_open_set)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_close_set(self):
        # Arrange
        close_set = ']'
        not_close_set = 'a'
        # Act
        true = is_close_set(close_set)
        false = is_close_set(not_close_set)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_open_alternate(self):
        # Arrange
        open_alternate = '('
        not_open_alternate = 'a'
        # Act
        true = is_open_alternate(open_alternate)
        false = is_open_alternate(not_open_alternate)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_close_alternate(self):
        # Arrange
        close_alternate = ')'
        not_close_alternate = 'a'
        # Act
        true = is_close_alternate(close_alternate)
        false = is_close_alternate(not_close_alternate)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_unit(self):
        # Arrange
        unit = '.'
        not_unit = '*'
        # Act
        true = is_unit(unit)
        false = is_unit(not_unit)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_literal(self):
        # Arrange
        literal = 'a'
        not_literal = '*'
        # Act
        true = is_literal(literal)
        false = is_literal(not_literal)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_dot(self):
        # Arrange
        dot = '.'
        not_dot = 'a'
        # Act
        true = is_dot(dot)
        false = is_dot(not_dot)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_escape_sequence(self):
        # Arrange
        escape_sequence = '\\'
        not_escape_sequence = 'a'
        # Act
        true = is_escape_sequence(escape_sequence)
        false = is_escape_sequence(not_escape_sequence)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_is_set(self):
        # Arrange
        set = '[XYZ]'
        not_set = 'a'
        # Act
        true = is_set(set)
        false = is_set(not_set)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_split_expression(self):
        # Arrange
        expression = 'a*b+c{1,3}'
        # Act
        result = split_expression(expression)
        # Assert
        self.assertEqual(result, ('a', '*', 'b+c{1,3}'))
    
    def test_split_alternate(self):
        # Arrange
        alternate = '(a|b)'
        # Act
        result = split_alternate(alternate)
        # Assert
        self.assertEqual(result, ['a', 'b'])

    # def test_split_count(self):
    #     # Arrange
    #     count = 'b{1,3}'
        
    #     # Act
    #     splited_count = split_count(count, 2, 5)
    #     # Assert
    #     self.assertEqual(splited_count, ['1', '3'])
    
    def test_split_set(self):
        # Arrange
        set = '[XYZ]'
        # Act
        result = split_set(set)
        # Assert
        self.assertEqual(result, ['X', 'Y', 'Z'])
    
    def test_does_unit_match(self):
        # Arrange
        unit = 'a*'
        string = 'aaaa'
        false_unit = 'b*'
        # Act
        true = does_unit_match(unit, string)
        false = does_unit_match(false_unit, string)
        # Assert
        self.assertTrue(true)
        self.assertFalse(false)
    
    def test_match_star(self):
        # Arrange
        star = 'a*'
        string = 'aaaa'
        # Act
        true = match_star(star, string, 0)
        # Assert
        self.assertTrue(true)

    def test_match_plus(self):
        # Arrange
        plus = 'a+'
        string = 'aaaa'
        false_plus = 'b+'
        # Act
        true = match_plus(plus, string, 1)
        false = match_plus(false_plus, string, 1)
        # Assert
        self.assertTrue(true)
        self.assertEqual(false, [False, None])
    
    def test_match_question(self):
        # Arrange
        question = 'a?'
        string = 'aaaa'
        # Act
        true = match_question(question, string, 0)
        # Assert
        self.assertTrue(true)

    def test_match_alternate(self): 
        # Arrange
        alternate = '(a|b)'
        string = 'aaaa'
        false_alternate = '(c|d)'
        # Act
        true = match_alternate(alternate, string, 0)
        false = match_alternate(false_alternate, string, 0)
        # Assert
        self.assertTrue(true)
        self.assertEqual(false, [False, None])
    
    def test_match_multiple(self):
        # Arrange
        multiple = 'a{1,3}'
        string = 'aaaa'
        false_multiple = 'b+'
        # Act
        true = match_multiple(multiple, string, 0, 1, 3)
        false = match_multiple(false_multiple, string, 0, 1, 3)
        # Assert
        self.assertTrue(true, [True, 2])
        self.assertEqual(false, [False, None])
    
    def test_match_count(self):
        # Arrange
        count = 'a{2,}'
        string = 'aaaa'
        false_count = 'b{1,3}}'
        # Act
        true = match_count(count, string, 0)
        false = match_count(false_count, string, 0)
        # Assert
        self.assertTrue(true, [True, 4])
        self.assertEqual(false, [False, None])

    def test_match_expression(self):
        # Arrange
        expression = 'a*b+'
        string = 'aaaab'
        false_expression = 'baa'
        # Act
        true = match_expression(expression, string, 0)
        false = match_expression(false_expression, string, 0)
        # Assert
        self.assertEqual(true, [True, 5])
        self.assertEqual(false, [False, None])
    
    def test_find_match(self):
        # Arrange
        expression = 'a*b+c{1,3}'
        string = 'aaaabccsabc'
        false_expression = 'baa'
        error_expression = 'a{1, b}'
        # Act
        true = find_match(expression, string)
        false = find_match(false_expression, string)
        # Assert
        self.assertEqual(true, ['aaaabcc', 'abc'])
        self.assertEqual(false, [])
        with self.assertRaises(ValueError):
            find_match(error_expression, string)
    
    def test_match(self):
        # Arrange
        expression = 'a*b+c{1,3}'
        string = 'aaaabccsabc'
        false_expression = 'baa'
        error_expression = 'a{1, {(]}'
        # Act
        true = match(expression, string)
        false = match(false_expression, string)
        error = match(error_expression, string)
        # Assert
        self.assertEqual(true, ['aaaabcc', 'abc'])
        self.assertEqual(false, [])
        self.assertEqual(error, ['Invalid expression'])
    
    def test_replace_matches(self):
        # Arrange
        expression = 'a*b+c{1,3}'
        string = 'aaaabccsabc'
        replacement = 'X'
        replaced = 'XsX'
        false_expression = 'baa'
        error_expression = 'a{1, {(]}'
        # Act
        true = replace_matches(expression, string, replacement)
        false = replace_matches(false_expression, string, replacement)
        error = replace_matches(error_expression, string, replacement)
        # Assert
        self.assertEqual(true, replaced)
        self.assertEqual(false, 'aaaabccsabc')
        self.assertEqual(error, 'Invalid expression')

        

if __name__ == '__main__':
    unittest.main()