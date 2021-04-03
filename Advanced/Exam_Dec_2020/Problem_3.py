def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row in range(3, n + 1):
        triangle.append([1]*row)

    for r in range(len(triangle)):
        if len(triangle[r]) == 1:
            continue
        for c in range(len(triangle[r])):
            if c < len(triangle[r]) - 1:
                sum = triangle[r][c] + triangle[r][c+1]
                if r < len(triangle) - 1:
                    triangle[r+1][c+1] = sum

    return triangle


print(get_magic_triangle(7))
