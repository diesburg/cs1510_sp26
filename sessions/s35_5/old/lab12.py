"""
File: lab12.py
Answers
"""

def buildDictionary():
    #Build the dictionary the way we want it.
    myFile = open("actors.txt","r")
    myDict = {}
    
    for line in myFile:
        chunks = line.split(",")
        movie = chunks[0]
        actorList = chunks[1:]
        
        for actor in actorList:
            actor = actor.strip()
            if movie not in myDict:
                myDict[movie] = set()
            myDict[movie].add(actor)

    return myDict


def compareTwoMovies(movie1,movie2):
    myDict = buildDictionary() #Helper function is helpful

    #Process the two movies
    if movie1 not in myDict or movie2 not in myDict:
        print("At least one of these movies is not in the database")
        return None

    #Do the set stuff
    set1 = myDict[movie1]
    set2 = myDict[movie2]
    
    union = set1.union(set2)
    print("The union of",movie1,"and",movie2,"is:",union)

    #More set stuff
    intersection = set1.intersection(set2)
    print("The intersection of",movie1,"and",movie2,"is:",intersection)

    #More set stuff
    symDiff = set1.symmetric_difference(set2)    
    print("The symmetric difference of",movie1,"and",movie2,"is:",symDiff)

def coActors(who):
    #Read in the dictionary
    myDict = buildDictionary()

    coActors = set()

    #We need to grab all the co-actors and union them together in a set
    for movie in myDict:
        if who in myDict[movie]:
            coActors=coActors.union(myDict[movie])
            
    #Error check
    if len(coActors)==0:
        print(who,"is not in database.")

    #Ok, we have some actors.  We do need to remove the "who" actor from
    #the set, since you can't star with yourself.
    else:
        coActors.remove(who)           
        print(who,"has also starred with:",coActors)
                    
                    

