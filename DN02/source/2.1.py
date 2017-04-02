from datetime import datetime
import numpy as np
from collections import defaultdict

np.set_printoptions(suppress=True)

data = np.loadtxt("../data/ratings.csv",delimiter=",",skiprows=1)

userID=[int(i) for i in data[:,0]]
movieID=[int(i) for i in data[:,1]]
ratingID=[float(i) for i in data[:,2]]
timestamp=[datetime.fromtimestamp(i).strftime('%Y-%m-%d')
           for i in data[:,3]]
relevantData=zip(movieID,ratingID)
allMovies=defaultdict(list)
for i1,i2 in relevantData:
    allMovies[i1].append(i2)

#allMovies[key][0] je seznam ocen
#allMovies[key][1] je aritmetična sredina
#allMovies[key][1] je varianca
statisticMovies=defaultdict(list)
for key,value in allMovies.items():
    if(len(value)>=30):
        statisticMovies[key].append(sorted(value))
        statisticMovies[key].append([np.std(statisticMovies[key][0])])

tempMov=defaultdict(float)
for key,value in statisticMovies.items():
    tempMov[key]=value[1][0]

print(tempMov)
import operator
sorted_x = sorted(tempMov.items(), key=operator.itemgetter(1))
print(sorted_x)
