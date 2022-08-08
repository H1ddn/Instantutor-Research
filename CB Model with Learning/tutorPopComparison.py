# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:14:38 2022

@author: cruze6
"""

from pymongo import MongoClient

# Grabs all made requests and returns a dictionary including all requests in form
# [state, tutor id, student id]
# state refers to if the student selected the tutor or not. 'Requested' if true, 'Denied' if false.
def getReqs():

    # connect to MongoDB
    client = MongoClient("mongodb+srv://Adm:instutor@cluster0.s0gxd.mongodb.net/?retryWrites=true&w=majority")

    # enter the deployment's database
    db = client['deployment']

    # get users
    cursor = list(db['users'].find())

    # The system currently works through a name / id basis
    # requests are related to names and ids. For the student
    # calling the request, the id is the same on both ends
    # but for tutors, the id is different. In order to correlate
    # a tutor to their profile, we need to take note of their name
    # then look for their user id in the users.json
    # this is something being fixed in the future
    users = {}
    for line in cursor:
        users.append({line['name'] : line['$oid']})

    cleanData = []

    # get requests
    cursor = list(db['requests'].find())

    for line in cursor:
        for tutor in line['potential_tutors']:
            newBid = []
            if(tutor['state'] == 'SEND'):
                newBid.append('Requested')
            else:
                newBid.append('Denied')
            newBid.append(users[tutor['name']])
            newBid.append(line['$oid'])
            cleanData.append(newBid)
    
    return(cleanData)