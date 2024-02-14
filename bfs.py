import queue
# BFS Psuedocode 

# marked = [False] * G.size()
# def bfs(G,v):
#     queue = [v]
#     while len(queue) > 0:
#         v = queue.pop(0)
#         if not marked[v]:
#             visit(v)
#             marked[v] = True
#             for w in G.neighbos(v):
#                 if not marked[w]:
#                     queue.append(w)

graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

# BFS Function
def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end= "")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

# visited = {}
# level = {} # distance dict
# parent = {}
# bfs_traversal_output = []
# queue = queue.Queue()

# for node in graph.keys():
#     visited[node] = False
#     parent[node] = None
#     level[node] = -1

# s = '5'
# visited[s] = True
# level[s] = 0
# queue.put(s)

# while not queue.empty():
#     u = queue.get()
#     bfs_traversal_output.append(u)

#     for v in graph[u]:
#         if not visited[v]:
#             visited[v] = True
#             parent[v] = u
#             level[v] = level[u]+1
#             queue.put(v)

# print(bfs_traversal_output)
# # shortest distance of node to source node
# print(level['8'])

# # shortest path to any node from source node
# v = "8"
# path = []

# while v is not None:
#     path.append(v)
#     v = parent[v]

# path.reverse()
# print(path)

# Depth First Search 

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')