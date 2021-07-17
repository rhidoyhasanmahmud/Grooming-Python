subjects = ["C", "C++", "Java", "Python", "Android", "OS", "TOC"]

print(subjects)  # ['C', 'C++', 'Java', 'Python', 'Android', 'OS', 'TOC']
print(subjects[2])  # Java
print(subjects[2:])  # ['Java', 'Python', 'Android', 'OS', 'TOC']
print(subjects[-1])  # TOC

print("Python" in subjects)  # True
print("Java" not in subjects)  # False

print(subjects + ["Swift", 27])  # ['C', 'C++', 'Java', 'Python', 'Android', 'OS', 'TOC', 'Swift', 27]
print(subjects * 2)
# ['C', 'C++', 'Java', 'Python', 'Android', 'OS', 'TOC', 'C', 'C++', 'Java', 'Python', 'Android', 'OS', 'TOC']

print(len(subjects))  # 7
subjects.append("BASIC")
print(subjects)  # ['C', 'C++', 'Java', 'Python', 'Android', 'OS', 'TOC', 'BASIC']

subjects.insert(2, "PHP")
print(subjects)  # ['C', 'C++', 'PHP', 'Java', 'Python', 'Android', 'OS', 'TOC', 'BASIC']

subjects.remove("TOC")
print(subjects)  # ['C', 'C++', 'PHP', 'Java', 'Python', 'Android', 'OS', 'BASIC']

subjects.sort()
print(subjects)  # ['Android', 'BASIC', 'C', 'C++', 'Java', 'OS', 'PHP', 'Python']

subjects.reverse()
print(subjects)  # ['Python', 'PHP', 'OS', 'Java', 'C++', 'C', 'BASIC', 'Android']

subjects.pop()
print(subjects)  # ['Python', 'PHP', 'OS', 'Java', 'C++', 'C', 'BASIC']

subjects2 = subjects.copy()
print(subjects2)  # ['Python', 'PHP', 'OS', 'Java', 'C++', 'C', 'BASIC']

print(subjects)  # ['Python', 'PHP', 'OS', 'Java', 'C++', 'C', 'BASIC']
print(subjects.index("Python"))  # 0
print(subjects.count("Python"))  # 1
