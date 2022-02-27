T = int(input()) 
for k in range(T):
    S = input() 
    even = [] 
    odd = []
    for i in range(0,len(S)):
    #even = [] 
    #odd = []
        if i%2 == 0:
            even.append(S[i]) 
        else:
            odd.append(S[i])
#print(even)
    print("".join(even),end=" ")
    print("".join(odd))
    

        