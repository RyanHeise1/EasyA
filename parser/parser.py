import requests
from bs4 import BeautifulSoup
import json

#parses the wayback URL
def parseFaculty(URL) -> dict:
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, "html.parser")
    lines = soup.findAll("p", class_="facultylist")

    professors = []

    for line in lines:
        try:
            name, _ = line.text.split(",", 1)
        except:
            continue
        else:
            professors.append(name)
            continue

    page.close()
    return professors

#gets data from wayback machine
def getFaculty():
    sites = [("BI", "https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/"),
             ("CH", "https://web.archive.org/web/20141107201414/http://catalog.uoregon.edu/arts_sciences/chemistry/"),
             ("CIS", "https://web.archive.org/web/20141107201434/http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/"),
             ("Data science", "NA"),
             ("Earth sciences", "NA"),
             ("Multidisciplinary science", "NA"),
             ("HPHY", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/humanphysiology/"),
             ("MATH", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/mathematics/"),
             ("Neuroscience", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/neuroscience/"),
             ("PHYS", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/physics/"),
             ("PSY", "https://web.archive.org/web/20141101200122/http://catalog.uoregon.edu/arts_sciences/psychology/")]
    professors = {}
    for subject, URL in sites:
        if URL == "NA": continue
        try:
            professors[subject] = parseFaculty(URL)
            continue
        except:
            print("Couldn't pull", subject)

    return professors

# gets data from gd.js
def parseGradeData(department: str, number: str, professor: str):
    f = open('gd.js')
    gradeData = json.loads(f.read())

    returnVal = []

    #inputs all department, number, prof (i.e: MATH111 with Smith)
    if department and number and professor:
        for term in gradeData[department + number]:
            if term["instructor"] == professor:
               returnVal.append(term)

    #inputs specfic class, (i.e: MATH111)
    elif department and number:
        returnVal = gradeData[department + number]
    #inputs only department (i.e: MATH)
    elif department:
        returnVal = {}
        for clas in gradeData:
            if department in clas:
                returnVal[clas] = gradeData[clas]

    f.close()
    return returnVal

# def getDepartmentNames():
#     return ["BI", "CH", "CIS", "HPHY", "MATH", ]

def getClassNumbers(department: str):
    f = open('gd.js')
    gradeData = json.loads(f.read())

    class_numbers = {}
    class_numbers[100] = []
    class_numbers[200] = []
    class_numbers[300] = []
    class_numbers[400] = []
    class_numbers[500] = []
    class_numbers[600] = []

    for clas in gradeData:
        if department in clas:
            if clas.startswith(department + "1"):
                class_numbers[100].append(clas)
            elif clas.startswith(department + "2"):
                class_numbers[200].append(clas)
            elif clas.startswith(department + "3"):
                class_numbers[300].append(clas)
            elif clas.startswith(department + "4"):
                class_numbers[400].append(clas)
            elif clas.startswith(department + "5"):
                class_numbers[500].append(clas)
            elif clas.startswith(department + "6"):
                class_numbers[600].append(clas)
    return class_numbers


def appendData(classname: str, newData: dict):
    #dictionary should be of the format {"TERM_DESC":"", "aprec":"", "bprec":"", "cprec":"",
                                #   "crn":"", "dprec":"", "fprec":"", "instructor":""}

    with open('gd.js', 'r') as f:
        gradeData = json.loads(f.read())
        #if class exists in gradedata
        if classname in gradeData.keys():
            gradeData[classname].append(newData)
        else:
            gradeData[classname] = [newData]

    with open('gd.js', 'w') as f:
        json_object = json.dumps(gradeData, indent=4)
        f.write(json_object)



#print(getFaculty())
print(getClassNumbers("MATH"))


#print(parseGradeData("MATH", "111", "Arbo, Matthew David"))


#returns a list of dictionaries of MATH111 with Arbo, Matthew David

#print(parseGradeData("MATH", "111", None))
#returns a list of dictionaries of MATH111

#print(parseGradeData("MATH", None, None))
#returns dictionary with the keys being the class name (i.e. MATH111), the values being a list of dictionaries (from each term)


# print(parseGradeData("AA", "508", None))
# appendData("AA508", {
#             "TERM_DESC": "Fall 2022",
#             "aprec": "20.0",
#             "bprec": "28.0",
#             "cprec": "32.0",
#             "crn": "0000",
#             "dprec": "4.0",
#             "fprec": "16.0",
#             "instructor": "Fake, Data"
#         })
# print(parseGradeData("AA", "508", None))
