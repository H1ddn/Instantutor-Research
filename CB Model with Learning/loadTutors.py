# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 01:24:32 2022

@author: cruze6
"""
import numpy as np
import cbModelPython as cb
from pymongo import MongoClient

# Function loads the profiles.json and returns only the tutors as a numpy array.
def loadTut():
    # connect to MongoDB
    client = MongoClient("mongodb+srv://Adm:instutor@cluster0.s0gxd.mongodb.net/?retryWrites=true&w=majority")

    # enter the deployment's database
    db = client['deployment']

    # get profiles
    cursor = list(db['profiles'].find())

    cleanData = []

    for line in cursor:
        if(line['role'] != 'Student'):
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

    # cbModel requires numpy arrays, have to cast before running.
    # test user:
    #user = np.array(['saotbeaibfoiaubsfia', 'Undergraduate', 'Computer Science', 'Data Structures'])
    cleanData = np.asarray(cleanData, dtype=object, order=None);

    # Each tutor is listed in this order:
    #   [userID, Degree Type, Major Type, List of Courses]

    # Each user request should be listed as:
    #   [userID, Degree Type, Major Type, Course Requested]

    return(cleanData)