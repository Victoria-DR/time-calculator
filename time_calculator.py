def add_time(start, duration, day=""):
    days = ["Sunday", "Monday", "Tuesday", \
    "Wednesday", "Thursday", "Friday", "Saturday"]
    days_later = 0

    start_hour = start.split(":")[0]
    start_minute = start.split()[0].split(":")[1]
    am_pm = start.split()[1]

    duration_hour = duration.split(":")[0]
    duration_minute = duration.split(":")[1]

    new_hour = int(start_hour) + int(duration_hour)
    new_minute = int(start_minute) + int(duration_minute)

    if am_pm == "PM":
        new_hour += 12

    if new_minute > 60:
        new_hour += 1
        new_minute -= 60
    
    if new_hour > 24:
        days_later = new_hour // 24
        new_hour %= 24

    if new_hour > 12:
        new_hour -= 12
        new_am_pm = "PM"
    elif new_hour == 0:
        new_hour = 12
        new_am_pm = "AM"
    elif new_hour == 12:
        new_am_pm = "PM"
    else:
        new_am_pm = "AM"

    new_time = f"{new_hour}:{new_minute:002d} {new_am_pm}"

    if day:
        day_num = days.index(day[0].upper() + day[1:].lower())
        day_num += days_later

        if day_num > 6:
            day_num %= 7

        new_time += f", {days[day_num]}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time