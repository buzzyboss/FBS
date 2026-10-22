li = [10,80,90,50,59,3,69,90]

new = []

for i in li:
    if i not in new:
        new.append(i)

print('list without duplicates =' , new)