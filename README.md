# GoIT Neoversity Tier 1. Python Programming: Foundations and Best Practices

The given team project is the final assignment for a group of developers in Python for GoIT Neoversity as part of the Tier 1 course "Python Programming: Foundations and Best Practices."

## Team of Collaborators
  Oleksandr Kydanov [saniola](https://github.com/saniola)

  Karpenko Nataliia [Netaly79](https://github.com/Netaly79)

  Serhii Dzhulai [Brigant](https://github.com/Brigant)

  Ivan Diabin [guzz](https://github.com/guzzgrey)

***Personal Assistant - Contact Book and Notes Application***

## Overview
The Personal Assistant is a feature-rich console application designed to help users manage their contacts and notes effectively. It allows users to store contact information and textual notes, conduct searches, and set reminders for upcoming birthdays. The application emphasizes data accuracy and user-friendly interactions.

## Main Features
### Contact Management
- Add new contacts with details like names, addresses, phone numbers, email addresses, and birthdates.
- Search for contacts using various criteria (e.g., by name).
- Edit and delete contact entries.
- Display a list of contacts whose birthdays are approaching within a specified number of days.
- Validate phone numbers and email addresses during contact creation and editing, providing feedback to the user on incorrect input.

### Note Management
- Create and manage textual notes.
- Attach "tags" to notes, keywords that describe the note's subject and content.
- Search, edit, and delete notes with ease.
- Sort and filter notes based on associated tags for better organization.

### Data Persistence
- All user data, including contacts and notes, is securely stored on the user's hard drive within their personal folder.
- The application supports data preservation, ensuring that users can restart the assistant without losing any information.

## Getting Started
**Installation**:
- Be sure that you have Python installed on your machine either [download](https://www.python.org/downloads/)
- clone repository on your machine
- install all requirements with command `pip install -r requirements.txt`

**Usage**: Run main.py from application and follow the instructions and use bot commands

**Contributing**: If you'd like to contribute to the project, please check ping one of the devs that starts this project.

**Support**: If you encounter any issues or have questions please reach us.

## Bot Commands

The following commands are supported by the bot:

- `add-address "[fullname]"`: Starts the instruction of address adding for specified contact
- `add-birthday "[fullname]" [birth date]`: Add a date of birth for a specified contact.
- `add-contact "[name] [surname](optional) [parentname](optional)" [phone]`: Add a new contact with a name and phone number.
- `add-email "[fullname]" [email]`: Add email for selected user
- `add-note "[note]" [text] [tags](optional)`: Add new text note with tags
- `add-tag-to-note "[note]" [tag]`: Add tag to selected note
- `birthdays [period](default=7 days)`: Show birthdays that will occur in the period of days passed as parameter. By default used 7 days.
- `delete-address "[fullname]"`: Delete the contact address
- `delete-note-by-title "[note]"`: Delete specific note
- `delete-contact "[fullname]"`: Delete contact
- `delete-tag-from-note "[note]" [tag]`: Delete tag from note
- `edit-address "[fullname]"`: Starts the instruction of address changing for specified contact
- `edit-birthday "[fullname]"`: Change birthday for specific contact
- `edit-email "[fullname]" [new email]`: Change email for specific contact
- `edit-name "[fullname]" "[new fullname]"`: Change name for specific contact
- `edit-note-text "[note]" "[new text]"`: Change text for the note
- `edit-note-title "[note]" "[new note name]"`: Change note name
- `edit-phone "[fullname]" [old phone] [new phone]`: Change the phone number for a specified contact.
- `find-notes-by-tags [tags]`: Find notes by tags
- `find-notes-by-title "[note]"`: Find notes by title
- `help`: Get this list of commands
- `search [value]`: Can search by phone, name, email etc.
- `show-contacts`: Show all contacts
- `show-birthday "[fullname]"`: Show contact birthday
- `show-notes`: Show all notes
- `show-phone "[fullname]"`: Show phone of specific contact
- `show-tags`: Show all tags
- `sort-by-tag [tag]`: Sort notes by tag
- `close` or `exit`: Close the program.

## Project Completion
This project aims to fulfill the following main requirements:

- Efficient contact and note management
- Effective data storage and retrieval
- User-friendly experience with validation and reminders
- Robust search and sorting capabilities
- Intuitive editing and deletion of records
- For more details on project completion, please refer to the team of contributors.

Thank you for choosing the Personal Assistant for Contact Book and Notes. We hope it enhances your organization and productivity.



