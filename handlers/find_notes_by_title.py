from decorators.input_error import input_error
from models.notes import Notes

@input_error
def find_notes_by_title(args, notes: Notes):
    if len(args) != 1:
        raise ValueError
    title = args[0]
    title = title.title()
    matching_notes = notes.find_notes_by_title(title)

    if matching_notes:
        result = "Matching notes:\n"
        for note in matching_notes:
            result += str(note) + "\n"
        return result
    else:
        return f"No notes found with title '{title}'."
