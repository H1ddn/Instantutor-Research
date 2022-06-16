# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 00:55:34 2022

@author: cruze6
"""
import numpy as np

# itertools used for test code
#import itertools

#user is an array of variables. Index 0 is the userID
#db is an array of tutors, all tutors are arrays of variables, 
#index 0 will always be that tutors userID
def cbModel(user, db):

    # test code
    #user = [1, 0, 1, 1, 0, 1, 1, 0, 0, 1]
    #N = 10;
    #db = np.array(list(itertools.product([0, 1], repeat=N)))
    
    # t is the number of tutors
    t = len(db)
    # v is the number of variables
    # user variable count and db variable count must be the same
    v = len(db[0])
    sorted = np.array(np.zeros((t,2)),dtype=object)

    # test code
    #for i in range(0, t):
    #    db[i,0] = i;


    for i in range(0, t):
        # tot = number of similarities between the user 
        # and specific tutor #i
        tot = 0;
        # j starts as 1 since j's first value will be userID
        # j ends 1 early because the last value will be a list the tutor's expertise courses
        for j in range(1, v-1):
            # if variable #j in user and tutor is equal
            # increment tot
            if(user[j] == db[i,j]):
                tot = tot + 1;
        
        # if the course the user needs help in
        # is within the tutor's expertise courses
        # we add a whopping 2 points because
        # they've literally taken the course
        if user[v-1] in db[i,v-1]:
            tot = tot + 2;
            
        tot = tot/(v);
        # first column is tutor's similarity score to user
        # next column is tutor's userID
        sorted[i,0] = tot;
        sorted[i,1] = db[i,0];    

    sorted = np.flip(sorted[sorted[:,0].argsort()[::-1]], 1);

    if(t < 10):
        out = sorted[0:t,:]
    else:
        out = sorted[0:10,:]
    
    return out
