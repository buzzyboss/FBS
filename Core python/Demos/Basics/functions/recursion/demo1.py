def fun(n):
    print('recursion executing')

    if(n>1):
        fun(n-1)
n=5
fun(n)
