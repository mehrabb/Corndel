def get_input_list():
    print("Enter the names of participants.")
    items = []
    while True:
        item = input("Enter name (or just press Enter to finish): ").strip()
        if item == "":
            break
        items.append(item)
    return items
    
participants = get_input_list()

print(participants)
