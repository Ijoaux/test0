import random
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print(random.choices(x,k = 10))
t = ""
a = int(input("masukan panjang pasword:"))
for i in range(a):
    y = random.choice(x)
    t = t + y
    
    
print(t)