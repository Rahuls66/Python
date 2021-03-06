def si(p,r,t):
    print("Principal Amount:", p)
    print("Rate of Interest:", r, "%")
    print("Time Period:", t, "units")
    simp_int = (p*r*t) / 100
    print("Simple Interest is: ", simp_int)

si(3000,4,7)    

'''
#Expected Output:
Principal Amount: 3000
Rate of Interest: 4 %
Time Period: 7 units
Simple Interest is:  840.0
'''
