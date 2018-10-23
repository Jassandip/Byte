def age_to_time(age):
    a = age * 12
    b = a * 30
    c = b * 24
    d = c * 60
    return("months: %d , days: %d , hours: %d : , and minutes: %d  " % (a, b, c, d))


def birthday_to_time(birthday):
    import datetime
    year = int(datetime.datetime.now().year) - int(birthday[0:4])
    month = int(datetime.datetime.now().month) - int(birthday[5:7])
    day = int(datetime.datetime.now().day) - int(birthday[8:10])
    x = (year * 12 * 30 * 24 * 60) + (month * 30 * 24 * 60) + (day * 24 * 60)
    y = (year * 12 * 30 * 24 * 60) 
    if x >= y:
        l = year
    else:
        l = year - 1
    return(age_to_time(l))

if __name__ == "__main__":
    age = input("How old are you?")
    print(age_to_time((age)))
    birthday = raw_input("What's your birthday? (YYYY-MM-DD) ")
    print(birthday_to_time(birthday))


