# import readline
# from prompt_toolkit import PromptSession
# from prompt_toolkit.completion import WordCompleter

from prompt_toolkit import PromptSession
from prompt_toolkit.completion  import WordCompleter


# import platform
# print(platform.system())


# COMMANDS = ['extra', 'extension', 'stuff', 'errors',
#             'email', 'foobar', 'foo']

# def complete(text, state):
#     for cmd in COMMANDS:
#         if cmd.startswith(text):
#             if not state:
#                 return cmd
#             else:
#                 state -= 1

# readline.parse_and_bind("tab: complete")
# readline.set_completer(complete)
# input('Enter section name: ')\




word_list = ['apple', 'ananas', 'cherry', 'date', 'elderberry', 'fig', 'grape']
completer = WordCompleter(word_list)
session = PromptSession()
while True:
    user_input = session.prompt('Введіть команду: ', completer=completer)
    print(f'Ви ввели: {user_input}')
