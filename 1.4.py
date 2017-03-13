from datetime import datetime
from numpy import *
from collections import defaultdict
#ID IME FILMA RATING
#858 GODFATHER
from scipy.stats._discrete_distns import randint_gen

set_printoptions(suppress=True)

data = loadtxt("ratings.csv",delimiter=",",skiprows=1)

movieID=[int(i) for i in data[:,1]]
ratingID=[float(i) for i in data[:,2]]
counter=0

timestamp=[datetime.fromtimestamp(i).strftime('%Y-%m-%d')
           for i in data[:,3]]

timestamp.sort()
relevantData=zip(movieID,ratingID,timestamp)

godRatings=list()
for mID,rating, time in relevantData:
    if(mID==858):
        godRatings.append([rating,time])

#print(godRatings)
avgRatings=defaultdict(float)
counter=0
currentScoreSum=0

for rating, time in godRatings:
    counter+=1
    currentScoreSum+=rating
    if(counter==30 or counter==50 or counter==100 or counter==150 or counter==200):
        avgRatings[time]=currentScoreSum/counter
#print(avgRatings)

padajoceGod = sorted(avgRatings.items(), key=lambda v: v[1], reverse=False)
print("Statistika za godfatherja")
print(padajoceGod)
#test narejen na godfatherju pokaže da ocena kvečjemu narašča
#poskusimo še na Shawshank Redemption, film ki ima več kot 250 ocen in je tudi najboljši film z oceno 4.487138
data = loadtxt("ratings.csv",delimiter=",",skiprows=1)

movieID=[int(i) for i in data[:,1]]
ratingID=[float(i) for i in data[:,2]]
counter=0

timestamp=[datetime.fromtimestamp(i).strftime('%Y-%m-%d')
           for i in data[:,3]]

timestamp.sort()
relevantData=zip(movieID,ratingID,timestamp)
shawkRatings=list()
for mID,rating, time in relevantData:
    if(mID==318):
        shawkRatings.append([rating,time])

#print(godRatings)
avgRatings=defaultdict(float)
counter=0
currentScoreSum=0

for rating, time in shawkRatings:
    counter+=1
    currentScoreSum+=rating
    if(counter==30 or counter==50 or counter==100 or counter==150 or counter==200 or counter==250):
        avgRatings[time]=currentScoreSum/counter
print("Statistika za Shawshank")
padajoceShawk = sorted(avgRatings.items(), key=lambda v: v[1], reverse=False)
print(padajoceShawk)
#tudi tukaj vidimo da ocena kvečjemu narašča z časom

#še primer slabega filma, home alone več kot 100 ratingov z ratingom 3.112403
data = loadtxt("ratings.csv",delimiter=",",skiprows=1)

movieID=[int(i) for i in data[:,1]]
ratingID=[float(i) for i in data[:,2]]
counter=0

timestamp=[datetime.fromtimestamp(i).strftime('%Y-%m-%d')
           for i in data[:,3]]

timestamp.sort()
relevantData=zip(movieID,ratingID,timestamp)
shawkRatings=list()
for mID,rating, time in relevantData:
    if(mID==586):
        shawkRatings.append([rating,time])

#print(godRatings)
avgRatings=defaultdict(float)
counter=0
currentScoreSum=0

for rating, time in shawkRatings:
    counter+=1
    currentScoreSum+=rating
    if(counter==30 or counter==50 or counter==100 or counter>128):
        avgRatings[time]=currentScoreSum/counter
print("Statistika za Home alone")
padajoceShawk = sorted(avgRatings.items(), key=lambda v: v[1], reverse=False)
print(padajoceShawk)
#za zelo slab filem bi pričakoval da povprečna ocena pada, vendar v tem primeru narašča