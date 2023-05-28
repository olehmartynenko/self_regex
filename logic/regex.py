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