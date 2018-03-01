class Car:

    def __init__(self,xpos,ypos,xdest,ydest,car_id): #car_id=number of the car
        self.xpos = xpos
        self.ypos = ypos
        self.xdest = xdest
        self.ydest = ydest
        self.car_id = car_id
        self.available = True #indice de la course en cours
        self.rides = []
        self.elapsed_time = 0
        self.moving_towards_ride = False

    def move(self):
        if self.moving_towards_ride:
            ride = self.rides[-1]
            ydest = ride.end_inter_col
            xdest = ride.end_inter_row
        else:
            xdest = self.xdest
            ydest = self.ydest
        
        if self.xpos != xdest:
            self.xpos += 1 
        elif self.ypos != ydest:
            self.ypos += 1
        else:
            if not self.moving_towards_ride:
                self.available = True
            else:
                self.moving_towards_ride = False

    def add_ride(self, ride):
        if self.xpos == ride.start_inter_row and self.ypos == ride.start_inter_col:
            self.moving_towards_ride = False
        else:
            self.moving_towards_ride = True
        self.available = False
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
