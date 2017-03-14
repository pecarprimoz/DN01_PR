from datetime import datetime
from numpy import *
from collections import defaultdict


set_printoptions(suppress=True)

data = loadtxt("ratings.csv",delimiter=",",skiprows=1)

userID=[int(i) for i in data[:,0]]
movieID=[int(i) for i in data[:,1]]
ratingID=[float(i) for i in data[:,2]]
timestamp=[datetime.fromtimestamp(i).strftime('%Y-%m-%d')
           for i in data[:,3]]
relevantData=zip(movieID,ratingID)
#vse skupne ocene, št. pojavitev
allMovies=defaultdict(list)
for mID,rating in relevantData:
    if(mID not in allMovies):
        allMovies[mID].append([0.0,0])
    allMovies[mID][0][1]+=1
    allMovies[mID][0][0]+=rating
#skupni št ocen (allMovies[key][0][1])
#skupna vsota ocen (allMovies[key][0][0])

avgRatings=list()
for key,value in allMovies.items():
    if(allMovies[key][0][1]>10):#dodal bomo filme k so ocenjeni vsaj z 30 ocenami
        avgRatings.append([key,allMovies[key][0][0]/allMovies[key][0][1],allMovies[key][0][1]])

print(avgRatings)
from operator import itemgetter
urejenoPoOgledihPad=sorted(avgRatings, key=itemgetter(2))[:10]
urejenoPoOgledihNar=sorted(avgRatings, key=itemgetter(2), reverse=True)[:10]
print("IZPIS JE MOVIE ID, MOVIE AVG. SCORE, MOVIE ST. OCEN")
print("PADAJOCE ZAPOREDJE")
print(urejenoPoOgledihPad)
print("NARASCAJOCE ZAPOREDJE")
print(urejenoPoOgledihNar)
#ugotovitev da večkrat gledani/ocenjeni filmi so boljše ocenjeni kot filmi ki so ocenjeni ~11 krat