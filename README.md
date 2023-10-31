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
**Installation**: To use the Personal Assistant, download and install the application on your system. Detailed installation instructions can be found in the Installation Guide.

**Usage**: Refer to the User Guide for comprehensive instructions on how to use the Personal Assistant efficiently. It covers everything from adding and managing contacts to creating and organizing notes.

**Contributing**: If you'd like to contribute to the project, please check the Contributing Guidelines for details on how to get involved.

**Support**: If you encounter any issues or have questions, refer to the Support section for guidance on getting help.

## Bot Commands

The following commands are supported by the bot:

- help: to get this list
- `hello`: Get a greeting from the bot.
- `add [name] [surname](optional) [parentname](optional) [phone]`: Add a new contact with a name and phone number.
- `change [fullname] [old phone] [new phone]`: Change the phone number for a specified contact.
- `phone [fullname]`: Show the phone number for a specified contact.
- `all`: Show all contacts in the address book.
- `search-contact [>2 letters or >2 numbers]`: Get list of contacts
- `delete-contact [name]`: Delete specific contact from list
- `add-birthday [fullname] [birth date]`: Add a date of birth for a specified contact.
- `show-birthday [fullname]`: Show the date of birth for a specified contact.
- `birthdays [number](optional)`: Show birthdays that will occur in the period of days passed as parameter. By default used 7 days.
- `add-note [name]`: Add new note
- `change-note [name]`: Change text of specific note
- `change-note-name [name]`: Change name of specific note
- `delete-note [name]`: Delete specific note
- `search-note [name or tag]`: Get list of notes
- `sort-note [tag]`:
- `note [name or tag]`:
- `add_tag [note_name] [tag_name]`:
- `close` or `exit`: Close the program.

## Project Completion
This project aims to fulfill the following main requirements:

- Efficient contact and note management
- Effective data storage and retrieval
- User-friendly experience with validation and reminders
- Robust search and sorting capabilities
- Intuitive editing and deletion of records
- For more details on project completion, please refer to the Completion Checklist.

Thank you for choosing the Personal Assistant for Contact Book and Notes. We hope it enhances your organization and productivity.



