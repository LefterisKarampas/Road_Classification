import math

#From https://gist.github.com/rochacbruno/2883505

def Harvesine(origin, destination):
    t1, lat1, lon1 = origin
    t2, lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


def Compare_Harvesine(origin,destination):
    return (Harvesine(origin,destination) < 0.2)