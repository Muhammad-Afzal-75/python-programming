inventory = []

while True:
    print("\n1. Add item")
    print("2. View items")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Item name: ")
        qty = int(input("Quantity: "))
        inventory.append([name, qty])
        print("Item add ho gaya ✅")

    elif choice == "2":
        if not inventory:
            print("Inventory khali hai ❌")
        else:
            print("\nInventory List:")
            for item in inventory:
                print(item[0], "=", item[1])

    elif choice == "3":
        print("Program band ho gaya 👋")
        break

    else:
        print("Galat choice ❌")
   