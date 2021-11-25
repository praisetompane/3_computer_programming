x = 5
print(x > 2 and x < 10) # true, true
print(x > 5 and x < 10) # false, true
print(x > 5 or x < 10)  # false, true
print(x > 2 or x < 10)  # true, true
print(x > 2 or x < 4)   # true, false
print(x > 6 or x < 4)   # false, false
print(not x > 6 )       #false