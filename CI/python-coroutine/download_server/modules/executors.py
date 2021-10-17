# -*- encoding=utf-8 -*-

import asyncio

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


MULTI_NUMS = 2

thread_pool_executor = ThreadPoolExecutor(MULTI_NUMS)
process_pool_executor = ProcessPoolExecutor(MULTI_NUMS)
pycoroutine_executor = asyncio.get_event_loop()