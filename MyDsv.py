'''Dsv Dash separated variables, fa il verso ai CSV. Questo file serve a gestirli e utilizzarli
nei miei stuprogetti for fun.
DSV: usa --- come separatore
    La prima colonna è seguita da un tab ("t") per leggibilità e format'''

def AcquireLine(FileName, lineTag):
    '''reads a specific line from the DSV file and returns the content as list.
    In: Data file, first element of the specific line
    Out: List of data'''
    try:
        WorkingFile = open(FileName, "r", encoding = "UTF-8")
        LineFound = False
        for l in WorkingFile:
            listData = l.split("---")
            if listData[0]==lineTag +"\t": #aggiunge un TAB for file format reason
                LineFound = True
                break
        WorkingFile.close() 
        if LineFound == True:
            return listData[:-1] #Non ritorna l'ha capo \n
        return "Line not found."
    

    except:
        print("File not Found")


def wholefile(fileName):
    WF = open(fileName, encoding="UTF-8")
    for l in WF:
        print(l)

#wholefile("PG_Data.txt")    
#    
#print(AcquireLine("PG_Data.txt","Mnèmon"))
#print(AcquireLine("PG_Data.txt","Beltur"))
