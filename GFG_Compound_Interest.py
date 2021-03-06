
def ci(p,r,t):
    print("Principal Amount:", p, "/-")
    print("Rate of Interest:", r, "%")
    print("Time Period:", t, "units")
    a = p * ((1 + r / 100) ** t)
    comp_int = a - p
    print("Compound Interest:", round(comp_int,2), "/-")

ci(35000, 6.5, 9)

'''
Expected Output:
Principal Amount: 35000 /-
Rate of Interest: 6.5 %
Time Period: 9 units
Compound Interest: 26689.96 /-
'''
