#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 28th, 2023
# this program is a calculator using different type parameters.
def calculate(sign: str, first_number: float, second_number: float) -> float:
    # Math signs, Addition, Subtraction, Multiplication, and Division.
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        return first_number / second_number
    else:  # Invalid sign response
        raise ValueError("Invalid sign. Valid signs are '+', '-', '*', and '/'.")


# Main function
def main():
    # Try catch statement
    try:  # Prompt user to input the operation and integers.
        sign = input("Enter the sign of the operation (+, -, *, /): ")
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        # Display the results to the user
        result = calculate(sign, first_number, second_number)
        print(f"The result of {first_number} {sign} {second_number} is {result}.")
    except ValueError as e:
        # Invalid input for the string
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
