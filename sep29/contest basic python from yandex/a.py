#https://new.contest.yandex.ru/contests/41248/problems?id=149944%2F2022_11_06%2FpFNA5C1tPm
from math import log, cos, sin, pi, e
x = float(input())
a = log(x ** (3 / 16), 32)
b = x ** cos((pi * x) / (2 * e))
c = sin(x / pi) ** 2
print(a+b-c)