# Push and Pop

books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)  # ['Learn C', 'Learn C++', 'Learn Java']

books.pop()
print("Now the top book is : ", books[-1])  # Now the top book is :  Learn C++
print(books)  # ['Learn C', 'Learn C++']


