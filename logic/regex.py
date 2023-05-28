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