from shlex import shlex


def parse_input(user_input) -> tuple[str, list(str)]:
    """
    The function parses user input and returns 'command' value
    and all 'arguments'
    """
    lexer = shlex(user_input, posix=True)
    lexer.quotes = '"'
    lexer.whitespace_split = True
    cmd, *args = list(lexer)

    return cmd, args
