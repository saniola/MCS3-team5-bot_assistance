from decorators.input_error import input_error
from models.notes import Notes

@input_error
def delete_note_by_title(args, notes: Notes):
    '''Waiting for title'''
    title = args[0]
    if notes.delete_note_by_title(title):
        print(f"Note '{title}' removed.")
    else:
        print(f"Note '{title}' not found.")
