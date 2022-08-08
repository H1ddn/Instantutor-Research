import dbUpd
import loadTutors as lt
import loadProfiles as lp
import tutorPopComparison as tpc
import reqML
import cbModCustW as cb

def model():

    # grab appropriate data and turn into usable arrays
    profiles = lp()
    relations = tpc()

    # use arrays to build weights for content model
    weights = reqML(relations, profiles)

    # return custom weights for model use
    return {'weights': weights}
    


