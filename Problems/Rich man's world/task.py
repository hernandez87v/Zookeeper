deposit = int(input())
year = 0
while deposit < 700000:
    deposit += deposit * 0.071
    year += 1
print(year)
