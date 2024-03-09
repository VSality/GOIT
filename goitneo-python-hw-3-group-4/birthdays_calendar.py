import datetime


def get_birthdays_per_week(data:list[dict]):
    
    week_list = {}
    date_today = datetime.datetime.today().date()

    for user in data:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=date_today.year)

        if birthday_this_year < date_today:
            birthday_this_year = birthday.replace(year=date_today.year + 1)

        delta_days = (birthday_this_year - date_today).days

        if delta_days < 7:
            week_name = birthday_this_year.strftime("%A")

            if birthday_this_year.weekday() >= 5:
                week_name = 'Monday'

            if week_name not in week_list.keys():
                week_list[week_name] = name
            else:
                week_list[week_name] += ", " + name
        
    for dayweek, names in week_list.items():
        print(f"{dayweek}: {names}")
        

if __name__ == "__main__":
    #test
    get_birthdays_per_week([{"name":"Bill Gates", "birthday": datetime.datetime(1955, 2, 28)}])
      