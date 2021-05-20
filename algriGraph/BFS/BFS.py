from collections import deque

def createGraph(graph:dict):
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

def BFS(name):
    search_queue = deque()
    search_queue += graph[name]  # deque还能这样用？！
    searched = [] # 记录检查过的人
    # print(search_queue)
    while search_queue: # 只要队列不为空
        person = search_queue.popleft() # 取出第一个做判断
        if not person in searched: # 仅当这个人没检查过时才更新
            if person_is_seller(person): # 检查这个人是否是芒果经销商
                print(person+" is a mango seller!") # 是芒果经销商
                return True
            else:
                search_queue +=graph[person] # 如果不是芒果经销商,将这个人的朋友都加入到搜索队列
                searched.append(person) # 将这个人标记为检查过
    print("no one is a mango seller!")  # 没有人是芒果经销商
    return False

def person_is_seller(name):
    return name[-1] == 'm' # 人名以m结尾的是芒果经销商

if __name__ == '__main__':
    graph = {}
    createGraph(graph)
    BFS("you")
    # print(graph)






