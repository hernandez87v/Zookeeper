# put your python code here
hours = abs(int(input()))
minutes = abs(int(input()))
seconds = abs(int(input()))

hours2 = abs(int(input())) - hours
minutes2 = abs(int(input())) - minutes
seconds2 = abs(int(input())) - seconds

hours_seconds = 3600 * hours2
minutes_seconds = 60 * minutes2
seconds_seconds = 1 * seconds2

result = hours_seconds + minutes_seconds + seconds_seconds

print(result)
