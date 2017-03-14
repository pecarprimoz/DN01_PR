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
#skupni rating (allMovies[key][0][1])
#št. pojavitev (allMovies[key][0][0])

avgRatings=defaultdict(float)
for key,value in allMovies.items():
    if(allMovies[key][0][1]!=0):
        print(allMovies[key][0][1])
        avgRatings[key]=allMovies[key][0][0]/allMovies[key][0][1]
    else:
        avgRatings[key]=-1

topFilmi=sorted(avgRatings.items(), key=lambda v: v[1], reverse=True)
#print(topFilmi)

#težava ker je film ocenjen enkrat ali manjkrat, popravimo tako da vzamemo vse filme ki so bili ocenjeni več kot 15x
trueAvgRatings=defaultdict(float)
for key,value in allMovies.items():
    if (allMovies[key][0][1] != 0 and allMovies[key][0][1]>30):
        trueAvgRatings[key] = allMovies[key][0][0] / allMovies[key][0][1]
    else:
        trueAvgRatings[key] = -1

topTrueFilmi = sorted(trueAvgRatings.items(), key=lambda v: v[1], reverse=True)[:10]
#print(topTrueFilmi)

#uporablam openpyxl od kle naprej ker ima numpy probleme
from openpyxl import load_workbook

movieNames= load_workbook(filename="moviesRMK_V1.xlsx")
useNames = movieNames['movies']
useNamesID=[]
useNamesName=[]
for i in range(2,9127):
    wholeColumn=useNames['A'+str(i)].value.split(",")
    useNamesID.append(wholeColumn[0])
    useNamesName.append(wholeColumn[1])

useNamesID=[int(i) for i in useNamesID]
skupajImena=zip(useNamesID,useNamesName)
finalShape=defaultdict(list)
for idFilma,avgRating in topTrueFilmi:
    finalShape[idFilma]=[avgRating,str()]



for skval in topTrueFilmi:
    for id,movname in zip(useNamesID,useNamesName):
        if(id==skval[0]):
            finalShape[id][1]=movname
            break
    #TIL, če zippaš dva arraya prej in ju uporabš v for zanki, se noče restartat, če nardiš vsakič na novo je vredu?

#for key,value in finalShape.items():
#    print(str(key)+"\t"+str(value))
finishedSortedArray=[]
for key,value in finalShape.items():
    finishedSortedArray.append(value)

from operator import itemgetter

urejenSeznam=sorted(finishedSortedArray,key=itemgetter(0))
print("%-55s | %20s" % ("IME FILMA","NJEGOV RATING"))
a= ["-" for i in range(0,80)]
print("".join(a))

for value in reversed(urejenSeznam):
    print("%-55s | %20f" % (str(value[1]).replace("\"",""),value[0]))



#dtTest=pd.read_csv('movies.csv')
#workingMovies=np.corrcoef(dtTest)
#print(workingMovies)

#MmovieID = [int(i) for i in dataFilmiIme[:,0]]
#movieName=[i for i in dataFilmiIme[:,1]]
#print(movieName)


#   Debugging
#for i in timestamp:
#    print(i)
#print(data.shape)
#print("USERID -  MOVIEID  -  RATING  -  TIMESTAMP")
#print(str(int(data[0][0]))+"\t\t\t"+str(int(data[0][1]))+"\t\t\t"+
#    str(float(data[0][2])) + "\t\t\t" + str((data[0][3])))
#for key,value in allMovies.items():
#    print(str(key)+"   "+str(value))
#for key,value in avgRatings.items():
#    print(str(key)+"   "+str(value))
#izpis vseh id-jev in imen
#print(useNamesID)
#print(useNamesName)

