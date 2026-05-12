##Objective: Mario and friends (4 people total) are planning a road trip. You need to calculate how many liters of gas will be need, the total cost of the gas, and how much each person needs to pay.
##Given:
#The total distance of the trip is 300 kilometers.
#Your car can travel 12 kilometers on a single liter of gas (fuel efficiency).
#The current price of gas is 60 per liter.
##Required: how many liters of gas needed, total cost of gas, payment per person.
#The Code is below the hashtags
#######################################################################################################################################################################################################
# Setting up the trip details
total_distance = 300 
km_per_liter = 12 
price_per_liter = 60
people = 4

# Calculating the liters of gas needed (Division)
# We divide the total distance by the car's fuel efficiency
liters_needed = total_distance / km_per_liter

# Calculating the total cost (Multiplication)
# We multiply the liters needed by the price per liter
total_cost = liters_needed * price_per_liter

# Calculating how much each person pays (Division)
# We divide the total cost by the number of people
cost_per_person = total_cost / people

# Showing the final results
print("Total distance (km):", total_distance)
print("Liters of gas needed:", liters_needed)
print("Total gas cost (PhP):", total_cost)
print("Cost per person (PhP):", cost_per_person)
