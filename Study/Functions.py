calculation_to_units = 24
name_of_unit = "hours"


def days_to_unit(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"



def validade_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
                calculate_value = days_to_unit(user_input_number)
                print(calculate_value)
        elif user_input_number == 0:
                print ("You entered 0, please enter a valid positive number")
    except ValueError:
        print("Your input is not a number, don't ruin my program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter the number of days and I will convert days in hours!\n")
    validade_and_execute()