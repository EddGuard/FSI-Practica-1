# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
at = search.GPSProblem('A', 'T', search.romania)
ar = search.GPSProblem('A', 'R', search.romania)
aS = search.GPSProblem('A', 'S', search.romania)

#print search.breadth_first_graph_search(ab).path()
#print search.depth_first_graph_search(ab).path()

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

print("\nBusqueda por ramificacion y acotacion\n")
print(search.search_ramification(ab).path())
print("Ruta A -> B")
print(search.search_ramification(at).path())
print("Ruta A -> T")
print(search.search_ramification(ar).path())
print("Ruta A -> R")
print(search.search_ramification(aS).path())
print("Ruta A -> S")

print('\nBusqueda Informada\n')
print(search.search_heuristic(ab).path())
print("Ruta A -> B")
print(search.search_heuristic(at).path())
print("Ruta A -> T")
print(search.search_heuristic(ar).path())
print("Ruta A -> R")
print(search.search_heuristic(aS).path())
print("Ruta A -> S")



#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
