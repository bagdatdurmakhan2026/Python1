## sort by recursiv method
## input 1,2,4,6,2,3,5
def ass(s):
    n = len(s)
    for x in range(n-1):
        if s[x]>s[x+1]:
            s[x],s[x+1]=s[x+1],s[x]
            return ass(s)
    return s
ans =[int(y) for y in input().split(',')]
nas = ass(ans)
print(nas)