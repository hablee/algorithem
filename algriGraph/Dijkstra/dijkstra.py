
# 创建图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# print(graph["start"].keys())
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # 终点没有任何邻居

# 创建开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 创建父节点散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 记录处理过的节点
processed = []


node = find_lowest_cost_node(costs) # 在未处理的节点中找出开销最小的节点
while node is not None: # 这个while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # 如果经当前节点前往该邻居更近
            costs[n] = new_cost # 就更新该邻居的开销
            parents[n] = node # 同时将该邻居的父节点设置为当前节点
    processed.append(node)
    node = find_lowest_cost_node(costs) # 找出接下来要处理的节点


