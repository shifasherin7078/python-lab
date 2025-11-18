result = []
for num in range(1000, 10000):
    if int(num**0.5)**2 == num:
        digits = str(num)
        if all(int(d)%2==0 for d in digits):
            result.append(num)
print(result)
