"""
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. 
The possible banknotes are 100, 50, 20, 10, 5, 2 and 1. 
Print the read value and the list of banknotes.
"""

def bankNotes(value, notes):
    notesQtt = value // notes
    rest = value % notes
    print("%d nota(s) de R$ %d,00" %(notesQtt, notes))
    return rest
    
intValue = int(input())
print("%d" %intValue)

restValue = bankNotes(intValue, 100)
restValue = bankNotes(restValue, 50)
restValue = bankNotes(restValue, 20)
restValue = bankNotes(restValue, 10)
restValue = bankNotes(restValue, 5)
restValue = bankNotes(restValue, 2)
restValue = bankNotes(restValue, 1)