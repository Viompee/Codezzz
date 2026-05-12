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