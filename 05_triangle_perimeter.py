def main():
    print("calculate  the perimeter of the triangle! :)")
    # Get the lengths of the sides from the user
    side1 = float(input("\033[1mEnter the length of side 1:\033[0m"))
    side2 = float(input("\033[1mEnter the length of side 2:\033[0m"))
    side3 = float(input("\033[1mEnter the length of side 3:\033[0m"))

    
    # Calculate the perimeter of the triangle
    print("The perimeter of the triangle is : " + str(side1 + side2 + side3))



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()