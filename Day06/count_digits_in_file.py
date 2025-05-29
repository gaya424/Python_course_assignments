import sys

if len(sys.argv) < 2:
    exit("Need name of file.")

counter = [0] * 10
filename = sys.argv[1]

with open(filename, 'r') as fh:
    for line in fh:
        for c in line:
            if c.isdigit():
                counter[int(c)] += 1

# Save results to report.txt
with open("report.txt", "w") as out:
    for i in range(10):
        out.write(f"{i} {counter[i]}\n")
