li = [10,7,20,6,78,99,1000]

maxx = li[0]
mini = li[0]

for i in li:
    if i > maxx:
        maxx = i

    if i < mini:
        mini = i

print('maximum ==' , maxx)
print('Minimum ==',mini)