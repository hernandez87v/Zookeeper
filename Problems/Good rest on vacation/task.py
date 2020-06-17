# put your python code here
duration_days = int(input())
total_food_cost = int(input())
flight_cost = int(input())
one_night_hotel = int(input())

print((one_night_hotel * (duration_days - 1)) + (duration_days * total_food_cost + (flight_cost * 2)))
