import re
from csvstuff.csv_miami import *

#exp = "([ABCDEFG]|[abcdefg])( |-)(Flat|flat|Sharp|sharp|♭|b|#|♮|♯|Natural|natural)? ?(Major|Minor|major|minor)"
exp = "([ABCDEFG])( |-)?(flat|sharp|♭|b|#|♮|♯|natural)? ?(major|minor)"

def getReg():
    return re.compile(exp,re.I)

def compareAll(reg,search_strings):
    res = []
    reg = getReg()
    #return [reg.search(string).match() for string in search_strings]
    for string in search_strings:
        thing = reg.search(string)
        thing = ' ' if thing == None else thing.group()
        res.append(thing)
    return res

def KeyMain():
    titles = GetKeys()
    keys = compareAll(getReg(),titles)
    return [titles,keys]

if __name__ == '__main__':
    thing = KeyMain()
    print(len(thing[0]),len(thing[1]))
    WriteResult('keyout.csv',['Track_Title','Key_Signature'],thing)
