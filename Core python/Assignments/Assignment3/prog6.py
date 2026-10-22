CP = int(input('Enter the cost price'))
SP = int(input('Enter the selling price'))

if SP > CP:
    profit = SP - CP
    print("profit =" , profit)
elif CP > SP:
    loss = CP - SP
    print("loss =" , loss)