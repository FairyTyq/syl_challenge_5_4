# coding:utf-8

# 使用 csv 模块来保存文件
import csv
# 使用 asyncion 库来实现异步编程
import asyncio
# 使用 aiohttp 库实现网络请求
import aiohttp
# 设置异步编程中的超时
import async_timeout
# 使用 scrapy 中的 HtmlResponse 构建并且解析页面内容
from scrapy.http import HtmlResponse

# 输出的结果保存到 result 列表中，每个元素都是一个二元组(name,update_time)
results = []

# 定义获取网页内容的异步操作，注意定义的方式
async def fetch(session,url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

# 定义提取网页数据的函数
def parse(url,body):
    # 1. 构建 HtmlResponse 对象
    response = HtmlResponse(url=url,body=body)
    # 2. 使用 xpath 获取仓库的 name 和 update_time 数据
    for info in response.css('div#user-repositories-list li'):
        name = info.xpath('.//a[contains(@itemprop,"name codeRepository")]/text()').re_first('[\w-]+')
        update_time = info.xpath('.//relative-time/@datetime').extract_first()
    # 3. 将提取的数据存入 results:results.append((name,update_time))
        results.append((name,update_time))

# 定义异步任务执行
async def task(url):
    async with aiohttp.ClientSession() as session:
        # 调用 fetch 获取 HTML 页面
        html = await fetch(session,url)
        # 调用 parse 解析页面并将获得的数据存入 results
        parse(url,html.encode('utf8'))

# 主函数
def main():
    loop = asyncio.get_event_loop()
    url_template = 'https://github.com/shiyanlou?page={}&tab=repositories'
    tasks = [task(url_template.format(i)) for i in range(1,5)]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    main()
