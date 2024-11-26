from datetime import datetime

def get_days_from_today(date: str)  -> int:
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")
    except:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
    now = datetime.today()
    days_difference = (now - formatted_date).days
    return days_difference



print(get_days_from_today("2026-03-22"))
