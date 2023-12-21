def shoelace_formula(coordinates):
    result = 0
    coordinates.append(coordinates[0])
    n = len(coordinates)

    for i in range(n-1):
        result += coordinates[i][0] * coordinates[i+1][1] - coordinates[i+1][0] * coordinates[i][1]

    return abs(result / 2)