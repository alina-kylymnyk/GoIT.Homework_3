from datetime import datetime


def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        delta = current_date - date_obj
        return delta.days
    except ValueError:
        print("Неправильно введена дата. Введіть дату у форматі YYYY-MM-DD.")


get_days_from_today("2023-10-09")
