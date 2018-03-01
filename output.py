import datetime
import os

def output(cars, file):
    today = datetime.date.today()
    basename = os.path.basename(file)
    input = open("output/" + file, "w")
    for key, c in cars.items():
        line = ""
        r = c.rides
        if len(r)>0:
            line = str(len(r))
            for ride in r:
                line += " "+str(ride.id)
        line+="\n"
        input.write(line)

    input.close()