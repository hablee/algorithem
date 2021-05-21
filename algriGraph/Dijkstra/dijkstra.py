
# 创建图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 1
graph["start"]["b"] = 2
# print(graph["start"].keys())

graph["a"] = {}
graph["a"]["end"] = 5
graph["a"]["c"] = 2

graph["b"] = {}
graph["b"]["c"] = 3

graph["c"] = {}
graph["c"]["end"] = 2

graph["end"] = {} # 终点没有任何邻居

# 创建开销表
infinity = float("inf")
costs = {}
costs["a"] = 1
costs["b"] = 2
costs["c"] = infinity
costs["end"] = infinity # 不确定一律设为infinity

# 创建父节点散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["end"] = None # 不确定一律设为None

# 记录处理过的节点
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低且没有被处理过
            lowest_cost = cost # 将其设为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node

path = []
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

"""从后向前,将父节点添加到path中"""
node = "end"
path = []
while node != 'start':
    path.append(node)
    node = parents[node]

"""打印路径"""
path.append("start")
for i in range(len(path)):
    node = path.pop()
    print(node,end='->' if (node!='end') else "")
