# Read input
n_temp = input().strip()

# Convert to integer
n = int(n_temp)

# Print multiplication table
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
