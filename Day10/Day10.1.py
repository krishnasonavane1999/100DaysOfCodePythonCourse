def is_leap(year):
  """This function takes year as 
  input and returns True if leap
   or False if not leap year"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
def days_in_month(year_value, month_value):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
  if is_leap(year_value) and month_value == 2:
    return month_days[month_value - 1] + 1
  else:
    return month_days[month_value - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












