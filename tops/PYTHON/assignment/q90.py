# Write python program that user to enter only odd numbers, else will raise an exception

try:
    num = int(input("Enter an odd number: "))

    if num % 2 == 0:
        raise ValueError()

    print("You entered an odd number")

except ValueError:
    print("Enter only an odd number!")
