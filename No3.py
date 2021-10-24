enterMoney = int(input("you will enter the amount of money you have."))
priceApple = int(input("ask for the price of an apple."))

maximumApple = int(input("maximum number of apples that you can buy."))

appleTotal = priceApple * maximumApple
moneyLeft = enterMoney - appleTotal
print(f"You can buy {maximumApple} apples and our change is {moneyLeft} pesos.")