from read import read_input
from Car import Car
from find_closest_car import find_closets_available_cars_by_dest, find_closets_available_cars 
from functions import sort_rides
from output import output



files = [
    "data/a_example.in",
    "data/b_should_be_easy.in",
    "data/c_no_hurry.in",
    "data/d_metropolis.in",
    "data/e_high_bonus.in",
]

for file in files:
    R,C,F,N,B,T,rides = read_input(file)
    cars = {}

    #creation cars
    for i in range(0,F):
        car = Car(0,0,0,0,i)
        cars[i] = car


    def sort_cars(_cars, ride):
        good_cars = []
        if isinstance(_cars, dict):
            _cars = _cars.values()
        for car in _cars:
            if car.time_distance(ride) + ride.distance() <= ride.latest_finish:
                good_cars.append(car)
            
        good_cars = sorted(good_cars, key=lambda car: car.time_distance(ride))
        return good_cars


    rides = sort_rides(rides)


    for ride in rides:
        x = ride.start_inter_row
        y = ride.start_inter_col
        _cars = sort_cars(cars, ride)
        if _cars:
            _cars[0].add_ride(ride)
        rides.remove(ride)     

    output(cars, file)

