def sort_rides(rides_ls):
    # Sort rides with the earliest start first
    return sorted(rides_ls, key=lambda ride: ride.earliest_start)
