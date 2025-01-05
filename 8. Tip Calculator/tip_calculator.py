total_amount = input('Input the total amount of bill: ')
tip_percent = input('Input the percent of tip: ')

float_total = float(total_amount)

float_tip_perc = float(tip_percent) / 100

tip_amount = float_total * float_tip_perc
total_with_tip = float_total + tip_amount

print(f'Tip Amount: ${tip_amount:.2f}')
print(f'Total with Tip: ${total_with_tip:.2f}')
