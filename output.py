import datetime

def output(cars):
    today = datetime.date.today()
    input = open("output/out"+str(today)+".in", "w")
    
    for key,c in cars.items():
        line = ""
        r = c.rides
        if len(r)>0:
            line = str(len(r))
            for ride in r:
                line += " "+str(ride.id)
        line+="\n"
        input.write(line)


    input.close()