def ass(s):
    num = "["+" ".join(map(str,s))+"]"
    return num
s = [int(x) for x in input().split(",")]
ans = ass(s)
print(ans)
##	1, 2, 3, 4, 5
## [1 2 3 4 5]
## https://contest.yandex.ru/tracks/python/data-processing-libraries/math-and-numpy the site bout modulos bout numpy
