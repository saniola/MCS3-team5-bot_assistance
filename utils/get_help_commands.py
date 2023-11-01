def get_help_commands():
    return '''
    - help: to get this list
    - hello: Get a greeting from the bot.
    - add [name] [surname](optional) [parentname](optional) [phone]: Add a new contact with a name and phone number.
    - change [fullname] [old phone] [new phone]: Change the phone number for a specified contact.
    - phone [fullname]: Show the phone number for a specified contact.
    - all: Show all contacts in the address book.
    - search-contact [>2 letters or >2 numbers]: Get list of contacts
    - delete-contact [name]: Delete specific contact from list
    - add-birthday [fullname] [birth date]: Add a date of birth for a specified contact.
    - show-birthday [fullname]: Show the date of birth for a specified contact.
    - birthdays [number](optional): Show birthdays that will occur in the period of days passed as parameter. By default used 7 days.
    - add-note [name]: Add new note
    - change-note [name]: Change text of specific note
    - change-note-name [name]: Change name of specific note
    - delete-note [name]: Delete specific note
    - search-note [name or tag]: Get list of notes
    - sort-note [tag]:
    - note [name] or [tag]:
    - add_tag [note_name] [tag_name]:
    - close or exit: Close the program.
'''
