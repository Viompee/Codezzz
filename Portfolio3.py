# Defining my function with the two required parameters
def computepay(hours, rate):
    # Checking if I need to calculate overtime
    if hours > 40:
        standard_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        overtime_pay = overtime_hours * overtime_rate
        total_pay = standard_pay + overtime_pay
    else:
        # Just regular pay if 40 hours or less
        total_pay = hours * rate
        
    # Returning the result to make it a fruitful function
    return total_pay

# Getting the inputs for my program
hours_input = input("Enter Hours: ")
rate_input = input("Enter Rate (PhP): ")

# Using built-in functions to convert my strings to floats so the math works
try:
    h = float(hours_input)
    r = float(rate_input)
except ValueError:
    print("Error: Please enter a numeric value.")
    quit()

# Calling my function, passing my arguments, and saving the result
final_pay = computepay(h, r)

# Printing out my final result
print("Pay:", final_pay)