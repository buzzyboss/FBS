def linearSearch(li , search_ele):
    for ind in range(0 , len(li)):
        if(search_ele == li[ind]):
            return ind
    else:
        return -1

li = [56,89,77,91,21,43,78]
ele = int(input('Enter the element to find=='))
res = linearSearch(li , ele)
if(res != -1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present at index {res}')