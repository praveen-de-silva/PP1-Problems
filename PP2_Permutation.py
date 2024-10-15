from itertools import permutations as perm

##def setResult(n, nums):
##    perms = sorted(perm(nums, len(nums)))
##
##    result = f"{''.join([str(x) for x in perms[0]])} {''.join([str(x) for x in perms[n-1]])} {''.join([str(x) for x in perms[-1]])}"
##    return perms
##
##n = int(input())
##num_arr = list(map(int, input().strip().split()))
##out = setResult(n, num_arr)
##
##print(out)


def perm(arr):
    if len(arr)==2:
        return [arr, arr[::-1]]

print(perm([1,2]))
