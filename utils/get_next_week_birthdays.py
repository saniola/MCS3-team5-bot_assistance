from datetime import datetime, timedelta
from utils.get_today import get_today

def get_next_week_birthdays(address_book, birthdays_per_week):
    today = get_today()
    today_datetime = datetime(today.year, today.month, today.day)
    users = address_book.values()

    for user in users:
        if user.birthday:
            name = user.name.value
            birthday = datetime.strptime(user.birthday.value, '%d.%m.%Y')
            birthday_this_year = birthday.replace(year=today.year)
            delta_days = (birthday_this_year - today_datetime).days

            if 0 <= delta_days <= 6:
                if birthday_this_year.weekday() == 5:
                    delta_days += 2
                elif birthday_this_year.weekday() == 6:
                    delta_days += 1

                birthday_weekday = (today_datetime + timedelta(days=delta_days)).strftime("%A")
                birthdays_per_week[birthday_weekday].append(name)
