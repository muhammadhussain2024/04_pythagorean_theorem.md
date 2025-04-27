import math

def main():
    # Ask the user for the lengths of AB and AC
    AB = float(input("Enter the length of AB: "))
    AC = float(input("Enter the length of AC: "))

    # Use the Pythagorean theorem to calculate BC
    BC = math.sqrt(AB**2 + AC**2)

    # Print the result
    print("The length of BC (the hypotenuse) is:", BC)

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
