f = open("day2_input.txt", "r")
arr = []
for d in f:
    arr.append(d.replace("\n", ""))

# Puzzle 1
valid = 0
for x in arr:
    num, letter, password = x.split(" ")
    num_low, num_high = num.split("-")
    letter = letter[:-1]
    count = password.count(letter)
    if count >= int(num_low) and count <= int(num_high):
        valid += 1
print(valid)


# Puzzle 2
valid = 0
for x in arr:
    num, letter, password = x.split(" ")
    num_low, num_high = num.split("-")
    letter = letter[:-1]
    if password[int(num_low) - 1] == letter and password[int(num_high) - 1] != letter:
        valid += 1
    if password[int(num_low) - 1] != letter and password[int(num_high) - 1] == letter:
        valid += 1
print(valid)
