#1. Numeric (Category)
    #1. int  (var =10)
    #2. Float (var = 3.14)
    #3. Complex (10 + 5j). Real value + Imaginary Value
#2. Text(Category)
    #1. string (var = 'FBS') / (var ="FBS") / (''' for multi Line ''') / ("""" Multiline """")
#3. Sequential
    #1. List (var = [10,20,2])
    #2. Tuples (var = (10,20,2))
#4. Set Type
    #1. set (var = {10,20,30})
    #2. frozenset ( ({10,20,30}) )
#5. Mapping 
    #1.dict (var = {1:'Python' , 2:'Java'}) key-value pair
#6. Other
    #1.Boolean (var = True / False)
    #2. None type (var = None)
#In python there is no variable decalration ..we can directly initialize variable.
#If we give same variable name and different values then it overrides.

#1.
var = 10
print(type(var))

#2.
var1 = 3.14
print(type(var1))

#3.
var2 = 10 + 5j
print(type(var2))

#1.
var3 = 'Revati'
print(type(var3))

var4 = "Revati deshpande"
print(type(var4))

#1.
var5 = [10,20,30]
print(type(var5))

#2.
var6 = (10,20,30)
print(type(var6))

#1.
var7 = {10,20,30}
print(type(var7))

#2.
var8 = ({10,20,30})
print(type(var8))

#1.
var9 = {1:'Python' , 2:'Java'}
print(type(var9))

#1.
var10 = True
print(type(var10))

#2.
var11 = None
print(type(var11))
