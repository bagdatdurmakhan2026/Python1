import math
def ass(s):
    ans = math.gcd(*s)
    return ans
s = [int(x) for x in input().split(" ")]
res = ass(s)
print(res)