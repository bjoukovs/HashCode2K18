class Car:

    def __init__(self,xpos,ypos,xdest,ydest,car_id): #car_id=number of the car
        self.time_available = 0
        self.xpos = xpos
        self.ypos = ypos
        self.xdest = xdest
        self.ydest = ydest
        self.car_id = car_id
        self.available = True #indice de la course en cours
        self.rides = []
        self.elapsed_time = 0
        self.next_ride = None
        self.moving_towards_ride = False

    def add_ride(self, ride):

        expected_time = abs(self.xpos - ride.start_inter_row)
        expected_time += abs(self.ypos - ride.start_inter_col)
        if self.time_available + expected_time <= ride.earliest_start:
            self.time_available = ride.earliest_start
        else:
            self.time_available += expected_time

        expected_time = abs(ride.start_inter_row - ride.end_inter_row)
        expected_time += abs(ride.start_inter_col - ride.end_inter_col)
        self.time_available += expected_time
        self.rides.append(ride)

    def compute_time(self):
        if self.available:
            expected_time = -1
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


    def time_distance(self, ride):
        expected_time = self.time_available
        expected_time += abs(self.xpos - ride.start_inter_row)
        expected_time += abs(self.ypos - ride.start_inter_col)
        return expected_time