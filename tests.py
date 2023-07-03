import datetime
from script import calculate_age_year_months_days, calculate_months_left_for_birthday

compare_date_obj = datetime.datetime.strptime('2023/07/03', "%Y/%m/%d")

date_birht1 = datetime.datetime.strptime('2000/09/23', "%Y/%m/%d")
date_birht2 = datetime.datetime.strptime('1997/11/15', "%Y/%m/%d")
date_birht3 = datetime.datetime.strptime('1990/04/15', "%Y/%m/%d")

assert (22, 2, 8) == calculate_age_year_months_days(
    date_birht1, compare_date_obj)

assert (25, 3, 21) == calculate_age_year_months_days(
    date_birht2, compare_date_obj)

assert (33, 4, 12) == calculate_age_year_months_days(
    date_birht3, compare_date_obj)
