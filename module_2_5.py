def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list1 = []
        for j in range(m):
            list1.append(value)
        matrix.append(list1)
    return matrix


result1 = get_matrix(3, 6, 666)
result2 = get_matrix(2, 4, 777)
print(result1)
print(result2)