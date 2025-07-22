
# Payments example
# compounded rate = (1 + period_rate) ** number of periods
# Monthly = Principal * period_rate * (compounded_rate / (compounded_rate – 1))

years = 8
interest = 0.05
payments_per_year = 12
principal = 100_000

period_rate = interest / payments_per_year
periods = years * payments_per_year

compounded_rate = (1 + period_rate) ** periods
fractional_payment = principal * period_rate * compounded_rate / (compounded_rate - 1)

payment = round(fractional_payment, 2)

print("payment = ", f"${payment:,}")

# Switch to integer pennies

left = int(principal * 100)
monthly = int(round(payment * 100, 0))
to_date = 0
for j in range(periods):
    period = j + 1
    if left > monthly:
        real_interest = left * period_rate
        # print("unrounded interest", real_interest, round(num,0))
        int_pn = round(real_interest,0)
        principal_pn = monthly - int_pn
    else:
        principal_pn = left
        int_pn = monthly - principal_pn
        
    to_date += principal_pn
    left -= principal_pn
    print("In period", period,
        "pay", f"${payment:,}",
        "principal", f"${principal_pn/100.0:,.2f}",
        "interest", f"${int_pn/100.0:,.2f}",
        "left", f"${left/100.0:,.2f}",
        "principal paid", f"${to_date/100.0:,.2f}"
    )
