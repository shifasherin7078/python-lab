

source = "input.txt"
destination = "output.txt"

with open(source, "r") as f1, open(destination, "w") as f2:
    lines = f1.readlines()
    for i in range(len(lines)):
        if (i + 1) % 2 != 0:
            f2.write(lines[i])