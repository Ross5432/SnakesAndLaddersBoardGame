
# gamecat_main.py - Main Module
# Responsible for displaying the menu and accepting user choices

from menu import display_menu, option_1, option_2, option_3, option_4, option_5

def get_user_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

def main():
    while True:
        print()
        display_menu()
        print()
        choice = get_user_choice()
        print()

        if choice == 1:
            option_1()
        elif choice == 2:
            option_2()
        elif choice == 3:
            option_3()
        elif choice == 4:
            option_4()
        elif choice == 5:
            option_5()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
