""" ParseJSFile(file)
    Retrieves the first Javascript object from given "file".

    ????VALIDATES DATA MAYBE

Inspired by: #https://stackoverflow.com/questions/46946227/reading-json-data-from-js-file
"""
def ParseJSFile(file: str):
    # crop out the object
    f = open(file)
    data = f.read()

    # a json object in javascript is in the form... var name = {};
            # want to pull just the {} (and whatever is inside it)
            # (there may be many nested {}, so that is why we are pulling by indices of the = and ;,
                # so we get the outmost object)
    croppedData = data[data.find("=") + 1: data.find(";")]
    f.close()

    # can probably validate the data here
    data = json.loads(croppedData)

    # load the data into the file
    with open('gd.js', 'w') as f:
        json_object = json.dumps(data, indent=4)
        f.write(json_object)
        f.close()

    return croppedData

ParseJSFile('gradedata.js')