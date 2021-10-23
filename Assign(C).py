money = int(input("Amount of Money : "))
apple_price = int(input("Price of an apple : "))
Total = money // apple_price
a = Total * apple_price
Change = money - a
print(f"You can buy {Total} apples and your change is {Change:.2f} pesos.")