f = open("day1_input.txt", "r")
arr = []
for d in f:
    arr.append(int(d))

# Puzzle 1
largest = 0
for x in arr:
    for y in arr:
        if x + y == 2020:
            print(x, y)
            if x * y > largest:
                largest = x * y
print(largest)


# Puzzle 2
largest = 0
for x in arr:
    for y in arr:
        for d in arr:
            if x + y + d == 2020:
                if x * y * d > largest:
                    largest = x * y * d
print(largest)
