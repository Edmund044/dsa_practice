#GVSM
#marked
#stack or queue
#visited
#graph 

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set()
stack = []
def tso(visited,graph,node):
    for neighbour in graph[node]:
        if neighbour not in visited:
            tso(visited,graph,neighbour)

    if node not in visited:
        visited.add(node)
        print(node)
        stack.append(node)        

tso(visited,graph,'5')   
print(stack[::-1])     

