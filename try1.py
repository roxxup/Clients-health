import time
muobj = open('log.txt',"r+")
for l in muobj.readlines():
    print l
muobj.write()