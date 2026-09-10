print("SMART AUDITOR PROGRAM!!!!")

STOCK_LIMIT = 500
failed_entry_count = 0
inventory = 0

def is_positive(num):
    return int(num) > 0

def is_digit(num):
    return num.isdigit()

def is_over_stock_limit(num):
    return int(num) > STOCK_LIMIT

def iterate_checks(list_of_checks, num):
    for check in list_of_checks:
        if not check(num):
            return False
    return True

def print_status(units_processed, failed_entry_count):
    print("Total units processed:", units_processed)
    print("Number of failed/rejected entries:", failed_entry_count)

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
        failed_entry_count += 1
        continue

    if is_over_stock_limit(inventory+int(command)):
        print("ALERT: ENTRY EXCEEDS STOCK INVENTORY\nEXITING...")
        break
        
    inventory += int(command)
    print(inventory)

print(inventory)
print_status(inventory, failed_entry_count)
    
