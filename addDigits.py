num = 381
res = 0
while True:   
    while(num>0):                
        res += num%10
        num //= 10
    if res<10:
        break
    else:
        num = res
        res = 0
print(res)