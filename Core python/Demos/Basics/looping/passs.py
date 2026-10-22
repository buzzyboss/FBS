# # pass = ignores expected indented block error

# for i in range(1 , 10):
#     pass


# # break = To terminate loop
# for i in range(1 , 5):
#     if(i == 3):
#         break
#     print(i)



# # Continue = To stop current iteration 
# for i in range(1 , 5):
#     if(i == 3):
#         continue
#     print(i)


# else = will execute when loop executed successfully
for i in range(1 , 5):
    if(i == 3):
        continue
    print(i)
else:
    print('Else block eexecuted')