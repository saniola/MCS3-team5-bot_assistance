from decorators.input_error import input_error
from models.notes import Notes

@input_error
def add_note(args, notes: Notes):
    if len(args) < 2:
        raise ValueError
    title, text, *tags = args
    title = title.title()
    notes.add_note(title, text, tags)
    return f"Note '{title}' added."
