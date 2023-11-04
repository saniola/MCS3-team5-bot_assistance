from datetime import datetime
from utils.get_today import get_today


def get_next_week_birthdays(address_book, birthdays_per_week, days):
    today = get_today()
    today_datetime = datetime(today.year, today.month, today.day)
    users = address_book.values()

    birthday_list = "\n"
    for user in users:
        if user.birthday:
            name = user.name.value
            birthday = datetime.strptime(user.birthday.value, '%d.%m.%Y')
            birthday_this_year = birthday.replace(year=today.year)
            delta_days = (birthday_this_year - today_datetime).days

            if delta_days <= int(days):
                if delta_days < 0:
                    if is_leap_year(today.year + 1):
                        delta_days += 366
                    else:
                        delta_days += 365

                birthday_list += f"{user.birthday}: {name} Залишилось до дня народження: {delta_days}\n"

    return birthday_list


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
