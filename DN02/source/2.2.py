from datetime import datetime
from numpy import *
from collections import defaultdict


set_printoptions(suppress=True)

data = loadtxt("../data/ratings.csv",delimiter=",",skiprows=1)

userID=[int(i) for i in data[:,0]]
movieID=[int(i) for i in data[:,1]]
ratingID=[float(i) for i in data[:,2]]
timestamp=[datetime.fromtimestamp(i).strftime('%Y-%m-%d')
           for i in data[:,3]]
relevantData=zip(movieID,ratingID)
#vse skupne ocene, št. pojavitev
allMovies=defaultdict(int)
for mID,rating in relevantData:
    if(mID not in allMovies):
        allMovies[mID]=0
    allMovies[mID]=+1

topTrueFilmi = sorted(allMovies.items(), key=lambda v: v[1], reverse=False)[:100]
print(topTrueFilmi)