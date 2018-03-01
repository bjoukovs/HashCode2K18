from ride import Ride

def read_input():

    input = open("data/b_should_be_easy.in", "r")
    content = input.readlines()
    input.close()

    #first line
    elems = content[0].strip().split(" ")
    #print(elems)
    R = int(elems[0])
    C = int(elems[1])
    F = int(elems[2])
    N = int(elems[3])
    B = int(elems[4])
    T = int(elems[5])

    print(R,C,F,N,B,T)

    rides = {}

    #read lines
    for i in range(1,len(content)-1):
        line = content[i].strip().split(" ")
        num = i-1
        x0 = int(line[0])
        y0 = int(line[1])
        x1 = int(line[2])
        y1 = int(line[3])
        es = int(line[4])
        lf = int(line[5])

        ride = Ride(x0,y0,x1,y1,es,lf,num)
        rides[num] = ride

    return(R,C,F,N,B,T,rides)

read_input()
