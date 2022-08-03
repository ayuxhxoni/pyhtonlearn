def oddeve(l):
    odd=[]
    eve=[]
    final =[odd,eve]
    for i in l:
        if i%2==0:
            eve.append(i)
        else:
            odd.append(i)
    return final
numbers = [1,2,3,4,5,6,7,8,9]
print(oddeve(numbers))