import csv

#return list of csv lines
#unsure of behavior when more than one column
#cols param skips the headers
def GetCSV(filename,cols=1):
    with open(filename,newline='') as readfile:
        reader = csv.reader(readfile)
        return [' '.join(row) for row in reader][cols:]
    return []

def GetCSV_dict(filename,column_names):
    with open(filename,newline='') as readfile:
        reader = csv.DictReader(readfile)
        return [[row[column] for column in column_names] for row in reader]
    return []

def condense(track_info):
    res = {}

    #iterate through all rows
    for row in track_info:
        #use ptr to descend into dict structure
        ptr = res
        for i in row:
            if not ptr.__contains__(i):
                ptr[i] = {}
            ptr = ptr[i]
    return res

def MakeTracks(trobject):
    res = []
    for id in trobject:
        #get dict of work_names
        work = trobject[id]
        work_names = [*work]
        for name in work_names:
            #get dict of movement_names
            movements = work[name]
            for movement in movements:
                title = ''
                if movement != '' and len(movements) > 1:
                    title = name + ': ' + movement
                res.append([id,name,movement,title])
    return res



#utils: get the clean and dirty lists
def GetClean():
    return GetCSV('./clean.csv')

def GetDirty():
    return GetCSV('./dirty.csv')

def GetKeys():
    return GetCSV('./keys.csv',cols=2)

def WriteResult(filename,column_names,columns):
    print(len(column_names),len(columns))
    print([len(column) for column in columns])
    with open(filename,'w',newline='') as csvout:
        writer = csv.DictWriter(csvout, fieldnames=column_names)
        writer.writeheader()
        for i in range(len(columns[0])):
            writer.writerow({column_names[j]:columns[j][i] for j in range(len(column_names))})
