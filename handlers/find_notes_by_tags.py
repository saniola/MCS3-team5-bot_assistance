from decorators.input_error import input_error
from models.notes import Notes

@input_error
def find_notes_by_tags(args, notes: Notes):
    tags = args
    matching_notes = notes.find_notes_by_tags(tags)

    if matching_notes:
        result = "Matching notes:\n"
        for note in matching_notes:
            result += str(note) + "\n"
        return result
    else:
        return f"No notes found with tags: {', '.join(tags)}."
