def sort_rides(rides_ls):
    # Sort rides with the earliest start first
    rides = {}
    # Start time => rides
    for ride in rides_ls.values():
        earliest_start = ride.earliest_start
        if rides.get(earliest_start):
            rides[earliest_start].append(ride)
        else:
            rides[earliest_start] = [ride]

    for earliest_start in rides:
        rides[earliest_start] = sorted(rides[earliest_start], 
                                        key=lambda ride: ride.points())
    return rides
