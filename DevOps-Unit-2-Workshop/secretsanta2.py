def get_input_list(prompt):
    print(prompt)
    items = []
    while True:
        item = input("Enter (or just press Enter to finish): ").strip()
        if item == "":
            break
        items.append(item)
    return items

def get_restrictions(participants):
    print("\nEnter pairs that should not be matched, formatted as 'Name1,Name2'.")
    restrictions = []
    while True:
        pair = input("Enter pair (or just press Enter to finish): ").strip()
        if pair == "":
             break
        restrictions.append(pair.split(","))
    return restrictions

participants = get_input_list("Enter the names of participants.")
restrictions = get_restrictions(participants)
print(participants)
print(restrictions)