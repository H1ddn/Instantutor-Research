import numpy as np
import json
import cbModelPython as cb

# Function loads the profiles.json into array
def loadTut():
    jdata = [json.loads(line) for line in open('profiles.json','r')]

    cleanData = []

    for user in jdata:
        newUser = []
        newUser.append(user['user']['$oid'])
        newUser.append(user['degree'])
        newUser.append(user['major'][0])
        courses = []
        for expertise in user['expertise']:
            for course in expertise['relatedCourses']:
                courses.append(course)
        newUser.append(courses)
        cleanData.append(newUser)

    cleanData = np.asarray(cleanData, dtype=object, order=None)
    return(cleanData)