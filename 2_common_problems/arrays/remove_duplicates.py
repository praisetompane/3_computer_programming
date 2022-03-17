values = [1,2,5,7,8,1,9,0,5,0]

def remove_duplicates(values):
    #duplicates are 1,5 and 0
    print(f'initial list {values}')

    #O(NlogN)
    values.sort()

    #O(N)
    for i in range(len(values)):
        adjacent = i+1
        if(adjacent < len(values) and values[i] == values[adjacent]):
            #O(N), need to search the whole list for the value, then shift elements. decreases over time, but effectively N
            values.remove(values[i])
    print(f'list without duplicates {values}')

    # total complexity = O(NlogN + (N * N)) = O(NlogN + N²) = O(N²)

def remove_duplicates_v2(values):
    print(f'initial list {values}')
    uniques = []
    #O(N)
    for v in values:
        #O(L) = L is size of unque list, which is <= N, increases over time to get close to N
        if v not in uniques:
            uniques.append(v)
    print(f'list without duplicates {uniques}')
    #total complexity = O(N * L) => In the range between O(N) and O(N²)

remove_duplicates(values[:])
remove_duplicates_v2(values[:])