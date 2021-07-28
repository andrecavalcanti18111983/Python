import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

### Calculate how many days from now till deadline

print(f"Dear user! Time remaining for your goal: {goal} is {time_till.days} ")

### or use this = print(deadline_date - today_date)


### Convertendo string para formato de data
###print(datetime.datetime.strptime(deadline, "%d,%m.%Y"))
###print(type(datetime.datetime.strptime(deadline, "%d,%m.%Y")))


### Convertendo string para formato de data
###print(datetime.datetime.strptime(deadline, "%d,%m.%Y"))
###print(type(datetime.datetime.strptime(deadline, "%d,%m.%Y")))



