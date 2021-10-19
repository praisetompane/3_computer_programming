values = [1,2,5,7,8,1,9,0,5,0]
#duplicates are 1,5 and 0
print(f'initial list {values}')

#O(NlogN)
values.sort()

#O(N)
for i in range(len(values)):
    adjacent = i+1
    if(adjacent < len(values) and values[i] == values[adjacent]):
        values.remove(values[i])
print(f'list without duplicates {values}')

# total complexity = O(NlogN + N)