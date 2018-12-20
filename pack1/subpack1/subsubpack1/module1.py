import itertools
# funcion
def nCk(n,k):
    return list(itertools.combinations(range(1,n+1),k))
def nPk(n,k):
    return list(itertools.permutations(range(1,n+1),k))
def nHk(n):
    return list(itertools.permutations(range(1,n+1)))
