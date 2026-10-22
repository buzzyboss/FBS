def SumOfSeries(n):
    if(n<=0):
        return 0
    else:
        return n + SumOfSeries(n-1)
n=5
res = SumOfSeries(n)

print(res)

# factorial
# separate digit
# sum of digit
# reverse the digit