# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:14:38 2022

@author: cruze6
"""

import json

# Grabs all made requests and returns a dictionary including all requests in form
# [state, tutor id, student id]
# state refers to if the student selected the tutor or not. 'Requested' if true, 'Denied' if false.
def getReqs():
    jreq = [json.loads(line) for line in open('requests.json','r')]
    juse = [json.loads(line) for line in open('users.json','r')]

    # The system currently works through a name / id basis
    # requests are related to names and ids. For the student
    # calling the request, the id is the same on both ends
    # but for tutors, the id is different. In order to correlate
    # a tutor to their profile, we need to take note of their name
    # then look for their user id in the users.json
    # this is something being fixed in the future
    users = {}
    for user in juse:
        users.append({user['name'] : user['$oid']})

    cleanData = []

    for req in jreq:
        for tutor in req['potential_tutors']:
            newBid = []
            if(tutor['state'] == 'SEND'):
                newBid.append('Requested')
            else:
                newBid.append('Denied')
            newBid.append(users[tutor['name']])
            newBid.append(req['$oid'])
            cleanData.append(newBid)
    
    return(cleanData)