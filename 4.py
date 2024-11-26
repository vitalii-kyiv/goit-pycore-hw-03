from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Michael Johnson", "birthday": "1978.03.12"},
    {"name": "Emily Brown", "birthday": "1992.08.05"},
    {"name": "Chris Taylor", "birthday": "1983.12.15"},
    {"name": "Laura Lee", "birthday": "1989.07.22"},
    {"name": "Daniel Walker", "birthday": "1975.06.30"},
    {"name": "Sophia Harris", "birthday": "1995.10.09"},
    {"name": "James Lewis", "birthday": "1988.04.18"},
    {"name": "Olivia Clark", "birthday": "1993.09.25"},
    {"name": "Peter Adams", "birthday": "1980.11.19"},
    {"name": "Anna Wilson", "birthday": "1991.02.13"},
    {"name": "David Moore", "birthday": "1984.05.17"},
    {"name": "Sarah Davis", "birthday": "1994.10.25"},
    {"name": "William Martin", "birthday": "1979.03.08"},
    {"name": "Isabella White", "birthday": "1996.01.14"},
    {"name": "Alexander Scott", "birthday": "1986.09.02"},
    {"name": "Victoria Hall", "birthday": "1987.11.26"},
    {"name": "Henry Young", "birthday": "1977.11.30"},
    {"name": "Elizabeth King", "birthday": "1998.10.01"}
]

def get_upcoming_birthdays(users):

  today_date = datetime.today().date() 
  birthday_period_end = today_date + timedelta(days=7)
  upcoming_birthdays =[]
  
  for user in users:
    try:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    except KeyError:
        raise ValueError("В Users відсутні необхідні дані про день народження")
    user_birthday_this_year = birthday.replace(year=today_date.year)
    if  user_birthday_this_year < today_date:
        user_birthday_this_year = user_birthday_this_year.replace(year=today_date.year + 1)
    if today_date <= user_birthday_this_year <= birthday_period_end:
         if user_birthday_this_year.weekday() in [5, 6]:  
                days_to_monday = 7 - user_birthday_this_year.weekday()
                user_birthday_this_year += timedelta(days=days_to_monday)
         upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": user_birthday_this_year.strftime("%Y.%m.%d")
            })
  if not upcoming_birthdays:
        print("В найближчі 7 днів немає дат для привітання")
        return []
    
  print("Список привітань на цьому тижні:", upcoming_birthdays)
  return upcoming_birthdays

get_upcoming_birthdays(users)
    