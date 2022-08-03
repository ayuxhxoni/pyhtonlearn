def rev(l):
    rev1=[]
    for i in l:
        rev1.append(i[::-1])
    return rev1
number=['abc','xyz','tuv']
print(rev(number))