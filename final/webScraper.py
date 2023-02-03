import requests
from bs4 import BeautifulSoup
import json

"""
    Pulls the faculty data of University of Oregon's Catalog of 2014-2015 from the natural sciences departments, 
    creates a dictionary with the keys being the department name, and the values being a list of faculty and imports 
    it into 'Faculty.js' 

    Notes:
        This program only needs to be called if 'Faculty.js' is not populated. 
            The data from University of Oregon's Catalog of 2014-2015 will not change, so 
            once the data is inserted, there is no need to call this program again.
    
    Overview of resources used:
        Writes to 'Faculty.js'
        Requests from the department pages of University of Oregon's Catalog of 2014-2015 (from the WayBack Machine)
        
"""




"""     parseFaculty(URL: str) -> list
The URL parameter should be a URL from the wayback machine of a department from the University of Oregon's Catalog of 2014-2015.
This function returns a list of faculty names for such department. Each faculty name is in the format: lastName, firstName.
If a part of the name has a ".", this is treated as a middle name and is removed.

Note if inputted other URL's than from what is specified as above:
    The scraper pulls from the html of the page and searches from containers of name "facultytextcontainer"
    If no such container exists, this function will return None
"""
def parseFaculty(URL: str) -> list:
    page = requests.get(URL)

    # all faculty
    soup = BeautifulSoup(page.text, "html.parser")
    container = soup.find("div", {"id": "facultytextcontainer"})
    lines = container.findAll("p")

    # just what is under faculty
    # text = page.text.split('Emeriti')
    # soup = BeautifulSoup(text[0], "html.parser")
    # container = soup.find("div", {"id": "facultytextcontainer"})
    # lines = container.findAll("p")

    professors = []

    for line in lines:
        try:
            name, _ = line.text.split(",", 1)
        except:
            # line is not a person's name
            continue
        else:
            # verified such data matches to the appropriate names in gradeData.js
            splitname = name.split(" ")

            #checks if there is a middle name
            cleanname = []
            for n in splitname:
                if ("." in n) or ('"' in n) or ('(' in n):
                    pass
                else:
                    cleanname.append(n)

            # appends name to list in the format: "firstName, lastName"
            professors.append(' '.join(cleanname[1:]) + ", " + cleanname[0])
            continue
    page.close()
    return professors


"""     getFaculty() -> dict
Returns a dictionary where the keys are the natural sciences (i.e. Biology), and the values are a list of faculty.

This function calls parseFaculty, which pulls the faculty data. 

Note: With Beautiful Soup, it is common for too many request be sent to this webpage, leading for the request to not
be fufilled. If it was unsuccessful for a certain department, an error message is printed: "Couldn't pull {department}" 

"""
def getFaculty() -> dict:
    #wayback machine sites for only the natural sciences
    sites = [("BI", "https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/#facultytext"),
             ("CH", "https://web.archive.org/web/20141107201414/http://catalog.uoregon.edu/arts_sciences/chemistry/#facultytext"),
             ("CIS",
              "https://web.archive.org/web/20141107201434/http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/#facultytext"),
             ("Data science", "NA"),
             ("Earth sciences", "NA"),
             ("Multidisciplinary science", "NA"),
             ("HPHY",
              "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/humanphysiology/#facultytext"),
             ("MATH",
              "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/mathematics/#facultytext"),
             ("Neuroscience",
              "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/neuroscience/#facultytext"),
             ("PHYS", "https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/physics/#facultytext"),
             ("PSY", "https://web.archive.org/web/20141101200122/http://catalog.uoregon.edu/arts_sciences/psychology/#facultytext")]
    professors = {}
    #calls the scraper on all of the natural sciences
    for subject, URL in sites:
        if URL == "NA": continue
        try:
            professors[subject] = parseFaculty(URL)
            print("Successfully pulled", subject)
            continue
        except Exception as e:
            # if there is an error with the parseFaculty
            print("Couldn't pull", subject)
            print(e)

    return professors

if __name__ == '__main__':
    # inserts the faculty data (which is pulled from getFaculty()) and writes it to Faculty.js as a json file
    with open('Faculty.js', 'w') as f:
        data = getFaculty()
        json_object = json.dumps(data, indent=4)
        f.write(json_object)
        f.close()
