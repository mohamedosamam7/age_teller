import datetime

# input('please enter your birtdate using format yyyy/mm/dd: ')
now = datetime.datetime.now()
birtdate_str = '1990/04/03'
birthdate_obj = datetime.datetime.strptime(birtdate_str, "%Y/%m/%d")


def calculate_age_year_months_days(birth_date_obj):
    """
    input: birth_date_obj
    ouput: age by year & months & days
    """
    now = datetime.datetime.now()
    age = now - birthdate_obj
    years = age.days // 365
    months = (age.days % 250) // 30
    days = (age.days % 250) % 30
    return f'your age is : {years} year, {months} month, and {days} days'


def calculate_months_left_for_birthday(month_of_birth_date, month_now):
    """

    """
    # calculating months & days left till brithdate
    months_left = month_of_birth_date - month_now
    if months_left < 0:
        months_left = 12 + months_left
    return f'months left for your birthday: {months_left}'


print(calculate_age_year_months_days(birthdate_obj))
print(calculate_months_left_for_birthday(birthdate_obj.month, now.month))
