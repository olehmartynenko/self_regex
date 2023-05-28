def is_start(char):
    return char == '^'

def is_end(char):
    return char == '$'

def is_star(char):
    return char == '*'

def is_plus(char):
    return char == '+'

def is_question(char):
    return char == '?'

def is_operator(char):
    return is_star(char) or is_plus(char) or is_question(char)

def is_dot(char):
    return char == '.'

def is_escape_sequence(term):
    return is_escape(term[0])

def is_escape(char):
    return char == '\\'

def is_open_alternate(char):
    return char == '('

def is_close_alternate(char):
    return char == ')'

def is_open_set(char):
    return char == '['

def is_close_set(char):
    return char == ']'

def is_literal(char):
    return char.isalpha() or char.isdigit() or char in ' :/'

def is_alternate(term):
    return is_open_alternate(term[0]) and is_close_alternate(term[-1])

def is_set(term):
    return is_open_set(term[0]) and is_close_set(term[-1])

def is_unit(term):
    return is_literal(term[0]) or is_dot(term[0]) or is_set(term) or is_escape_sequence(term)

def split_alternate(alternate):
    return alternate[1:-1].split('|')

def split_set(set_head):
    set_inside = set_head[1:-1]
    set_terms = list(set_inside)
    return set_terms

def split_expression(expression):
    head = None
    operator = None
    rest = None
    last_expression_pos = 0

    if is_open_set(expression[0]):
        last_expression_pos = expression.find(']') + 1
        head = expression[:last_expression_pos]
    elif is_open_alternate(expression[0]):
        last_expression_pos = expression.find(')') + 1
        head = expression[:last_expression_pos]
    elif is_escape(expression[0]):
        last_expression_pos += 2
        head = expression[:2]
    else:
        last_expression_pos = 1
        head = expression[0]

    if last_expression_pos < len(expression) and is_operator(expression[last_expression_pos]):
        operator = expression[last_expression_pos]
        last_expression_pos += 1

    rest = expression[last_expression_pos:]

    return head, operator, rest

def does_unit_match(expression, string):
    head, operator, rest = split_expression(expression)

    if len(string) == 0:
        return False
    if is_literal(head):
        return expression[0] == string[0]
    elif is_dot(head):
        return True
    elif is_escape_sequence(head):
        if head == '\\a':              # \a here for alpha (a-z || A-Z)
            return string[0].isalpha()
        elif head == '\\d':
            return string[0].isdigit()
        else:
            return False
    elif is_set(head):
        set_terms = split_set(head)
        return string[0] in set_terms

    return False