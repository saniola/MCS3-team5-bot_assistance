from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

commands = [
    "hello","add-contact", "edit-phone", "show-contacts", "edit-name", "show-phone", "add-birthday"\
    "edit-birthday", "show-birthday", "birthdays", "add-email", "edit-email", "search"\
    "delete-contact", "add-note", "show-notes", "show-tags", "edit-note-title", "edit-note-text",\
    "edit-note-title", "edit-node-text", "add-tag-to-note", "delete-tag-to-note", "find-notes-by-title",\
    "find-notes-by-tags", "sort-by-tag", "delete-note-by-title", "help", "add-address", "delete-address",\
    "edit-address", "save"
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
