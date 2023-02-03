import json

""" parseGradeData(department: str, number: str, professor: str):
    Pulls from 'gd.js' and returns the data from the parameters. Different inputs lead to different return values
    
    - Parameters
        Department is the letters/department of a class code (i.e. MATH)
        Number is the class number (i.e. 111)
        Professor is the teacher of the class in the format "LastName, First" (i.e. Hornof, Anthony)
    
    - Input
        The innermost dictionary is a dictionary of the format 
        {"TERM_DESC": "", "aprec": "", "bprec": "","cprec": "","crn": "","dprec": "","fprec": "","instructor": {professor}
        
        (i) If a department, number and professor are provided, a list of the innermost dictionaries of all 
            the terms from the provided professor and class name is returned.

        (ii) If a department and number are provided, and professor is set to None, a list of the innermost dictionaries of all 
            the terms from the provided class name is returned.
            
        (iii) If only a department is provided, a dictionary of lists is returned, with the keys being the class name
            and the values being the lists from (ii)
    
        (iv) Returns an error if parameters are not in the format from i-iii listed above.
    
    Note: doesn't check if department, number, or professor is a valid, because the user is only able to pick from
          what is available from the GUI (which is only valid data)

"""
def parseGradeData(department: str, number: str, professor: str):
    f = open('gd.js')
    # reads the gd.js from a json file to a dictionary
    gradeData = json.load(f)

    returnVal = []
    # inputs all department, number, prof (i.e: MATH111 with Smith)
    if department and number and professor:  # return list of dictionaries
        for term in gradeData[department + number]:
            if term["instructor"] == professor:
                returnVal.append(term)

    # inputs specific class, (i.e: MATH111)
    elif department and number:  # returns a dictionary (of lists)
        returnVal = gradeData[department + number]
    # inputs only department (i.e: MATH)
    elif department:  # returns a dictionary (of lists)
        returnVal = {}
        for clas in gradeData:
            if department in clas:
                returnVal[clas] = gradeData[clas]
    # invalid input
    else:
        raise Exception("Must supply a department, department and number, or department and number and professor")

    f.close()
    return returnVal

# returns a dictonary with the keys being the level (i. 100, 200...) and the values being a
# list of class names of that level
""" getClassNumbers(department)
    Returns a dictionary of all the class numbers from a specified department with the keys being the level.
    (i.e. 100, 200...) and the values being a list of all the class names of that level (i.e. 111, 121 ...). Pulls 
    such data from 'gd.js'.
    
    - Parameters
            Department is the letters/department of a class code (i.e. MATH)
            
    Note:
        Does not validate that the department exists, because the user should not be able to input an invalid department
"""
def getClassNumbers(department: str) -> dict:
    f = open('gd.js')
    gradeData = json.load(f)

    class_numbers = {}
    class_numbers[100] = []
    class_numbers[200] = []
    class_numbers[300] = []
    class_numbers[400] = []
    class_numbers[500] = []
    class_numbers[600] = []
    levels = ["1", "2", "3", "4", "5", "6"]

    #parses through gradeData
    for clas in gradeData:
        if department in clas:
            #checks what level the class is
            for l in levels:
                if clas.startswith(department + l):
                    # with the full class name (i.e. MATH111)
                    # class_numbers[int(l + "00")].append(clas)

                    # with only class name (i.e. 111)
                    class_numbers[int(l + "00")].append(clas.strip(department))
                    break

    return class_numbers

""" getFacultyData(department)
    Pulls from 'Faculty.js', and returns a list of faculty names from a given department. If no department is provided
    (set to None), a dictionary is return with the keys being the department name, and the values being the list 
    of faculty names from such department
"""
def getFacultyData(department: str):
    with open('Faculty.js', 'r') as f:
        gradeData = json.load(f)
        f.close()
        if not department:
            return gradeData
        else:
            return gradeData[department]

print(parseGradeData("MATH", "", None))