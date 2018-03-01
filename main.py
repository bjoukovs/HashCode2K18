from read import read_input
from Car import Car
from find_closest_car import find_closest_car

R,C,F,N,B,T,rides = read_input()
cars = {}

#creation cars
for i in range(0,F-1):
    car = Car(0,0,0,0,i,-1)
    cars[i] = car

print(cars)

#print(find_closest_car(cars,10,10))