# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 01:24:32 2022

@author: cruze6
"""
import numpy as np
import json
import cbModelPython as cb

jdata = [json.loads(line) for line in open('profiles.json','r')]

cleanData = []

for user in jdata:
    if(user['role'] != 'Student'):
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

# cbModel requires numpy arrays, have to cast before running.
# test user:
user = np.array(['saotbeaibfoiaubsfia', 'Undergraduate', 'Computer Science', 'Data Structures'])
cleanData = np.asarray(cleanData, dtype=object, order=None);

# Each tutor is listed in this order:
#   [userID, Degree Type, Major Type, List of Courses]

# Each user request should be listed as:
#   [userID, Degree Type, Major Type, Course Requested]

print(cb.cbModel(user,cleanData))