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
pairs = [    (10140, 10150), (10230, 10240), (10340, 10350), (10430, 10440), (10540, 10550),
    (10630, 10640), (10740, 10750), (10830, 10840), (10940, 10950), (11030, 11040),
    (11140, 11150), (11230, 11240), (11340, 11350), (11430, 11440), (11540, 11550),
    (11630, 11640), (11740, 11750), (11830, 11840), (11940, 11950), (12030, 12040),
    (12140, 12150), (12230, 12240), (12340, 12350), (12430, 12440), (12540, 12550),
    (12630, 12640), (12740, 12750), (12830, 12840), (12940, 12950), (13030, 13040),
    (13140, 13150), (13230, 13240), (13340, 13350), (13430, 13440), (13540, 13550),
    (13630, 13640), (13740, 13750), (13830, 13840), (13940, 13950), (14030, 14040),
    (14140, 14150), (14230, 14240), (14340, 14350), (14430, 14440), (14540, 14550),
    (14630, 14640), (14740, 14750), (14830, 14840), (14940, 14950), (15030, 15040),
    (15140, 15150), (15230, 15240), (15340, 15350), (15430, 15440), (15540, 15550),
    (15630, 15640), (15740, 15750), (15830, 15840), (15940, 15950), (16030, 16040),
    (16140, 16150), (16230, 16240), (16340, 16350), (16430, 16440), (16540, 16550),
    (16630, 16640), (16740, 16750), (16830, 16840), (16940, 16950), (17030, 17040),
    (17140, 17150), (17230, 17240), (17340, 17350), (17430, 17440), (17540, 17550),
    (17630, 17640), (17740, 17750), (17830, 17840), (17940, 17950), (18030, 18040),
    (18140, 18150), (18230, 18240), (18340, 18350), (18430, 18440), (18540, 18550),
    (18630, 18640), (18740, 18750), (18830, 18840), (18940, 18950), (19030, 19040),
    (19140, 19150), (19230, 19240), (19340, 19350), (19430, 19440), (19540, 19550),
    (19630, 19640), (19740, 19750), (19830, 19840), (19940, 19950), (20030, 20040),
    (20140, 20150), (20230, 20240), (20340, 20350), (20430, 20440), (20540, 20550),
    (20630, 20640), (20740, 20750), (20830, 20840), (20940, 20950), (21030, 21040),
    (21140, 21150), (21230, 21240), (21340, 21350), (21430, 21440), (21540, 21550),
    (21630, 21640), (21740, 21750), (21830, 21840), (21940, 21950), (22030, 22040),
    (22140, 22150), (22230, 22240), (22340, 22350), (22430, 22440), (22540, 22550),
    (22630, 22640), (22740, 22750), (22830, 22840), (22940, 22950), (23030, 23040),
    (23140, 23150), (23230, 23240), (23340, 23350), (23430, 23440), (23540, 23550),
    (23630, 23640), (23740, 23750), (23830, 23840), (23940, 23950), (24030, 24040),
    (24140, 24150), (24230, 24240), (24340, 24350), (24430, 24440), (24540, 24550),
    (24630, 24640), (24740, 24750), (24830, 24840), (24940, 24950), (25030, 25040),
    (25140, 25150), (25230, 25240), (25340, 25350), (25430, 25440), (25540, 25550),
    (25630, 25640), (25740, 25750), (25830, 25840), (25940, 25950), (26030, 26040),
    (26140, 26150), (26230, 26240), (26340, 26350), (26430, 26440), (26540, 26550),
    (26630, 26640), (26740, 26750), (26830, 26840), (26940, 26950), (27030, 27040),
    (27140, 27150), (27230, 27240), (27340, 27350), (27430, 27440), (27540, 27550),
    (27630, 27640), (27740, 27750), (27830, 27840), (27940, 27950), (28030, 28040),
    (28140, 28150)]
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

closest_first_operation = 'SELL STOP' if is_closest_lesser else 'BUY STOP'

closest_second_operation = 'BUY LIMIT' if is_closest_lesser else 'SELL LIMIT'

not_closest_first_operaton ='BUY STOP' if is_closest_lesser else 'SELL STOP'
not_closest_second_operaton ='SELL LIMIT' if is_closest_lesser else 'BUY LIMIT'


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
    first_sl = first_entry_point - 25 if is_closest_lesser else first_entry_point + 25
    first_tp = first_entry_point + 100 if is_closest_lesser else first_entry_point - 100
    first_alarm = first_entry_point + 40 if is_closest_lesser else first_entry_point -40
    second_entry_point = not_closest_pair[1] + spread if is_closest_lesser else not_closest_pair[0] + spread
    second_sl = second_entry_point + 25 if is_closest_lesser else second_entry_point - 25
    second_tp = second_entry_point - 100 if is_closest_lesser else second_entry_point + 100
    second_alarm = second_entry_point - 40 if is_closest_lesser else second_entry_point +40
    print('The furthest trades to the current price are (place these last):\n')
    print(f'Create a {not_closest_first_operaton} with Entry Point: {first_entry_point}. SL: {first_sl}. TP: {first_tp}.')
    print(f'SET A PRICE ALARM AT  {first_alarm}\n')
    print(f'Create a {not_closest_second_operaton} with Entry Point: {second_entry_point}. SL: {second_sl}. TP: {second_tp}.')
    print(f'SET A PRICE ALARM AT {second_alarm}\n')

    # add this at the end of your script
input("Press enter to exit")
