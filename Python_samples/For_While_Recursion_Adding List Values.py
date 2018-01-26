#Using a for, while, and recursive loop to add the values of an int list

thelist = [14, 10, 22, 26, 11, 211, 19, 64]

def theforloop(l):
    x = 0
    t = 0
    for t in l:
        x += t
    return(x)

def thewhileloop(l):
    x= k = 0
    while k != len(l):
        x += l[k]
        k +=1
    return(x)

def therecursiveloop(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + therecursiveloop(l[1:])


print('for-loop', theforloop(thelist))
print('while-loop', thewhileloop(thelist))
print('recursive-loop', therecursiveloop(thelist))