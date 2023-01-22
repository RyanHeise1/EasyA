import requests
from bs4 import BeautifulSoup
import json

#parses the wayback URL
def parseFaculty(URL) -> dict:
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, "html.parser")
    lines = soup.findAll("p", class_="facultylist")

    professors = {}

    for line in lines:
        try:
            name, _ = line.text.split(",", 1)
        except:
            continue
        else:
            professors[name] = None
            continue

    page.close()
    return professors

#gets data from wayback machine
def getFaculty():
    sites = [("Biology", "https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/"),
             ("Chemistry and Biochemistry", "https://web.archive.org/web/20141107201414/http://catalog.uoregon.edu/arts_sciences/chemistry/"),
             ("Computer science", "https://web.archive.org/web/20141107201434/http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/"),
             ("Data science", "NA"),
             ("Earth sciences", "NA"),
             ("Multidisciplinary science", "NA"),
             ("Human physiology", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/humanphysiology/"),
             ("Mathematics", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/mathematics/"),
             ("Neuroscience", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/neuroscience/"),
             ("Physics", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/physics/"),
             ("Psychology", "https://web.archive.org/web/20141101200122/http://catalog.uoregon.edu/arts_sciences/psychology/")]
    professors = {}
    for subject, URL in sites:
        if URL == "NA": continue
        try:
            professors[subject] = parseFaculty(URL)
            continue
        except:
            print("Couldn't pull", subject)

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

def appendData(classname: str, newData: dict):
    #dictionary should be of the format {"TERM_DESC":value, "aprec":value, "bprec":value, "cprec":value,
                                #   "crn": value, "dprec":value, "fprec":value, "instructor":value}
    
    #appends data
    with open('gd.js', 'r') as f:
        gradeData = json.loads(f.read())
        #if class exists in gradedata
        if classname in gradeData.keys():
            gradeData[classname].append(newData)
        else:
            gradeData[classname] = [newData]

    #writes the data
    with open('gd.js', 'w') as f:
        json_object = json.dumps(gradeData, indent=4)
        f.write(json_object)



#getFaculty()

#----------------------getting data---------------------------------
print(parseGradeData("MATH", "111", "Arbo, Matthew David"))
#returns a list of dictionaries of MATH111 with Arbo, Matthew David

#print(parseGradeData("MATH", "111", None))
#returns a list of dictionaries of MATH111

#print(parseGradeData("MATH", None, None))
#returns dictionary with the keys being the class name (i.e. MATH111), the values being a list of dictionaries (from each term)

#------------------------appending data-----------------------------
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
