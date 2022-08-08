# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 21:02:18 2022

@author: cruze6
"""
from sklearn.linear_model import SGDRegressor

# input two matricies.
# 
# reqs is a list of requests for tutoring made by students
# reqs[0] is if the student selected said tutor or not
# reqs[1] is the student id
# reqs[2] is the tutor id
#
# users is a list of ids correlating to info on that id's user
# this means major, degree, courses, etc.
#
# returns a list of weights that increase the chance for a user
# to pick a tutor based on the similarity of their profiles
def reqML(reqs, profiles):
    x = []
    y = []
    
    # create matricies using reqs data
    for match in reqs:
        # if tutor was requested, y = 1, else, y = 0
        if(reqs[0] == 'Requested'):
            y.append(1)
        else:
            y.append(0)
        # add to x the tutor data, then the student data
        vector = []
        tutor = profiles[reqs[1]]
        student = profiles[reqs[2]]
        for i in range(len(tutor)):
            if(tutor[i] == student[i]):
                vector.append(1)
            else:
                vector.append(0)
        x.append(vector)

    # run SGD to get best weights
    # idk abt using SciLearn, perhaps
    # in the future, build our own. should be simple
    classifier = SGDRegressor(alpha = 0.01)
    # decided to use high regularization because 
    # much of the y = 1s and y = 0s will be muddled
    # close together. If low regularization, could lead
    # to complex and invalid prediction
    
    classifier.fit(x, y)
    return(classifier.coef_)
        