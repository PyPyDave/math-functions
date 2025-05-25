import numpy as np

def selection(choice, number):
    if choice == 0:
        print('Exiting the program...')
        exit()
    elif choice == 1:
        return np.sqrt(number)
    elif choice == 2:
        return np.square(number)
    elif choice == 3:
        return np.power(number, 3)  # Cube of a number
    else:
        print('Invalid input')
        return None

def show_menu():
    print("\nThis function prints desired output based on your choice")
    print("Select your choice from below:")
    print("1. To get the Square Root of a number")
    print("2. To get the Square of a number")
    print("3. To get the Cube of a number")  # Added cube option
    print("0. Exit")

while True:
    show_menu()
    try:
        mychoice = int(input("Enter your choice: "))
        if mychoice not in [0, 1, 2, 3]:  # Added 3 to valid choices
            print("Invalid choice. Please choose 0, 1, 2, or 3.")
            continue
        if mychoice == 0:
            selection(0, 0)  # just to call exit()
        mynum = float(input("Enter a number: "))
        result = selection(mychoice, mynum)
        if result is not None:
            print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

