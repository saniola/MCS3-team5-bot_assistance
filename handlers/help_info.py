from decorators.input_error import input_error
from utils.get_help_commands import get_help_commands

@input_error
def help_info():
    return get_help_commands()
