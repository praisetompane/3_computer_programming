'''
    end value is excluded
'''
print("default start of 0")
numbers = range(5) # start at 0[default] exlude 5
for n in numbers:
    print(n)

print("start and end set")
numbers = range(5, 10)
for n in numbers:
    print(n)

print("start, end and step set")
numbers = range(5, 10, 2)
for n in numbers:
    print(n)