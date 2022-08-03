def hanji(n):
    revstring=[str(i) for i in n if type(i)==int or type(i)==float]
    return revstring

hmm =['abc', 'tuv', 'xyz',[1,2,3], 1, 1.0, 3]
print(hanji(hmm))