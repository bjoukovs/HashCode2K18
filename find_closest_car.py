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

