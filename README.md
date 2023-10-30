# GoIT Neoversity Tier 1. Python Programming: Foundations and Best Practices

## Homework 3: Address Book with Birthday

This homework is the final part of a series of homework assignments completed by Oleksandr Kydanov in Python for GoIT Neoversity as part of the Tier 1 course "Python Programming: Foundations and Best Practices."

### Task Description

In this assignment, two previous homework assignments, which were completed at [GitHub Repo 1](https://github.com/saniola/goitneo-python-hw-1-group3.git) and [GitHub Repo 2](https://github.com/saniola/goitneo-python-hw-2-group3.git), are combined.

Additional functionality has been added to the existing project:
- **Birthday Field**: A new field for storing the date of birth has been introduced as a class called `Birthday`. This field is optional and can be associated with a contact.
- **Birthday Functionality**: Added a function `add_birthday` in the `Record` class to add a birthday to a contact.
- **Data Validation**: Implemented functionality for verifying the correctness of values for the `Phone` and `Birthday` fields.

A new function `get_birthdays_per_week` has been added to the `AddressBook` class. It returns a list of users whose birthdays will occur in the upcoming week.

### Bot Commands

The following commands are supported by the bot:

- `add [name] [phone]`: Add a new contact with a name and phone number.
- `change [name] [old phone] [new phone]`: Change the phone number for a specified contact.
- `phone [name]`: Show the phone number for a specified contact.
- `all`: Show all contacts in the address book.
- `add-birthday [name] [birth date]`: Add a date of birth for a specified contact.
- `show-birthday [name]`: Show the date of birth for a specified contact.
- `birthdays`: Show birthdays that will occur in the next week.
- `hello`: Get a greeting from the bot.
- `close` or `exit`: Close the program.



