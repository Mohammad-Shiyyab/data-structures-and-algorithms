from graph.graph import Graph


def graph_business_trip(graph, cities):
    cost = 0
    for i in range(len(cities) - 1):
        curr_vertex = graph.add_vertex(cities[i])
        dist_vertex = graph.add_vertex(cities[i+1])
        if not curr_vertex or not dist_vertex:
            return None

        trip_cost = get_weight(graph, curr_vertex, dist_vertex)
        if trip_cost is None:
            return None
        cost += trip_cost

    return cost


def get_weight(graph, curr_vertex, dist_vertex):
    neighbors = graph.get_neighbors(curr_vertex)

    for neighbor in neighbors:
        if neighbor.vertex == dist_vertex:
            return neighbor.weight