import math
def ass(s) ->float:
    return math.prod(s)**(1/len(s))
s = [int(x) for x in input().split(" ")]
ans = ass(s)
print(ans)