# coding:utf-8

# ʹ�� csv ģ���������ļ�
import csv
# ʹ�� asyncion ����ʵ���첽���
import asyncio
# ʹ�� aiohttp ��ʵ����������
import aiohttp
# �����첽����еĳ�ʱ
import async_timeout
# ʹ�� scrapy �е� HtmlResponse �������ҽ���ҳ������
from scrapy.http import HtmlResponse

# ����Ľ�����浽 result �б��У�ÿ��Ԫ�ض���һ����Ԫ��(name,update_time)
result = []

# �����ȡ��ҳ���ݵ��첽������ע�ⶨ��ķ�ʽ
async def fetch(session,url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

# ������ȡ��ҳ���ݵĺ���
def parse(url,body):
    # 1. ���� HtmlResponse ����
    # 2. ʹ�� xpath ��ȡ�ֿ�� name �� update_time ����
    # 3. ����ȡ�����ݴ��� results:results.append((name,update_time))
    pass

# �����첽����ִ��
async def task(url):
    async with aiohttp.ClientSeesion() as session:
        # ���� fetch ��ȡ HTML ҳ��
        TODO
        # ���� parse ����ҳ�沢����õ����ݴ��� results
        TODO

# ������
def main():
    loop = asyncio.get_event_loop()
    url_template = 'https://github.com/shiyanlou?page={}&tab=repositories'
    tasks = [task(ur_template.format(i)) for i in range(1,5)]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

if __name__ == '__main__':
    main()
    













