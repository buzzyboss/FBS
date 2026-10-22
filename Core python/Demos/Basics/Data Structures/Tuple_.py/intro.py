#1.( ) or without( )
t = (10,20,20,30,40,'abc',3.14)
# t = (10,)

# t = 10,20,30,40

# print(type(t))


#2.heterogeneous

# print(t)

#3.Ordered

#4. immutable (cant change the values )
# t[0]= 50 raises error


#5. duplicates allowed
# print(type(t))
# print(t)

#Tuple is faster than list - because tuple has less memory block than list

import sys
tu = ()
li = []

print(sys.getsizeof(tu)) #40
print(sys.getsizeof(li)) #56