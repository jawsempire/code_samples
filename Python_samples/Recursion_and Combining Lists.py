letterlist = ['a','b','c']
numlist = ['1','2','3']

thelist = [3, 3, 3]

#Take a list of ints and recursively multiply each item together
# Note the return on the base case; 1 instead of 0
def rec(list):
    if len(list) == 0:
        return 1
    else:
        return list[0] * rec(list[1:])


print(rec(thelist))


# Pre-Contract: two lists of EQUAL size are passed as parameters to the mixed function
# Return: Combines the two lists together; if [a, b, c] and [1, 2, 3] then [a, 1, b, 2, c, 3]
def mixed(lista, listb):
     mixedlist = []
     if len(lista) == len(listb):
         stop = len(lista)
         counter = 0
         while counter != stop:
             mixedlist += lista[counter]
             mixedlist += listb[counter]
             counter += 1
         return mixedlist
     else:
        print("error! list size must be equal")

print(mixed(letterlist, numlist))

