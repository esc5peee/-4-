a=int(input("Введите процент:"))
n=int(input("Введите количество дней:"))
k=int(input("Введите курс валюты:"))
for i in range(n+1):
    print(k*((1+a/100)**i))
