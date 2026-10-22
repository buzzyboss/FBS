#1. structure= []
li = [10,20,30,40,3.14,'abc']
print(li)
#2. Types of data= Hetergogeneous 10,20,30,40,3.14,'abc'

#3. sequential = ordered

#4. Changable = Mutable ..we can change values

li[0] = 50
print(li)

#5. Duplications = allowed
print(id(li)) # same id bcos uses same memory
li[2]=20
print(li)
print(id(li)) # same id bcos uses same memory