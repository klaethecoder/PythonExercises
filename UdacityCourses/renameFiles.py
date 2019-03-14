#import both OS and String Module into file
import os, string

#Create a function that will rename the files in the folder.
def renameFiles():
    
    #Set the list of files into a variable
    contents = os.listdir(r"/Users/first/Desktop/prank")
    
    #Put the current directory user is in into a variable.
    path = os.getcwd()

    # Change directory to the where the files are
    os.chdir(r"/Users/first/Desktop/prank")
    
    # Loop through the names of the files in the variable contents
    for name in contents:

        # Rename the files to have the numbers removed from the name
        os.rename(name, name.strip(string.digits))
    
    # Change back to the original directory that the user was in
    os.chdir(path)
    
    #return the revised contents variable 
    return contents

# Print the outcome of all of the above mentioned functions
print(renameFiles())