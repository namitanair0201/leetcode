num = 1534236469
temp = str(abs(num))
rev = "".join(reversed(temp))
if int(rev) > 2**31-1:
    print(0)
elif num<0:
    print(int("-"+ rev ) )
else:
    print(int(rev))