def sort_rides(rides_ls):
    """sorted_ls=[] #liste finale
    sublist=[]
    ref_time=0
    for i in range len(rides_ls):
        start=rides_ls[i].earliest_start
        if start<=ref_time:
            sublist.append(rides_ls[i])

    for j in range len(sublist)
    """

    rides_ls = sorted(rides_ls.values(), key=lambda ride: ride.earliest_start)
    return rides_ls
