from decorators.input_error import input_error
from models.notes import Notes

@input_error
def sort_by_tag(args, notes: Notes):
    '''Waiting for tag'''
    if len(args) != 1:
        raise ValueError
    tag = args[0]
    matching_notes = notes.sort_notes_by_tag(tag)
    if matching_notes:
        result = ''
        print("Notes sorted by tag:")
        for note in matching_notes:
            result += str(note)+'\n'

        return result.strip('\n')
