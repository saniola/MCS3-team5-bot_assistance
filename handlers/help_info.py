from decorators.input_error import input_error
from utils.get_help_commands import get_help_commands

@input_error
def help_info(args):
    if len(args) > 0:
        raise ValueError

    return get_help_commands()
