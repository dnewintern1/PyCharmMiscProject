# def sol(matrix):
#
#     result = []
#     for i in range(len(matrix)):
#
#         for j in range(len(matrix)):
#
#             if i ==0:
#                 result.append(matrix[0][j])
#
#             if i>=1:
#                 result.append(matrix[i][-1])
#
#                 if i==len(matrix)-1:
#                     result.append(matrix[i][-2])
#                     result.append(matrix[i][-3])
#                     result.append(matrix[i][-4])
#
#                     result.append(matrix[2][0])
#                     result.append(matrix[1][0])
#                     result.append(matrix[1][1])
#                     result.append(matrix[1][2])
#
#                     result.append(matrix[2][2])
#                     result.append(matrix[2][1])
#
#                 break
#     return print(result)

def sol(matrix):
    result = []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while left <= right and top <= bottom:

        # left → right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # top → bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # right → left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # bottom → top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(sol(matrix))
