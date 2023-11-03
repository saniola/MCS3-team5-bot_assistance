from decorators.input_error import input_error
from models.notes import Notes

@input_error
def sort_by_tag(args, notes: Notes):
    '''Waiting for tag'''
    tag = args[0]
    matching_notes = notes.sort_notes_by_tag(tag)
    if matching_notes:
        print("Notes sorted by tag:")
        for note in matching_notes:
            print(str(note))
