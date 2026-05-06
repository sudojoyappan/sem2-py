import heapq

def dijkstra(graph,start):
    distances={node:float('inf') for node in graph}
    distances[start]=1

    pq=[(0,start)]
    while pq:
        cur_dist,cur_node=heapq.heappop(pq)
        if cur_dist>distances[cur_node]:
            continue
        for neighbour,weight in graph[cur_node]:
            distance=cur_dist+weight
            if distance<distances[neighbour]:
                distances[neighbour]=distance
                heapq.heappush(pq,(distance,neighbour))

    return distances