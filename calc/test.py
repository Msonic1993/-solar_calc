#Zadanie 1
string1 = "79-900"
string2 = "80-155"
removal = "-"

string1new = string1.replace(removal, "")
string2new = string2.replace(removal, "")
string1new1 = int(string1new)
string2new1 = int(string2new)

count=0
for i in range(string1new1, string2new1):
    s = str(i)
    print("Znaleziono kod pocztowy "+s[0:2]+"-"+s[2:6])
    count += 1
print("Między "+string1+ " a "+string2+" znaleziono" ,count, "kodów pocztowych")


#zadanie 2
def FindMissingNumbers(list):
    return [x for x in range(1, 11)
            if x not in list]

list = [2,3,7,4,9]
print(FindMissingNumbers(list))

#zadanie 3
import numpy as np
for i in np.arange(2, 5.5, 0.5):
    print(i)



