
print("================================")
print("       FINANCIAL CALCULATOR")
print("================================")

print("1. Simple Interest")
print("2. Compound Interest")
print("3. Profit and Loss")
print("4. Percentage")

choice = int(input("\nChoose an option (1-4): "))

if choice == 1:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time in years: "))

    interest = (principal * rate * time) / 100

    print("Simple Interest:", interest)
    print("Total Amount:", principal + interest)

elif choice == 2:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time in years: "))

    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal

    print("Compound Interest:", round(interest, 2))
    print("Total Amount:", round(amount, 2))

elif choice == 3:
    cost_price = float(input("Enter cost price: "))
    selling_price = float(input("Enter selling price: "))

    if selling_price > cost_price:
        profit = selling_price - cost_price
        print("Profit:", profit)
        print("Profit Percentage:", round(profit / cost_price * 100, 2), "%")

    elif selling_price < cost_price:
        loss = cost_price - selling_price
        print("Loss:", loss)
        print("Loss Percentage:", round(loss / cost_price * 100, 2), "%")

    else:
        print("No Profit, No Loss.")

elif choice == 4:
    obtained = float(input("Enter obtained value: "))
    total = float(input("Enter total value: "))

    if total != 0:
        percentage = (obtained / total) * 100
        print("Percentage:", round(percentage, 2), "%")
    else:
        print("Total cannot be zero.")

else:
    print("Goli Beta Masti Nahi")
