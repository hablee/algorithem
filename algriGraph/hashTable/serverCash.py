"""
大型网站的缓存就用散列表存储
"""

def get_data_from_server(url):
    """假设这是获取server数据的函数"""
    pass

cache = {}
def get_page(url):
    if cache.get(url):
        return cache(url)
    else:
        data = get_data_from_server(url)
        cache[url] = data # 先将数据保存到缓存中
        return data

