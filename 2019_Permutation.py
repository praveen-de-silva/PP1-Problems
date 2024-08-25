# =====================
# PROGRAM : Permutation
# =====================

from itertools import permutations as perm

# Input :
userInt = list(input().strip().split())
n = int(input())


permInt = list(perm(userInt, len(userInt)))


# Output :
print(''.join(permInt[0]), ''.join(permInt[n-1]), ''.join(permInt[-1]))

for i in range(len(permInt)):
    print(permInt[i])
