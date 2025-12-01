total = 0

while True:
    userInput = input("Enter the price (press x to quit): ")

    if userInput.lower() != 'x':    # handles X or x
        try:
            total += int(userInput) 
            print(f"Order total so far: {total}")
        except ValueError:
            print("Please enter a valid number!")
    else:
        print(f"Your final bill is {total}. Thanks for shopping with us!")
        break

