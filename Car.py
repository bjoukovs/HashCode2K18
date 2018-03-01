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
        self.next_ride = None
        self.moving_towards_ride = False

    def move(self):
        if self.moving_towards_ride:
            ydest = self.next_ride.end_inter_col
            xdest = self.next_ride.end_inter_row
        else:
            xdest = self.xdest
            ydest = self.ydest
        
        if self.xpos != xdest:
            if self.xpos > xdest:
                self.xpos -= 1 
            else:
                self.xpos += 1
        elif self.ypos != ydest:
            if self.ypos > ydest:
                self.ypos -= 1
            else:
                self.ypos += 1
        else:
            if not self.moving_towards_ride:
                self.available = True
            else:
                self.moving_towards_ride = False
                self.rides.append(self.next_ride)
                self.xdest = self.next_ride.end_inter_row
                self.ydest = self.next_ride.end_inter_col
                self.next_ride = None

    def add_ride(self, ride):
        if self.xpos == ride.start_inter_row and self.ypos == ride.start_inter_col:
            self.moving_towards_ride = False
            self.rides.append(ride)
            self.xdest = ride.end_inter_row
            self.ydest = ride.end_inter_col
        else:
            self.moving_towards_ride = True
            self.next_ride = ride
        self.available = False

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
        expected_time = 0
        if not self.available:
            expected_time += abs(self.xdest - self.xpos)
            expected_time += abs(self.ydest - self.ypos)
        expected_time += abs(self.xdest - ride.start_inter_row)
        expected_time += abs(self.ydest - ride.start_inter_col)
        return expected_time