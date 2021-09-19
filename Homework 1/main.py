#Ikechukwu Ibe
#PSID 1492996
#HW1
#Birthday code
print('Current Day\n')
current_month = int(input())
current_day = int(input())
current_year = int(input())
#Birthday
birth_month = int(input())
birth_day = int(input())
birth_year = int(input())
age = int(current_year - birth_year)
if birth_month == current_month and birth_day == current_day:
    print('Happy Birthday! You are', age, 'years old')

else: print('You are', age, 'years old')