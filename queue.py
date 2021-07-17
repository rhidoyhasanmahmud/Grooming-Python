from collections import deque

bank = deque(["Hasan", "Mahmud", "Nisha"])
print(bank)  # deque(['Hasan', 'Mahmud', 'Nisha'])
bank.popleft()
print(bank)  # deque(['Mahmud', 'Nisha'])
bank.popleft()
bank.popleft()

if not bank:
    print("No Person Left")



