from pydoc import doc
from pymongo import MongoClient
import numpy as np
import json

# function updates all json files from mongodb, returns a reccomeneded next update time depending on time input
def upd(time):

    # current jsons saved
    reqs = [json.loads(line) for line in open('requests.json','r')]
    profs = [json.loads(line) for line in open('profiles.json','r')]
    users = [json.loads(line) for line in open('users.json','r')]

    # connect to MongoDB
    client = MongoClient("mongodb+srv://Adm:instutor@cluster0.s0gxd.mongodb.net/?retryWrites=true&w=majority")

    # enter the deployment's database
    db = client['deployment']

    # depending on the time between updates and the difference between the old jsons and new jsons
    # we will return a new reccomended time to update the database
    # update requests
    cursor = list(db['requests'].find())
    reqDiff = abs(((len(reqs) - len(cursor))/len(reqs) )* 100)
    # clear requests file
    open('requests.json','w').close()
    with open('requests.json','w') as outfile:
        for line in cursor:
            outfile.write(line)

    # update profiles
    cursor = list(db['profiles'].find())
    # clear profiles file
    open('profiles.json','w').close()
    with open('profiles.json','w') as outfile:
        for line in cursor:
            outfile.write(line)
            
    # update users
    cursor = list(db['users'].find())
    # clear users file
    open('users.json','w').close()
    with open('users.json','w') as outfile:
        for line in cursor:
            outfile.write(line)

    # currently, alpha = 70%
    alpha = 0.7
    # update time accordingly
    time = (time*len(reqs)*(1-alpha))/(time*(1 - alpha) + reqDiff*(alpha))
    return time;