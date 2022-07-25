import numpy as np

#user is an array of variables. Index 0 is the userID
#db is an array of tutors, all tutors are arrays of variables, 
#weights are custom weights from ML
#index 0 will always be that tutors userID
def cbModel(user, db, weights):

    t = len(db)
    v = len(db[0])
    sorted = np.array(np.zeros((t,2)),dtype=object)

    for i in range(0, t):
        tot = 0;
        for j in range(1, v-1):
            if(user[j] == db[i,j]):
                tot = tot + weights[j - 1];
        if user[v-1] in db[i,v-1]:
            tot = tot + weights[v - 1];
            
        tot = tot/(v);
        sorted[i,0] = tot;
        sorted[i,1] = db[i,0];    

    sorted = np.flip(sorted[sorted[:,0].argsort()[::-1]], 1);

    if(t < 10):
        out = sorted[0:t,:]
    else:
        out = sorted[0:10,:]
    
    return out
