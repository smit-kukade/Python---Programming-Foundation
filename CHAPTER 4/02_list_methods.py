friends = ["Apple", "Orange",  345.86, False, "Aakash", "Rohan"]
print(friends)

friends.append("Smit") # Add at the end of the list
print(friends)

# String -> Immutable
# List -> Mutable

# friends.sort()
# print(friends)
# It will print an error because sort only works for an Integer

l1 = [1, 24, 62, 2, 6, 11]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3, 33333)
print(l1)

l1.pop()
print(l1)

l1.pop(3)
print(l1)
