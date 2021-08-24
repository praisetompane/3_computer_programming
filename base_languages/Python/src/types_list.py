letters = ["a", "b", "c", "d", "person"]

print("exploration")
print(letters)
print(letters[0])
print(letters[-1])
print(letters[-2])
print(letters[-5])
print(letters[0:3]) # excludes end index
print("a" in letters)
print(len(letters))

for i in letters:
    print(i)

print("mutations")
letters[4] = "e"
print(letters)

letters.append("g")
print(letters)

letters.insert(5, "f")
print(letters)

letters.remove("a")
print(letters)

letters.clear()
print(letters)

