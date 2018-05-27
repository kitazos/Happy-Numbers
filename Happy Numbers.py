
# User input
num = str(input("Input a positive integer:\n"))


# Declaring global variables
all_numbers = []
x = num

all_numbers.append(num)


h_lines = [line.rstrip('\n') for line in open('HappyN.txt')]
u_lines = [line.rstrip('\n') for line in open('UnhappyN.txt')]


while True:

    # Declaring local variables
    next_number = 0

    # Checks if the original input has already been declared as happy
    if str(x) in h_lines:
        with open('HappyN.txt', "a+") as f:
            for number in all_numbers:
                if str(number) not in h_lines:
                    print(number, file=f)
        print(num, "is happy")

        num = str(input("\nNext number:\n"))
        # Exit location
        if num == "exit":
            break
        else:
            x = num

    # Checks if the original input has already been declared as unhappy
    elif str(x) in u_lines:
        with open('UnhappyN.txt', "a+") as f:
            for number in all_numbers:
                if str(number) not in u_lines:
                    print(number, file=f)
        print(num, "is unhappy")

        num = str(input("\nNext number:\n"))
        # Exit location
        if num.lower() == "exit":
            break
        else:
            x = num

    else:
        # Creates the next number to be tested
        for digit in str(x):
            next_number += int(digit) ** 2
        all_numbers.append(next_number)
        x = next_number
        print(next_number)                                                                                  # Debugging

