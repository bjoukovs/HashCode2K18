class Car:

    def __init__(self,xpos,ypos,xdest,ydest,nb,current_ride_index): #nb=number of the car
        self.xpos = xpos
        self.ypos = ypos
        self.xdest=xdest
        self.ydest=ydest
        self.nb=nb
        self.current_ride_index=current_ride_index #indice de la course en cours
        self.rides=[]

    def moveto_x(self):
        self.xpos=xdest
        elapsed_time=0
        elapsed_time = elapsed_time + abs(xdest-xpos)
        self.ypos=ydest
        elapsed_time = elapsed_time + abs(ydest-ypos)

        return elapsed_time

    def add_ride(self):
        self.rides.append(current_ride_index)
