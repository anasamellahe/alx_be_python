monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings =  monthly_income -  monthly_expenses
if (monthly_savings < 0):
    print("You don't save any money.")
    exit()
print("Your monthly savings are $", monthly_savings)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: $",int(projected_savings),".", sep="")