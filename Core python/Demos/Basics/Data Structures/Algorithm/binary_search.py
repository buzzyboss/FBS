def binary_search(li , search_ele):
    beg = 0
    end = len(li)-1
    while(beg <= end):
        print('beg==',beg)
        print('end==',end)
        mid = (beg + end )//2
        print('mid==',mid)
        if(search_ele == li[mid]):
            return mid
        elif(search_ele <= li[mid]):
            end = mid - 1
        elif(search_ele >= li[mid]):
            beg = mid + 1
    else:
        return -1

li = [10,20,30,40,50]
ele = int(input('Enter the element to find=='))
res = binary_search(li , ele)
if(res != -1):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present at index {res}')