from read import read_input
from Car import Car

R,C,F,N,B,T,rides = read_input()
cars = {}

#creation cars
for i in range(0,F-1):
    car = Car(0,0,0,0,i,0)
    cars[i] = car

print(cars)