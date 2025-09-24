def get_number():
    """
    Ask the user to enter a number and return it as an integer.
    """
    return int(input("Enter a number: "))


def check_even_odd(number):
    """
    Check if the number is even or odd.
    """
    return "Even" if number % 2 == 0 else "Odd"


def check_positive_negative(number):
    """
    Check if the number is positive, negative, or zero.
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def find_square(number):
    """
    Return the square of the number.
    """
    return number ** 2


def find_cube(number):
    """
    Return the cube of the number.
    """
    return number ** 3


def main():
    """
    Main function to run the program.
    """
    number = get_number()

    even_odd = check_even_odd(number)
    pos_neg = check_positive_negative(number)
    square = find_square(number)
    cube = find_cube(number)

    # Print results
    print(f"\nResults for number {number}:")
    print(f"E/O: {even_odd}")
    print(f"P/N: {pos_neg}")
    print(f"Sqrt: {square}")
    print(f"Cube: {cube}")


if __name__ == "__main__":
    main()
