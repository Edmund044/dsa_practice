#GVSM
#marked
#stack or queue
#visited
#graph 



# Using a Python dictionary to act as an adjacency list
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

def dfs(visited,node,graph):
    visited = set()
    stack = []
    if node not in visited:
            visited.append(node)
            stack.append(node)
            for neighbour in graph[node]
                dfs(visited,node,graph)




# visited = set() # Set to keep track of visited nodes of graph.
# stack  = []
# def dfs(visited, graph, node):  #function for dfs 
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         stack.append(node)
#         for neighbour in graph[node]:
            dfs(visited, graph, neighbour)        

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
print(stack)
print(visited)

# graph = {
#    5 : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

# def dfs(graph,node,visited):
#     visited = []
#     stack = []
#     if node not in visited:
#         visited.append(node)
#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                 stack.append(neighbour)


    # visited = []
    # if node not in visited:
    #     visited.append(node)
    #     for neighbour in graph[node]:
    #         if neighbour not in visited:
    #             dfs(graph,neighbour)


# print(dfs(graph,5))
        




# Using a Python dictionary to act as an adjacency list
# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

# visited = set() # Set to keep track of visited nodes of graph.

# def dfs(visited, graph, node):  #function for dfs 
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# # Driver Code
# print("Following is the Depth-First Search")
# dfs(visited, graph, '5')
