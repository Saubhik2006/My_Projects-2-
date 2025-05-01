from datetime import datetime
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))
current_date = datetime.now()
birth_date = datetime(birth_year, birth_month, birth_day)
age = current_date.year - birth_date.year
if(current_date.month,current_date.day) < (birth_month,birth_day):
    age -= 1
    next_birthday = datetime(current_date.year, birth_month, birth_day)
else:
    next_birthday = datetime(current_date.year + 1, birth_month, birth_day)
days_until_birthday = (next_birthday - current_date).days
print(f"You are {age} years old.")
print(f"There are {days_until_birthday} days remaining until your next birthday.")