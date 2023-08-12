# Class 35 - Graphs

## Challenge

Create a Graph class that has the following methods:

- add_vertex

   - Adds a new node to the graph
   - Takes in the value of that node
   - Returns the added node

- add_edge

   - Adds a new edge between two nodes in the graph
   - Include the ability to have a “weight”
   - Takes in the two nodes to be connected by the edge
   - Both nodes should already be in the Graph

- get_vertices

   - Returns all of the nodes in the graph as a collection (set, list, or similar)

- get_neighbors

   - Returns a collection of edges connected to the given node
   - Takes in a given node
   - Include the weight of the connection in the returned collection

- size

   - Returns the total number of nodes in the graph


## code

- <a href="#graph.py">Graph</a>

## test

    pytest -k graph


test file: <a href="#test_graph.py">test_graph</a>

