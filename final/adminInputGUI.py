import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os
import csv
import shutil
import json

""" ParseJSFile(filepath: str):
    Takes in the file, 'filepath' and constructs it into a .js file that we can then pull data from

    - Parameters
        filepath is the name of the file that the user has uploaded (i.e. /Users/Lauren/Desktop/gradedata.js)
    
    - Input
        We are stripping the leading 'var groups = ' and trailing code IF it is there. If not
        we simply return and move on to the next step of validating the contents of the file
"""
def ParseJSFile(filepath):
    try:
        # Try to strip file of leading and trailing info
        f = open(filepath)
        data = f.read()
        # Extract only the JSON data from the file by slicing
        # The data string from the character after the "="
        # To the character before the ";"
        croppedData = data[data.find("=") + 1: data.find(";")]
        f.close()
        # Update data contents
        data = json.loads(croppedData)
        with open(filepath, 'w') as f:
            # Write data to file using indent=4 for readability
            json.dump(data, f, indent=4)
    # If we don't find the extra lines in the .js file
    # Return and move on to next file Validation step
    except:
        return


""" check_header(filenmae: str):
    Takes in the file, 'filename' and checks the headers are the expected headers

    - Parameters
        filename is the name of the file that the user has uploaded (i.e. /Users/Lauren/Desktop/gradedata.js)

    - Input
        We are checking to see if the headers match what the system is expecting
        it steps through each class for each term and checks the header description
    - Note
        The function will return an error if:
            the headers are not what are expected
            contents of file are not valid .js data 
"""
def check_headers(filename):
    # Define the expected headers for the data file
    expected_headers = ['TERM_DESC', 'aprec', 'bprec', 'cprec', 'crn', 'dprec', 'fprec', 'instructor']
    try:
        # Open the file
        with open(filename) as f:
            # Read the contents of the file and parse it as a JSON object
            data = json.loads(f.read())

            # iterate through each class in the data
            for clas in data:
                # iterate through each term in the class
                for term in data[clas]:
                    # retrieve the headers of the current term
                    headers = list(term.keys())
                    # compare the headers with the expected headers
                    if headers != expected_headers:
                        # show an error message if the headers don't match
                        messagebox.showerror("Incorrect Headers", "Incorrect Headers\nExpected headers:\n{}".format(expected_headers))
                        # return False if the headers don't match
                        return False
        # return True if all headers match the expected headers
        return True
    except:
        # if the file doesn't contain valid JSON data, print an error message
        print("Error: The file does not contain valid JSON data.")


""" no_middle_init(filename: str):
    Takes in the file, 'filename' and removes the middle initial/name from the Instructor
    if it exists

    - Parameters
        filepath is the name of the file that the user has uploaded (i.e. /Users/Lauren/Desktop/gradedata.js)

    - Input
        We are stepping through each class for each term and removing the middle
        initial or middle name if it exists and updating the file
    - Note
        We are doing this to ensure that the name conventions between the wayback
        machine and the new .js data matches and we can pull data properly
"""
def no_middle_init(filename):
    with open(filename) as f:
        data = json.loads(f.read())

        # loop through each class in the data
        for clas in data:
            # loop through each term in the class
            for term in data[clas]:
                instructor = term["instructor"]

                # if the instructor name is empty, continue to the next term
                if (instructor == ""):
                    continue
                else:
                    # split the instructor name into last name and first name
                    lname, first_name = instructor.split(', ')
                    # split the first name into first name and middle name if it exists
                    if len(first_name.split(" ")) >= 2:
                        fname, *middle = first_name.split(" ")
                        # if the first name is abbreviated (ie. J. Craig Appleseed),
                        # use the middle name as the first name instead
                        if "." in fname:
                            fname = middle[0]
                        # update the instructor name in the term
                        # with the format lastname, firstname
                        term["instructor"] = "{}, {}".format(lname, fname)

    # write the updated data back to the file
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

""" uploade_file():
    takes in no parameters but generates Admin GUI instructing user
    to upload a file of .js filetype. It then validates filetype, and expected headers, 
    strips extra code, and removes middle initial of instructors to prep file for
    use by graphing functions
    
    - Note
        The file will return an error if:
            file extension is not of .js
            the headers are not what are expected
            contents of file are not valid .js data
            no file is selected
"""
def upload_file():
    # Get the file path selected by the user using the filedialog module
    filepath = filedialog.askopenfilename()
    # Split the file path into the filename and file extension
    filename, file_extension = os.path.splitext(filepath)

    # Check if the file extension is not .js
    if file_extension != '.js':
        # Show an error message if the file extension is not .js
        messagebox.showerror("Invalid file type", "Please select a .js or .csv file.")
        return

    # Call the ParseJSFile function with the selected file path as the argument
    ParseJSFile(filepath)

    # Check if the headers of the file are incorrect
    if(check_headers(filepath) == False):
        return
    # Call the no_middle_init function to remove middle initials from instructor names
    no_middle_init(filepath)
    # Remove the file named 'gd.js'
    os.remove("gd.js")
    # Move the file to the current working directory and rename it to 'gd.js'
    shutil.move(filepath, "gd.js")
    # Print a message indicating that the file has been uploaded and added to the directory
    print('File uploaded and added to directory.')

'''
The following lines of code set up Graphical User Interface for uploading new data
'''
root = tk.Tk()

# Label 'instructions' that displays the text "Select a .js or .csv file to upload:"
instructions = tk.Label(root, text='Select a .js file to upload:')
instructions.pack()

# label 'note' that displays a note about the expected headers of the file to be uploaded.
note = tk.Label(root, text='Note: The headers must be as follows, \n'
                           'TERM_DESC (term year), aprec, bprec, cprec, crn, '
                           'dprec, fprec, instructor (lname, fname)')
note.pack()

# button 'upload_button' that, when clicked, will trigger the upload_file() function
upload_button = tk.Button(root, text='Upload File', command=upload_file, padx=20, pady=10)
upload_button.pack()

# 'root.mainloop()' starts the event loop that will run the GUI until the user closes it.
root.mainloop()