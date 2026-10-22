li = [20,30,40,54,38,100]

maxx = li[0]
smaxx = li[0]

for i in li:
    if i > maxx:
        smaxx = maxx
        maxx = i
    elif i > smaxx and i < maxx:
        smaxx = i

print('second maxx is ==',smaxx)