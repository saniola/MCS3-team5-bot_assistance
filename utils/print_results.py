from datetime import timedelta
from utils.get_today import get_today

def print_results(birthdays_per_week):
    if len(birthdays_per_week):
        today = get_today()
        current_weekday = today.weekday()

        for _ in range(7):
            day = (current_weekday % 7)
            day_name = today.strftime("%A")

            if day_name in birthdays_per_week:
                names = birthdays_per_week[day_name]
                return f"{day_name}: {', '.join(names)}"

            today += timedelta(days=1)
            current_weekday += 1
    else:
        raise KeyError
