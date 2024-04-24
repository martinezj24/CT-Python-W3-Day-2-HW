# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to

def both_airlines(our_routes, competitor_routes):
    same_dest = our_routes.intersection(competitor_routes)
    return same_dest
print(both_airlines(our_routes, competitor_routes))

# 2. Destinations unique to your airline
def only_ours(our_routes, competitor_routes):
    my_airline = our_routes.difference(competitor_routes)
    return my_airline
print(only_ours(our_routes, competitor_routes))

# 3. Whether there are any destinations that neither airline shares.
def neither_airlines(our_routes, competitor_routes):
    neither_dest = our_routes.symmetric_difference(competitor_routes)
    return neither_dest
print(neither_airlines(our_routes, competitor_routes))
