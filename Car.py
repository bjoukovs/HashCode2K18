class Car:

    def __init__(self,xpos,ypos,xdest,ydest,car_id,ride_id): #car_id=number of the car
        self.xpos = xpos
        self.ypos = ypos
        self.xdest = xdest
        self.ydest = ydest
        self.car_id = car_id
        self.ride_id = ride_id #indice de la course en cours
        self.rides = []

    def moveto_x(self):
        elapsed_time = abs(self.xdest - self.xpos)
        elapsed_time += abs(self.ydest - self.ypos)
        self.xpos = self.xdest
        self.ypos = self.ydest
        return elapsed_time

    def add_ride(self):
        self.rides.append(self.id)

    def compute_time(self):
        if self.ride_id==-1:
            expected_time=-1
        else:
            expected_time = abs(self.xdest - self.xpos)
            expected_time += abs(self.ydest - self.ypos)
        return expected_time


    def __repr__(self):
        return "Car id {} at ({}, {}) going to ({}, {})".format(self.car_id,
                                                                self.xpos,
                                                                self.ypos,
                                                                self.xdest,
                                                                self.ydest)
