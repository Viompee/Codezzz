# Initializing variables using the 'None' type (The "Smallest" pattern) 
largest = None
smallest = None
count = 0
total = 0

# Starting an indefinite loop using 'while True' 
while True:
    line = input("Enter a positive sensor reading (or 'done'): ")
    
    # Using 'break' to exit the loop 
    if line == 'done':
        break
        
    # Handling bad data to prevent a Traceback
    try:
        num = float(line)
    except:
        print("Invalid input - skipped.")
        continue # Using 'continue' to restart the loop for new input 
        
    # Filtering out negative numbers 
    if num < 0:
        print("Negative reading ignored.")
        continue
        
    # Pattern: Counting and Summing 
    count = count + 1
    total = total + num
    
    # Pattern: Finding the largest 
    if largest is None or num > largest:
        largest = num
        
    # Pattern: Finding the smallest
    # Using 'is' as a stronger comparison operator for None 
    if smallest is None or num < smallest:
        smallest = num

# Final output processing after the loop finishes 
print("--- Results ---")
if count > 0:
    print("Valid readings:", count)
    print("Total Sum:", total)
    print("Average:", total / count)
    print("Largest:", largest)
    print("Smallest:", smallest)
else:
    print("No valid data was entered.")