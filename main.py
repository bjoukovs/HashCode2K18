from read import read_input
from Car import Car
from find_closest_car import find_closets_available_cars
from functions import sort_rides

R,C,F,N,B,T,rides = read_input()
cars = {}

#creation cars
for i in range(0,F):
    car = Car(0,0,0,0,i)
    cars[i] = car


temps = 0
rides = sort_rides(rides)
for earliest_start, _rides in rides.items():
    for ride in _rides:
        x = ride.start_inter_row
        y = ride.start_inter_col
        t0 = earliest_start
        #print(x,y,t0)
        av_cars = find_closets_available_cars(cars, x, y, t0)
        if av_cars:
            car = av_cars[0]
            car.add_ride(ride)
            print(car, ride)

