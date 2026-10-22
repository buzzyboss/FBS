#Heterogeneous and ordered

di = { 1:'Python' , 2:'Java' , 3:'Java' , 'year':2026 , 1:'PHP'}

#keys : immutable and values: mutable    size mutable
di['year'] = 2027 
di['age'] = 22

#keys:unique and values : duplicates are allowed

print(type(di))
print(di)