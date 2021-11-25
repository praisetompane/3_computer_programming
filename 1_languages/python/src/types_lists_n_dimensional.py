matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [4, 8, 12]
]

for row in matrix:
    for item in row:
        print(item, end='')
    print('')
print()

print('comma separated matrix')
for row in matrix:
    print(",".join([str(item) for item in row]))
print()

print('scaled by 2')
dimension = len(matrix[0])
scalar = 2
for row in range(dimension):
    for col in range(dimension):
        matrix[row][col] = matrix[row][col] * scalar

for row in matrix:
    print(",".join([str(item) for item in row]))
print()

depth_three_list= [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
]

print(depth_three_list[0][2][2])
