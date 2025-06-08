def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item(shopping_list):
    item = input("Enter an item you want to add to the list :")
    shopping_list.append(item)

def remove_item(shopping_list):
    item = input("Enter an item you want to remove from the list: ")
    for it in shopping_list:
        if it == item:
            shopping_list.remove(item)
            print(f"{item} Removed successfully")
            return
    print(f"{item} Not found")

def displayItems(shopping_list):
    for item in shopping_list:
        print(item)

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt for and add an item
            add_item(shopping_list)
            pass
        elif choice == 2:
            # Prompt for and remove an item
            remove_item(shopping_list)
            pass
        elif choice == 3:
            # Display the shopping list
            displayItems(shopping_list)
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()