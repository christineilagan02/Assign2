money = int(input("you will enter the amount of money you have."))
priceApple = int(input("ask for the price of an apple."))

appleTotal = money // priceApple
change = money % appleTotal
print(f"You can buy {appleTotal} apples and our change is {change} pesos.")