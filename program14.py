start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

result = []

for i in range(start, end + 1):
    if 1000 <= i <= 9999:
        s = str(i)
        if all(int(d) % 2 == 0 for d in s):
            if int(i ** 0.5) ** 2 == i:
                result.append(i)

print(result)