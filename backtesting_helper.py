# Initialize variables
days = []
total = 0
max_sum = 0
current_sum = 0

# Loop through days and get input
print("Enter daily amounts for the month. Press ENTER to stop.")
while True:
    # Get input from user
    amount_str = input(f"Day {len(days)+1}: ")
    
    # Check for empty input
    if amount_str == "":
        break
    
    try:
        amount = int(amount_str)
        
        # Add amount to list and total
        days.append(amount)
        total += amount
        
        # Update max sum of consecutive days
        current_sum = max(current_sum + amount, amount)
        max_sum = max(max_sum, current_sum)
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

# Calculate maximum sum of consecutive days
current_sum = 0
for amount in days:
    current_sum = max(current_sum + amount, amount)
    max_sum = max(max_sum, current_sum)

# Print results
print(f"Monthly total: {total}")
print(f"Max sum of consecutive days: {max_sum}")
