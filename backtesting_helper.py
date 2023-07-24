from colorama import init, Fore, Style

init()

# Initialize variables
days = []
total = 0
current_sum = 0
win_rate = 0
max_loss_index = float('inf')
max_profit_index = float('inf')

# Loop through days and get input
print("Enter daily amounts for the month. Press ENTER to stop.")
day_index = 0
while True:
    # Get input from user
    amount_str = input(f"Day {day_index + 1}: ")

    # Check for empty input
    if amount_str == "":
        break

    try:
        amount = int(amount_str)

        # Add amount to list and total
        days.append(amount)
        total += amount

        # Update win rate
        if amount > 0:
            win_rate += 1


    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Update current sum
    current_sum += amount
    day_index += 1

# Calculate maximum sum of consecutive days
current_sum = 0
max_sum = 0
min_sum = 0
for index,amount in enumerate(days):
    current_sum = current_sum + amount
   
    # Check if max loss or max profit is hit
    if current_sum <= min_sum:
        max_loss_index = index
    if current_sum >= max_sum :
        max_profit_index = index
    
    max_sum = max(max_sum, current_sum)
    min_sum = min(min_sum, current_sum)

# Determine which was hit first
hit_first = "Max Loss" if max_loss_index < max_profit_index else "Max Profit"

# Print results
print(f"Monthly total: {total}%")
print(f"Max Profit: {max_sum}%")
print(f"Max Loss: {min_sum}%")
print(f"Win rate: {(win_rate / len(days)) * 100}%")
print(Style.BRIGHT  + f"Hit first: {hit_first}")
if min_sum < -11:
    print(Style.BRIGHT + Fore.RED + "TA QUEMAO BRO XD"+Style.RESET_ALL)

input('PRESS ENTER TO EXIT')
