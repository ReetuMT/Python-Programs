# Prime Numbers

for n in range(2,20):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)

# Prime or Not
num = 10
for a in range(2,num):
    if num%a == 0:
        print("Not Prime Number")
        break
else:
    print("Prime number")