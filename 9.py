a=int(input("Введите цену:"))
b=int(input("Введите скидку:"))
c=int(input("Введите количество товаров:"))
d=int(input("Введите колличество денег:"))
f=0
s=0
for i in range(1,c+1):
    f=(a-(a*(b*i)/100))
    s+=f
    if s>0:
        print(d-s)