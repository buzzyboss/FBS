# map function is used to perform same task multiple times on different input
# method 1


def sq(n):
    return n*n

data = [1,2,3,4,5,6,7,8,9,10]

res = list(map(sq , data))
print(res)