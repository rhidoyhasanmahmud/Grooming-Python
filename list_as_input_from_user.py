n = input("Enter a text of numbers : ")  # 10 20 30 40
splitList = n.split()  # 10 20 30 40
result = 0

for num in splitList:
    result = result + int(num)

print(result)
