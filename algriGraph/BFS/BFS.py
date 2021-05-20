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

def BFS():
    search_queue = deque()
    search_queue += graph["you"]  # deque还能这样用？！
    # print(search_queue)
    while search_queue: # 只要队列不为空
        person = search_queue.popleft() # 取出第一个做判断
        if person_is_seller(person): # 检查这个人是否是芒果经销商
            print(person+" is a mango seller!") # 是芒果经销商
            return True
        else:
            search_queue +=graph[person] # 如果不是芒果经销商,将这个人的朋友都加入到搜索队列
    print("no one is a mango seller!")  # 没有人是芒果经销商
    return False

def person_is_seller(name):
    return name[-1] == 'm' # 人名以m结尾的是芒果经销商

if __name__ == '__main__':
    graph = {}
    createGraph(graph)
    BFS()
    # print(graph)






