""" Sum Until User Enters 0 """
total = 0

while True:
    try:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            print("Stopped")
            break
        print("You entered:", num)
    except KeyboardInterrupt:
        print("\nYou stopped the program!")
        break
    except ValueError:
        print("Please enter a valid number")