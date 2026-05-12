##Objective: Mario and his friends are combining their money for an epic pizza and arcade party. You need to write a program that calculates their total pooled budget, their total expenses, how much money is left over, and finally, how to split the remaining cash equally among the group (finding out if there are any extra coins left over that can't be split).
##Given: 
#There is Mario + 4 friends (5 people total).
#The Budget: Mario brings 512. Each of his 4 friends contributes 250.
#The Expenses:  They buy 5 large pizzas. Each pizza costs 125.
#They buy 100 arcade tokens. Each token costs 5.
##Required: how much money is left over, how to split the remaining cash equally among the group (finding out if there are any extra coins left over that can't be split).
#The Code is below the hashtags
#########################################################################################################################################################################################################################################################################################################################################################################
# 1. Setting up the group and the budget
mario_money = 512
friend_contribution = 250
num_friends = 4
total_people = num_friends + 1 # Mario plus his 4 friends

# Calculating the total pooled money using multiplication and addition
total_money = mario_money + (friend_contribution * num_friends)

# 2. Setting up the expenses
pizza_price = 125
num_pizzas = 5
token_price = 5
num_tokens = 100

# Calculating total expenses using operator precedence (multiplication happens before addition)
total_expenses = (pizza_price * num_pizzas) + (token_price * num_tokens)

# 3. Calculating the remaining budget
remaining_money = total_money - total_expenses

# 4. Splitting the remaining money
# Standard division (/) produces a floating-point result. 
# We use int() to convert it so we only deal with whole bills/coins.
share_per_person = int(remaining_money / total_people)

# We use the remainder operator (%) to find out how many coins are left over that couldn't be split evenly.
leftover_coins = remaining_money % total_people

# 5. Showing the final results
print("PARTY BUDGET REPORT:")
print("Total pooled money:", total_money)
print("Total expenses:", total_expenses)
print("Remaining money:", remaining_money)
print("LEFTOVER SPLIT:")
print("Each person gets:", share_per_person)
print("Unsplittable leftover coins:", leftover_coins)
