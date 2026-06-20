req = int(input("Enter requirement: "))
cans_in_liters = [10, 5, 2, 1]

total_cans = 0

for can in cans_in_liters:
    count = req // can
    total_cans += count
    req %= can

print("Minimum cans required:", total_cans)