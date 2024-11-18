def planting_plan(rows):
    return [(x * 2) for x in range(1, rows + 1)]


print(planting_plan(5))