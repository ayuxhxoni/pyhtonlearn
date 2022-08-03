def count(l):
    output =[ True if l.count(19)>=2 and l.count(5)>=3 in l else False]
    return output
print(count([19, 19, 15, 5, 3, 5, 5, 2]))