on_road=1755000
down_payment=250000
bankintrest=9
P=total_loan = on_road - down_payment
N=loan_period_months=24
R=intrestpermonth=(bankintrest/12)/100
emi=(P*R*(1+R)**N) / ((1+R)**N-1)
print(emi)

