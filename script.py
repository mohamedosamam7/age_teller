import datetime
now = datetime.datetime.now()
# input('please enter your birtdate using format yyyy/mm/dd: ')
birtdate_str = '1990/11/03'
birthdate_obj = datetime.datetime.strptime(birtdate_str, "%Y/%m/%d")
age = now - birthdate_obj
years = age.days // 365
months = (age.days % 250) // 30
days = (age.days % 250) % 30
print(f'your age is : {years} year, {months} month, and {days} days')
