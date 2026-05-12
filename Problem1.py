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