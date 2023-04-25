def find_closest_pair(pairs, target):
    """
    Given a set of number pairs and a target number, returns the pair
    with the closest value to the target.
    """
    closest_pair = None
    closest_dist = float('inf')
    
    for pair in pairs:
        for num in pair:
            dist = abs(num - target)
            if dist < closest_dist or (dist == closest_dist and pair != closest_pair):
                closest_pair = pair
                closest_dist = dist
    
    return closest_pair

# Ask the user for input
input_num = float(input("Enter asset's current price: "))
spread = float(input("Enter the spread: "))

# Define the set of number pairs
pairs = [(10540, 10550), (10620, 10630), (10740, 10750), (10830, 10840), (10940, 10950), (11040, 11050), (11120, 11130), (11240, 11250), (11340, 11350), (11420, 11430), (11540, 11550), (11630, 11640), (11740, 11750), (11820, 11830), (11940, 11950), (12030, 12040), (12140, 12150), (12230, 12240), (12340, 12350), (12430, 12440), (12540, 12550), (12630, 12640), (12740, 12750), (12820, 12830), (12940, 12950), (13030, 13040), (13140, 13150), (13230, 13240), (13340, 13350), (13430, 13440), (13540, 13550), (13630, 13640), (13740, 13750), (13830, 13840), (13940, 13950), (14030, 14040), (14140, 14150), (14230, 14240), (14340, 14350), (14430, 14440), (14540, 14550), (14630, 14640), (14740, 14750), (14830, 14840), (14940, 14950), (15065, 15075), (15140, 15150), (15230, 15240), (15340, 15350), (15440, 15450), (15540, 15550), (15630, 15640), (15740, 15750), (15830, 15840), (15940, 15950), (16030, 16040), (16140, 16150), (16230, 16240), (16340, 16350), (16430, 16440), (16540, 16550), (16630, 16640)]
# Find the pair with the closest value to the input number
closest_pair = find_closest_pair(pairs, input_num)

# Find the first pair where the first number is greater than the input number
greater_pair = None
for pair in pairs:
    if pair[0] >= input_num and (greater_pair is None or pair[0] < greater_pair[0]):
        greater_pair = pair

# Find the first pair where the first number is less than the input number
lesser_pair = None
for pair in pairs:
    if pair[0] <= input_num and (lesser_pair is None or pair[0] > lesser_pair[0]):
        lesser_pair = pair

not_closest_pair = lesser_pair if closest_pair == greater_pair else greater_pair

is_closest_lesser = lesser_pair == closest_pair

closest_first_operation = 'SELL STOP' if is_closest_lesser else 'BUY LIMIT'

closest_second_operation = 'BUY LIMIT' if is_closest_lesser else 'SELL STOP'

not_closest_first_operaton ='BUY STOP' if is_closest_lesser else 'SELL LIMIT'
not_closest_second_operaton ='SELL LIMIT' if is_closest_lesser else 'BUY STOP'


# Print the results
print(f'The current Price is {input_num}. with a {spread} spread.\n')
if closest_pair:
    first_entry_point = closest_pair[1] + spread if is_closest_lesser else closest_pair[0] + spread
    first_sl = first_entry_point + 25 if is_closest_lesser else first_entry_point - 25
    first_tp = first_entry_point - 100 if is_closest_lesser else first_entry_point + 100
    first_alarm = first_entry_point - 40 if is_closest_lesser else first_entry_point +40
    second_entry_point = closest_pair[0] + spread if is_closest_lesser else closest_pair[1] + spread
    second_sl = second_entry_point - 25 if is_closest_lesser else second_entry_point + 25
    second_tp = second_entry_point + 100 if is_closest_lesser else second_entry_point - 100
    second_alarm = second_entry_point + 40 if is_closest_lesser else second_entry_point -40

    print('The closest trades to the current price are (place these first): \n')
    print(f'Create a {closest_first_operation} with Entry Point: {first_entry_point}. SL: {first_sl}. TP: {first_tp}.')
    print(f'SET A PRICE ALARM AT {first_alarm}\n')
    print(f'Create a {closest_second_operation} with Entry Point: {second_entry_point}. SL: {second_sl}. TP: {second_tp}.')
    print(f'SET A PRICE ALARM AT  {second_alarm} \n')
print(f'--------------------------------------------------------\n')
if not_closest_pair:
    first_entry_point = not_closest_pair[0] + spread if is_closest_lesser else not_closest_pair[1] + spread
    first_sl = first_entry_point + 25 if is_closest_lesser else first_entry_point - 25
    first_tp = first_entry_point - 100 if is_closest_lesser else first_entry_point + 100
    first_alarm = first_entry_point - 40 if is_closest_lesser else first_entry_point +40
    second_entry_point = closest_pair[0] + spread if is_closest_lesser else closest_pair[1] + spread
    second_sl = second_entry_point - 25 if is_closest_lesser else second_entry_point + 25
    second_tp = second_entry_point + 100 if is_closest_lesser else second_entry_point - 100
    second_alarm = second_entry_point + 40 if is_closest_lesser else second_entry_point -40
    print('The furthest trades to the current price are (place these last):\n')
    print(f'Create a {not_closest_first_operaton} with Entry Point: {first_entry_point}. SL: {first_sl}. TP: {first_tp}.')
    print(f'SET A PRICE ALARM AT  {first_alarm}\n')
    print(f'Create a {not_closest_second_operaton} with Entry Point: {second_entry_point}. SL: {second_sl}. TP: {second_tp}.')
    print(f'SET A PRICE ALARM AT {second_alarm}\n')

    # add this at the end of your script
input("Press enter to exit")
