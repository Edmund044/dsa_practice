# knapsack problem python

def knapsack_greedy(items, max_weight):
    knapsack = []
    knapsack_weight = 0
    knapsack_profit = 0
    sorted_items = sorted(items,lambda i:i[1])

    for item in sorted_items:
        popped_item = sorted_items.pop()
        if popped_item[1] + knapsack_weight <= max_weight:
            knapsack.append(popped_item[1])
            knapsack_weight += popped_item[1]
            knapsack_profit += popped_item[2]
        else:
            break

    return knapsack,knapsack_profit,knapsack_weight    



	# knapsack = []
	# knapsack_weight = 0
	# knapsack_value = 0
	# items_sorted = sorted(items, key=keyFunc)
	# while len(items_sorted) > 0:
	# 	item = items_sorted.pop()
	# 	if item[1] + knapsack_weight <= max_weight:
	# 		knapsack.append(item)
	# 		knapsack_weight += item[1](knapsack[-1])
	# 		knapsack_value += item[2](knapsack[-1])
	# 	else:
	# 		break
	# return knapsack, knapsack_weight, knapsack_value