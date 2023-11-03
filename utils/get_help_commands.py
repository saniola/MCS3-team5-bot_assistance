def get_help_commands():
    return '''
    - add-address "[fullname]": Starts the instruction of address adding for specified contact
    - add-birthday "[fullname]" [birth date]: Add a date of birth for a specified contact.
    - add-contact "[name] [surname](optional) [parentname](optional)" [phone]: Add a new contact with a name and phone number.
    - add-email "[fullname]" [email]: Add email for selected user
    - add-note "[note]" [text] [tags](optional): Add new text note with tags
    - add-tag-to-note "[note]" [tag]: Add tag to selected note
    - birthdays [period](default=7 days): Show birthdays that will occur in the period of days passed as parameter. By default used 7 days.
    - delete-address "[fullname]": Delete the contact address
    - delete-note-by-title "[note]": Delete specific note
    - delete-contact "[fullname]": Delete contact
    - delete-tag-from-note "[note]" [tag]: Delete tag from note
    - edit-address "[fullname]": Starts the instruction of address changing for specified contact
    - edit-birthday "[fullname]": Change birthday for specific contact
    - edit-email "[fullname]" [new email]: Change email for specific contact
    - edit-name "[fullname]" "[new fullname]": Change name for specific contact
    - edit-note-text "[note]" "[new text]": Change text for the note
    - edit-note-title "[note]" "[new note name]": Change note name
    - edit-phone "[fullname]" [old phone] [new phone]: Change the phone number for a specified contact.
    - find-notes-by-tags [tags]: Find notes by tags
    - find-notes-by-title "[note]": Find notes by title
    - help: Get this list of commands
    - search [value]: Can search by phone, name, email etc.
    - show-contacts: Show all contacts
    - sort-by-tag [tag]: Sort notes by tag
    - close or exit: Close the program.
'''
