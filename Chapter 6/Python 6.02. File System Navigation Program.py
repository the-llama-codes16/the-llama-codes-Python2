"""
Python Exercise 6.02
Written by: Iam Rasendi M. Saldua
Date: March 18, 2023

Gathering Information from a File System

In this case study, we develop a simple terminal-based file system navigator
that provides some information about the system. In the process, we will have
an opportunity to exercise some skills in top-down design and recursive design.

The program we will design in this case study provides some basic browsing capability
as well as options that allow you to search for a given filename and find statistics
on the number of files and their size in a directory. At program startup,
the current working directory (CWD) is the directory containing the Python program file.
The program should display the path of the CWD, a menu of command options, and a prompt
for a command.

When the user enters a command number, the program runs the command,
which may display further information, and the program displays the CWD and
command menu again. An unrecognized command produces an error message,
and command number 7 quits the program.

The command menu of the filesys program
/Users/KenLaptop/Book/Chapter6
1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program
Enter a number:

"""

import os
import os.path

MENU = """1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program"""

# Define all functions
def listCWD():
    """1. List the current directory
    Prints the names of the files and directories in the current working directory (CWD)."""
    print("Files and directories inside the current working directory:")
    contents = os.listdir(os.getcwd())
    for content in contents:
        print(content)

def moveUp():
    """2 Move up
    If the CWD is not the root, move to the parent directory and make it the CWD."""

    # Check if the CWD is a root
    if os.path.dirname(os.getcwd()) == os.getcwd():
        print("Current working directory is the root.\n")
    else:
        os.chdir(os.path.dirname(os.getcwd()))

def moveDown():
    """3 Move down
    Prompts the user for a directory name. If the name is not in the CWD, print an error message; otherwise,
    move to this directory and make it the CWD."""
    target = input("Enter directory name: ")
    new_path = os.path.join(os.getcwd(), target)

    # Check if the target exists, check if it is a directory
    if (os.path.exists(new_path)) and (os.path.isdir(new_path)):
        os.chdir(new_path)
    else:
        print("The directory %s does not exist.\n" % target)

def numFiles():
    """4 Number of files in the directory
    Prints the number of files in the CWD and all of its subdirectories."""
    
    # Count the contents of the CWD
    print("Total number of files and subdirectories: %d\n" % len(os.listdir(os.getcwd())))

def sizeCWD():
    """5 Size of the directory in bytes
    Prints the total number of bytes used by the files in the CWD and all of its subdirectories."""

    cwd = os.getcwd()
    
    # Define the recursive function for getting file/folder size
    def getSize(path):
        if os.path.isfile(path):
            return os.path.getsize(path)
        else:
            folder_contents = os.listdir(path)
            total_size = 0
            for content in folder_contents:
                new_path = os.path.join(path, content)
                total_size = total_size + getSize(new_path)
            return total_size

    print("Size of the current working directory: %d bytes\n" % getSize(cwd))

def searchFileName():
    """6 Search for a filename
    Prompts the user for a search string. Prints a list of all the filenames (with their paths) that contain the
    search string, or “String not found.”"""

    search_keyword = input("Enter search string: ").lower()
    cwd = os.getcwd()
    matches = dict()

    # Define the recursive function to search for matching files/folders
    def searchMatches(search_key: str, path):
        if os.path.isfile(path):
            file_name = os.path.basename(path)
            if search_key in file_name.lower():
                matches[file_name] = path
                return matches
        else:
            contents = os.listdir(path)
            for content in contents:
                new_path = os.path.join(path, content)
                searchMatches(search_key, new_path)
            return matches

    search_results = searchMatches(search_keyword, cwd)
    if len(matches) < 1:
        print("String not found.")
    else:
        print("Search results:")
        for result in search_results:
            print(result, "\nPATH:", search_results[result], "\n")

# Prepare the jumpTable and the runCommand

jumpTable = {1: listCWD, 2: moveUp, 3: moveDown, 4: numFiles, 5: sizeCWD, 6: searchFileName}

def runCommand(command):
    jumpTable[command]()
    

# Define the main function
def main():
    while True:
        print("\n" + os.getcwd())
        print(MENU)
        # Use try-except in case user enters invalid input
        try:
            command = int(input("Enter a number: "))
            if (command == 7):
                break
            runCommand(command)
        except:
            # Default command is to quit the program
            break
    print("Thank you for using our file management system!\n")

# Entry point for the main function
if __name__ == "__main__":
    main()



















