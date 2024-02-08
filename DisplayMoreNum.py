def main():
    numbers = []

    print("Enter numbers (separated by spaces), press Enter to finish:")

    # Continuously prompt user for input until an empty line is entered
    while True:
        user_input = input().strip()

        # If user_input is empty, break out of the loop
        if not user_input:
            break

        # Split the input by spaces and convert each part to integer
        for num_str in user_input.split():
            try:
                num = int(num_str)
                numbers.append(num)
            except ValueError:
                print("Invalid input. Please enter integers only.")

    print("Numbers entered by the user:", numbers)
