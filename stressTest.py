import asyncio
import aiohttp
import time

async def send_request(session, url, data, i):
    start_time = time.time()
    async with session.post(url, data=data) as response:
        end_time = time.time()

        if response.status == 200:
            print(f"Request {i+1} successful! Execution time: {end_time - start_time} seconds")
        else:
            print(f"Request {i+1} failed with status code: {response.status}")

async def send_multiple_requests(url, n):
    data = {
        'key1': 'value1' #replace with your actual request body
    }

    total_start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(n):
            task = asyncio.create_task(send_request(session, url, data, i))
            tasks.append(task)

        await asyncio.gather(*tasks)
    total_end_time = time.time()
    print(f"Total time to run {n} requests: {total_end_time - total_start_time} seconds\n")

url = 'https://example.com/abc'  # Replace with your actual URL
n = 4  # Number of async requests
asyncio.run(send_multiple_requests(url, n))

