#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aio_amac_infodisc_manager_scraper.py
# chasyncio
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 03/08/19 10:01.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
中国证券投资基金业协会 Asset Management Association of China

私募基金管理人综合查询
"""
import time
import random
# Begin by importing the aiohttp module
import aiohttp
# Begin by importing the multiprocessing module
import multiprocessing
#
import asyncio


# 爬取中国证券投资基金业协会-私募基金管理人-首页
url_index = 'http://gs.amac.org.cn/amac-infodisc/api/pof/manager'
# limit the total number of connections open at once
# to be a good citizen on servers.
sema = asyncio.Semaphore(10*multiprocessing.cpu_count())


# Now, let's try to get a web-page
async def get_manager_info(url):
    async with aiohttp.ClientSession() as session:
        async with sema, session.get(url) as resp:
            print(resp.status)
            print(await resp.text())


def main():
    # 获取时间循环
    loop = asyncio.get_event_loop()
    # 添加任务队列
    # tasks = [get_manager_info(url) for url in urls]
    tasks = [get_manager_info(url_index)]
    # 激活协程
    loop.run_until_complete(asyncio.wait(tasks))
    # 关闭时间循环
    loop.close()


if __name__ == '__main__':
    start = time.time()
    main()
    print('总耗时: %.5f s' % float(time.time()-start))
