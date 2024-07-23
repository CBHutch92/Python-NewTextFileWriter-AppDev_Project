# This program is written for Assignment #3 - Basic File Input and Output in Python
# Name of programmer: Casey B. Hutchinson
# Date: 10/19/2023

# Name of functions: write_to_txtfile, read_from_newfile, and main
# Description: This program is designed to create a new txt file labeled new_file in your file location.
# The input for the program will come from the user.



# Creating the write_to_txtfile function that will open up a new txt file
def write_to_txtfile():
    outfile = open('new_file.txt', 'w')          # This opens the file for writing with w mode, and labels it new_file.txt

    # for loop is designed to prompt the user to input 3 lines that will then be written to new_file.txt

    for i in range(3):                           # Using i range(3) establishes 3 lines to be entered by the user
        line = input(f"Enter line {i + 1}: ")    # line variable stores the users input as a string
        outfile.write(line + "\n")               # Outfile writes the string stored in variable "line" to the new txt file and then starts new line until loop breaks

    # Close the file
    outfile.close()


# Creating the read_from_newfile function that will open the new txt file to read, and then print the lines to display them to the user
def read_from_newfile():
    infile = open('new_file.txt', 'r')           # This opens the new file (new_file.txt) for reading using r mode

    newfile_contents = infile.read()             # infile object is to read the contents of the new file and store them in newfile_contents variable
    infile.close()                               # This will close the file before the last step of this function

    print(newfile_contents)                      # Uses newfile_contents variable in order to display the contents written in the new file


# Creating the main function that will call the other 2 functions
def main():
    # Introduction
    print("This program will create, write, and read a new file. \n")

    write_to_txtfile()                           # Calls the function write_to_txtfile

    # This is a status message that will display after input has been received from the user and a file has been created. It also lets user know their input is being displayed
    print("Thank you for your input. The file has been created and you can see your input below!")

    read_from_newfile()                          # Calls the function read_from_newfile


if __name__ == '__main__':
    main()                         