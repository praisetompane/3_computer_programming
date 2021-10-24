''' 
    Context:
        Given:
            array of n distinct integers
        
        Objective:
            transform array
                into ziug zag sequence
                    by permuting the its elements
            find the lexicographically 
                smallest
                    zig zag sequence
        Definitions:
            zig-zag sequence = if first k elements
                                    increasing in order
                                last k elements
                                    decreasing in order
                                where k = (n + 1)/2
        Example:
            a = [2, 3, 5, 1, 4]
            [1, 2, 3, 4, 5]
            permuted_a = [1, 4, 5, 3, 2]: zig zag sequence
            
        Contraints:
            code base:  max 3 lines source code changes
                        no code addition or removal
'''
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    # swap array values between mid point and end index [exclusive of both]
    # you want them in descending order
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
