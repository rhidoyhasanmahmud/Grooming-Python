num = {1, 2, 3, 4, 5}
print(num)  # {1, 2, 3, 4, 5}
num2 = set([4, 5, 6, 7, 7])
print(num2)  # {4,5,6,7,7}
# num2.add(7)
# num2.remove(1)
print(7 in num2)  # True
print(5 not in num2)  # False

print(num | num2)  # {1, 2, 3, 4, 5, 6, 7}
print(num & num2)  # {4, 5}
print(num - num2)  # {1, 2, 3}
