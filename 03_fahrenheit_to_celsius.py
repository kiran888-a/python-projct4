def main():
    print("temperature convert fahrenheit to celsius! :)")
    degrees_fahrenheit = float(input("\033[1mEnter tenperature in Fahrenheit :\033[0m"))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0


    print(f"Temperature {degrees_fahrenheit}F = {degrees_celsius}C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()