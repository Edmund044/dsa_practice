#left pointer right pointer sum
#compare and do something
def maximum_profit(stock_prices):
    left_pointer,right_pointer = 0,1
    while right_pointer < len(stock_prices):
        if stock_prices[right_pointer] > stock_prices[left_pointer]:
            current_profit = stock_prices[right_pointer] - stock_prices[left_pointer]
            maximum_profit = max(maximum_profit,current_profit)
        else:
            left_pointer = right_pointer
        right_pointer += 1
    return maximum_profit         



         

    # left_pointer, right_pointer = 0, 1
    # maximum_profit = 0

    # while right_pointer < len(stock_prices):
    #     if(stock_prices[left_pointer]<stock_prices[right_pointer]):
    #         current_maximum_profit = stock_prices[right_pointer] - stock_prices[left_pointer]
    #         maximum_profit = max(maximum_profit,current_maximum_profit)
    #     else:
    #         left_pointer = right_pointer
    #     right_pointer += 1
    # return maximum_profit            

        
print(maximum_profit([7,1,5,3,6,4]))
print(maximum_profit([7,6,4,3,1]))

