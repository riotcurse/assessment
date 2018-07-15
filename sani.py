import csv
from csvstuff.csv_miami import *
from fuzzywuzzy import fuzz,process

# #return list of csv lines
# #unsure of behavior when more than one column
# def GetCSV(filename):
#     with open(filename,newline='') as readfile:
#         reader = csv.reader(readfile)
#         return [' '.join(row) for row in reader][1:]
#     return []
#
# #utils: get the clean and dirty lists
# def GetClean():
#     return GetCSV('./clean.csv')
#
# def GetDirty():
#     return GetCSV('./dirty.csv')

# given a list of comparison results, return the index of the best match
# needs fix in case of multiple best matches
def BestMatch(results):
    return results.index(max(results))

#given dirty line, set of all cleans, and a function to compare them
#generate a list of comparison values
def CompareLine(dirty,cleans,compfunc):
    return [compfunc(dirty,clean) for clean in cleans]

def CompareAll(dirties, cleans, compfunc):
    return [BestMatch(CompareLine(dirty,cleans,compfunc)) for dirty in dirties]

#main routine
#get the lists
#traverse the dirty list comparing each item to each clean item
#build a list of closest clean matches
def SaniMain(compfunc):
    clean = GetClean()
    dirty = GetDirty()
    print(len(dirty))
    return [dirty,[clean[i] for i in CompareAll(dirty,clean,compfunc)]]

if __name__ == '__main__':
    thing = SaniMain(fuzz.ratio)
    #print(len(thing))
    #for i in thing:
    #    print(i)
    WriteResult('saniout.csv',['Raw_Track_Title','Clean_TrackTitle'],thing)
