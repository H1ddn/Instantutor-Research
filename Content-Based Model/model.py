import dbUpd
import loadTutors as lt
import loadProfiles as lp
import tutorPopComparison as tpc
import reqML
import cbModCustW as cb


# model runs after time is over
def model(time):

    # first, update with new time
    time = dbUpd(time)

    # second, grab appropriate data and turn into usable arrays
    profiles = lp()
    relations = tpc()

    # third, use arrays to build weights for content model
    weights = reqML(relations, profiles)

    # return the new time and weights in a dict
    # These return values are to be used in cbModCustW
    # or are used to run model again after a certain time
    return {'time': time, 'weights': weights, 'tutors': lt()}
    


