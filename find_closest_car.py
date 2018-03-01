def dist(x0,y0,x1,y1):
    return abs(x1-x0)+abs(y1-y0)

#Closest cars at current instant
def find_closest_cars(cars,x,y):
    min_dist = -1
    best_cars = []

    for key,c in cars.items():
        xc = c.xpos
        yc = c.ypos
        dist = abs(xc-x)+abs(yc-y)
        if min_dist == -1:
            best_cars.append(c)
            min_dist = dist

        else:
            if min_dist>dist:
                best_cars = [c]
                min_dist = dist

            elif min_dist == dist:
                best_cars.append(c)
        
    return best_cars

#Closest cars by their destinations
def find_closest_cars_by_dest(cars,x,y):
    min_dist = -1
    best_cars = []

    for key,c in cars.items():
        xc = c.xdest
        yc = c.ydest
        dist = abs(xc-x)+abs(yc-y)
        if min_dist == -1:
            best_cars.append(c)
            min_dist = dist

        else:
            if min_dist>dist:
                best_cars = [c]
                min_dist = dist

            elif min_dist == dist:
                best_cars.append(c)
        
    return best_cars

def find_closets_available_cars(cars,x,y,t0):
    best_cars = find_closest_cars(cars,x,y)
    #best_cars = find_closest_cars_by_dest(cars,x,y)
    #print(best_cars)
    already_available = False
    best_best_cars = []

    for i in range(0,len(best_cars)):
        c = best_cars[i]

        if already_available==True:
            if c.compute_time()==-1:
                best_best_cars.append(c)

        else:
            if c.compute_time() == -1:
                already_available = True
                best_best_cars.append(c)
            else:
                ttd = c.compute_time()

                if len(best_best_cars)==0:
                    if ttd==-1:
                        best_best_cars = [c]
                elif ttd < best_best_cars[0].compute_time():
                    best_best_cars = [c]
                elif ttd == best_best_cars[0]:
                    best_best_cars.append(c)
    
    return best_best_cars



def find_closets_available_cars_by_dest(cars,x,y,t0):
    #best_cars = find_closest_cars_by_dest(cars,x,y)
    best_cars = find_closest_cars_by_dest(cars,x,y)
    #print(best_cars)
    already_available = False
    best_best_cars = []

    for i in range(0,len(best_cars)):
        c = best_cars[i]

        if already_available==True:
            if c.compute_time()==-1:
                best_best_cars.append(c)

        else:
            if c.compute_time() == -1:
                already_available = True
                best_best_cars.append(c)
            else:
                ttd_delay = c.compute_time()+dist(x,y,c.xdest,c.ydest)

                if len(best_best_cars)==0:
                    if ttd_delay==-1:
                        best_best_cars = [c]
                elif ttd_delay < best_best_cars[0].compute_time():
                    best_best_cars = [c]
                elif ttd_delay == best_best_cars[0]:
                    best_best_cars.append(c)
    
    return best_best_cars