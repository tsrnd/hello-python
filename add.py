# def add(a, b):
#     result = []
#     for i, j in zip(a, b):
#         tmp = []
#         for k, l in zip(i, j):
#             tmp.append(k+l)
#         result.append(tmp)
#     return result


def add(a, b):
    """Add corresponding numbers in given 2-D matrices."""
    result = []
    for i, j in zip(a, b):
        tmp = [
            k + l
            for k, l in zip(i, j)
        ]
        result.append(tmp)
    return result

m1 = [[6, 6], [3, 1]]
m2 = [[1, 2], [3, 4], [5, 6]]
# m3 = [[6, 6], [3, 1, 2]]
print(add(m1, m2))
