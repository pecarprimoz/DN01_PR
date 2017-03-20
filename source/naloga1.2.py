from openpyxl import load_workbook
from collections import defaultdict
movieNames= load_workbook(filename="../data/moviesRMK_V1.xlsx")
useNames = movieNames['movies']
filmZanri=[]
for i in range(2,9127):
    wholeColumn=useNames['A'+str(i)].value.split(",")
    for vrednosti in wholeColumn:
        print(vrednosti)
        if("|" in str(vrednosti) or vrednosti=="(no genres listed)") and "IMAX" not in str(vrednosti):
            filmZanri.append(vrednosti)
#print(filmZanri)

splitGenres=defaultdict(int)
for zanri in filmZanri:
    zanSplit=zanri.split("|")
    for posebaj in zanSplit:
        splitGenres[posebaj]+=1

#print(splitGenres)
stGenres=0
for key,value in splitGenres.items():
    stGenres+=1
import operator
sortedGenres=sorted(splitGenres.items(),key=operator.itemgetter(1))
print(sortedGenres)

print("ZANER\t\t\t\t\t\t\tST. POJAVITEV")
print("-------------------------------------------------")
pojavitve=[]
zaner=[]
for value in reversed(sortedGenres):
    print("%-25s | %20d" % (str(value[0]),value[1]))
    zaner.append(value[0])
    pojavitve.append(value[1])
print("Število vseh žanrov: "+str(stGenres))
import matplotlib.pyplot as plt
import numpy as np
y_axis = np.arange(1, len(zaner) + 1, 1)
plt.barh(y_axis, pojavitve[::-1], align='center')
plt.yticks(y_axis, zaner[::-1])
plt.show()