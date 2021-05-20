"""
使用散列表实现不重复的随机数
"""
import random

def createRand():
    """创建10个不重复的随机整数列表"""
    nums = {}
    while len(nums.keys())<10:
        num = random.randint(1,101)
        if nums.get(num) == None:
            nums[num] = 'yes'

    return list(nums.keys())


if __name__ == '__main__':
    ans = createRand()
    print(ans)
