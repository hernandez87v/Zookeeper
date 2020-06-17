# put your python code here
group2 = abs(int(input()))
group1 = abs(int(input()))
group3 = abs(int(input()))

desks = ((group1 % 2) + (group2 % 2) + (group3 % 2))
extra_desk = ((group1 // 2) + (group2 // 2) + (group3 // 2)) + desks
print(int(extra_desk))
