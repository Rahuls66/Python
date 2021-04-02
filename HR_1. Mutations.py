#HackerRank - Mutations
def mutate_string(S, i, c):
  L = list(S)
  L[int(i)] = c
  S = ''.join(L)
  print(S)
mutate_string('abracadabra', 5, 'k')

'''
Expected Output:
abrackdabra
'''
