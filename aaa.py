def print_menu():
    print("Taco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $3.00")
    print("3. Nachos - $3.50")
    print("4. Soft Drink - $1.50")
    print("5. Quit")
def get_price(selection):
    prices = [2.50, 3.00, 3.50, 1.50]
    return prices[selection - 1]
def main():
    print("Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection.")
    total = 0
    ordered_items = []
    while True:
        print_menu()
        user_input = int(input("User entered: "))

        if user_input == 5:
            break
        elif user_input in [1, 2, 3, 4]:
            food_items = ["Taco", "Burrito", "Nachos", "Soft Drink"]
            selected_item = food_items[user_input - 1]
            print(f"You have selected a {selected_item}.")
            total += get_price(user_input)
            ordered_items.append(selected_item)
        else:
            print("Invalid selection. Please choose a number from the menu.")
    # Print the order summary
    ordered_items_str = ", ".join(ordered_items)
    print(f"You ordered: {ordered_items_str}. Your total is ${total:.2f}")


if __name__ == "__main__":
    main()