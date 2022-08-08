import numpy as np
import cbModelPython as cb
from pymongo import MongoClient

# Function loads the profiles.json into array
def loadProf():
    # connect to MongoDB
    client = MongoClient("mongodb+srv://Adm:instutor@cluster0.s0gxd.mongodb.net/?retryWrites=true&w=majority")

    # enter the deployment's database
    db = client['deployment']

    # get profiles
    cursor = list(db['profiles'].find())

    cleanData = []

    for line in cursor:
        newUser = []
        newUser.append(line['user']['$oid'])
        newUser.append(line['degree'])
        newUser.append(line['major'][0])
        courses = []
        for expertise in line['expertise']:
            for course in expertise['relatedCourses']:
                courses.append(course)
        newUser.append(courses)
        cleanData.append(newUser)

    cleanData = np.asarray(cleanData, dtype=object, order=None)
    return(cleanData)