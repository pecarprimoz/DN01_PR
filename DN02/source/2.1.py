from datetime import datetime
from encodings import big5

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
sorted_x = sorted(tempMov.items(), key=operator.itemgetter(0))
temp=[]
for key,value in sorted_x:
    temp.append(value)
import matplotlib.pyplot as plt
plt.hist(temp, bins='auto')
plt.title("Porazdelitev standardnih odklonov filmov.")
plt.show()
#opazimo da je normalna porazdelitev (zvonasta)
#sedaj zanimali nas bodo tisti filmi ki imajo standardni odklon
#pod 0.6 in nad 1.2
specialDownSet=set()
specialUpSet=set()
specialDown=defaultdict(str)
specialUp=defaultdict(str)
for key,value in tempMov.items():
    if value<=0.6:
        specialDownSet.add(key)
    elif value >=1.2:
        specialUpSet.add(key)

from openpyxl import load_workbook

movieNames= load_workbook(filename="../data/moviesRMK_V1.xlsx")
useNames = movieNames['movies']
useNamesID=[]
useNamesName=[]
for i in range(2,9127):
    wholeColumn=useNames['A'+str(i)].value.split(",")
    useNamesID.append(wholeColumn[0])
    useNamesName.append(wholeColumn[1])

print(specialUpSet)
for id,movieName in zip(useNamesID,useNamesName):
    if int(id) in specialUpSet:

        specialUp[id]=movieName
    elif int(id) in specialDownSet:
        specialDown[id] = movieName
#mas use narjen, preglej se mal teorijo pa bo
print(specialUp)
print(specialDown)