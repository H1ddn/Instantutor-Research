# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:14:38 2022

@author: cruze6
"""

import json

jdata = [json.loads(line) for line in open('requests.json','r')]

cleanData = []

for req in jdata:
    for tutor in req['potential_tutors']:
        newBid = []
        if(tutor['state'] == 'SEND'):
            newBid.append('Requested')
        else:
            newBid.append('Denied')
        newBid.append(tutor['_id'])
        newBid.append(req['_id'])
        cleanData.append(newBid)