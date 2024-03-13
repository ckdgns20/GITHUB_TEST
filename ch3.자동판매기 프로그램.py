money=int(input("투입한 돈: "))
cost=int(input("물건값: "))
rest=money-cost
five=rest//500
one=(rest%500)//100

print("거스름돈:",rest)
print("500원 동전의 개수:",five)
print("100원 동전의 개수:",one)
