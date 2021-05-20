"""
选择排序算法：
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
属于不稳定的排序算法。o(n^2)
"""

def findSmallest(arr:list):
    """找最小值并返回它的index"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """对数组进行排序"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == '__main__':
    ans = selectionSort([5,3,2,6,10])
    print(ans)
