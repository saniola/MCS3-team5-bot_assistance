from collections import UserDict
from datetime import datetime


def get_next_birthdays(address_book, days):
    today_datetime = datetime.today()
    users = address_book.values()
    leap_date = datetime(3000, 3, 1)
    result = UserDict()
    for user in users:
        if user.birthday:
            birthday = datetime.strptime(user.birthday.value, '%d.%m.%Y')
            birthday_this_year = birthday.replace(year=today_datetime.year)
            delta_days = (birthday_this_year - today_datetime).days

            if delta_days < 0:
                if is_leap_year(today_datetime.year + 1) \
                    and birthday.day >= leap_date.day \
                    and birthday.month >=leap_date.month:
                    delta_days += 366
                else:
                    delta_days += 365
            if delta_days <= int(days):
                if result.get(delta_days):
                    result[delta_days] = result[delta_days] + f", \'{user.name.value}\'"
                else:
                    result[delta_days] = f"\'{user.name.value}\'"

    return print_birdays(result)


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def print_birdays(birdayes: UserDict):
    res = ''
    for k, val in sorted(birdayes.data.items()):
        if k == 1:
            res += f"Birthay in {k+1} day: {val}\n"
        else:
            res += f"Birthay in {k+1} days: {val}\n"

    return res.strip('\n')
