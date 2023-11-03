from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

commands = [
    "change", "change-name", "change-email", "close", "exit", \
    "hello", "all", "add-birthday", "add-note", "add","phone", \
    "show-birthday", "birthday", "add-email", "search", "search-email", \
    "note-ls", "edit-note-title", "edit-note-text","add-tag-to-note", \
    "remove-tag-from-note","find-notes-by-title",'find-notes-by-tags', \
    "sort-by-tag", "help", "add-adress", "del-address", "change-address", \
    "save","delete-note", "change-note-name", "change-note"
    ]

def commands_completer():
    custom_style = Style.from_dict({
        'prompt': 'ansiblue',
        'line': 'ansired',
        'output': 'ansiyellow bg:ansiblack',
    })

    completer = WordCompleter(commands)
    session = PromptSession(style = custom_style)

    return session.prompt("Enter a command: ", completer = completer)
