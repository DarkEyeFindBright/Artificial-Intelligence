# Data Structure for Graph
graph = {
    0: [1, 4],
    1: [2, 3],
    2: [1],
    3: [1],
    4: [5, 6],
    5: [4],
    6: [4]
}


# BFS
def BFS(graph, s):  # s is the start node
    # queue for OPEN list
    queue = [s]
    # hash set for CLOSED list
    seen = set()
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)  # Pop the first node in the queue
        nodes = graph[vertex]  # store child nodes
        for w in nodes:
            if w not in seen:  # Is visited or not
                queue.append(w)  # If not, append the node into queue
                seen.add(w)
        print(vertex)


# DFS
def DFS(graph, s):  # s is the start node
    # stack for OPEN list
    stack = [s]
    seen = set()  # hash set for CLOSED list
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()  # Pop the first node in the stack
        nodes = graph[vertex]  # store child nodes
        for w in nodes:
            if w not in seen:  # Is the node visited or not
                stack.append(w)  # If not, push into stack
                seen.add(w)
        print(vertex)


BFS(graph, 0)
DFS(graph, 0)
