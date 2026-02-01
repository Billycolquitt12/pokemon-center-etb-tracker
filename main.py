from items_dao import get_all_items, add_item, delete_item

while True:
    print("\nPokemon Center ETB Tracker")
    print("1. View ETBs")
    print("2. Add ETB")
    print("3. Delete ETB")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        for item in get_all_items():
            print(item)

    elif choice == "2":
        name = input("ETB name: ")
        add_item(1, 1, name)
        print("ETB added.")

    elif choice == "3":
        iid = input("ETB ID to delete: ")
        delete_item(iid)
        print("ETB deleted.")

    elif choice == "4":
        break
