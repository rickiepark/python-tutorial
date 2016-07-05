# pycharm debug test
import math


def findRoot(x, power, epsilon):
    if x < 0 and power%2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans


r1 = findRoot(4, 2, 0.01)
print(r1)

r2 = findRoot(10, 2, 0.01)
print(r2)

r3 = findRoot(30, 3, 0.01)
print(r3)
