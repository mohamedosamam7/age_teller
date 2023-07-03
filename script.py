import datetime

# input('please enter your birtdate using format yyyy/mm/dd: ')
now = datetime.datetime.now()
birtdate_str = '1990/04/15'
birthdate_obj = datetime.datetime.strptime(birtdate_str, "%Y/%m/%d")


def calculate_age_year_months_days(birth_date_obj, now_obj):
    """
    input: birth_date_obj
    ouput: age by year & months & days
    """
    age = now_obj - birthdate_obj
    years = age.days // 365
    months = (age.days % 250) // 30
    days = (age.days % 250) % 30
    return (years, months, days)


def calculate_months_left_for_birthday(month_of_birth_date, month_now):
    """

    """
    # calculating months & days left till brithdate
    months_left = month_of_birth_date - month_now
    if months_left < 0:
        months_left = 12 + months_left
    return months_left


if __name__ == '__main__':
    print(calculate_age_year_months_days(birthdate_obj, now))
    print(calculate_months_left_for_birthday(birthdate_obj.month, now.month))
