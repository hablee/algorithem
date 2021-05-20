"""
快速排序算法：
在待排序的数列中，我们首先要找一个数字作为基准数（这只是个专用名词）。为了方便，我们一般选择第 1 个数字作为基准数
（其实选择第几个并没有关系。其实有关系）。接下来我们需要把这个待排序的数列中小于基准数的元素移动到待排序的数列的左边，
把大于基准数的元素移动到待排序的数列的右边。这时，左右两个分区的元素就相对有序了；
接着把两个分区的元素分别按照上面两种方法继续对每个分区找出基准数，然后移动，直到各个分区只有一个数时为止。
属于不稳定排序算法。o(nlogn)
"""

def quicksort(array):
    """快速排序"""
    if len(array)<2:
        return array # 基线条件
    else:
        pivot = array[0] # 递归条件
        less = [i for i in array[1:] if i<=pivot] # 由所有小于基准值的元素组成的数组
        greater = [i for i in array[1:] if i>pivot] # 由所有大于基准值的元素组成的数组

        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    ans = quicksort([10,5,2,3])
    print(ans)
