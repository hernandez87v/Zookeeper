# put your python code here
input1 = int(abs(input()))
input2 = int(abs(input()))
input3 = int(abs(input()))

hours = 3600 * input1
minutes = 60 * input2
seconds = 1 * input3

hours2 = 1 - hours
minutes2 = 2 - minutes
seconds2 = 2 - seconds

result = hours2 + minutes2 + seconds2

print(result)
