print("SMART AUDITOR PROGRAM!!!!")

inventory = []

def is_positive(num):
    return int(num) > 0

def is_digit(num):
    return num.isdigit()

def iterate_checks(list_of_checks, num):
    for check in list_of_checks:
        if not check(num):
            return False
    return True

while True:
    command = input("Enter stock quantity or enter 'quit': \n")

    if command == "quit":
        break
    
    list_of_checks = [
            is_digit,
            is_positive
        ]

    if not iterate_checks(list_of_checks, command):
        print("ERROR!!! CHECK YOUR STOCK QUANTITY AGAIN!!")
        continue

    inventory.append(command)

    print(inventory)
