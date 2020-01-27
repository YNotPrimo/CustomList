from custom_list import CustomList

a = CustomList(1, 2, 3, 4)
print(a)  # [1, 2, 3, 4]
print(a.append(5))  # [1, 2, 3, 4, 5]

print(a.remove(1))  # 2
print(a)  # [1, 3, 4, 5]

print(a.get(2))  # 4
print(a.extend(6, 7, 8))  # [1, 3, 4, 5, 6, 7, 8]
print(a.insert(2, 10))  # [1, 3, 10, 4, 5, 6, 7, 8]

print(a.pop())  # 8
print(a)  # [1, 3, 10, 4, 5, 6, 7]

print(a.index(6))  # 5
print(a.count(1))  # 1

print(a.reverse())  # [7, 6, 5, 4, 10, 3, 1]
print(a.copy())  # [1, 3, 10, 4, 5, 6, 7]

print(a.add_first(6))  # [6, 1, 3, 10, 4, 5, 6, 7]
print(a.dictionize())  # {6: 1, 3: 10, 4: 5}
print(a.move(4))  # [4, 5, 6, 7, 6, 1, 3, 10]
print(a.sum())  # 42

print(a.overbound())  # 10
print(a.underbound())  # 1

print(a.clear())  # []

print(list.__str__([]))
