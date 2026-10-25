def total_calc(bill_amount, tip_per):
    total = bill_amount + (bill_amount*(tip_per/100))
    rounded_total = round(total, 2)

    print(f"your rounded total is {rounded_total}")

total_calc(150, 20)
