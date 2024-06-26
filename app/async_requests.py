import asyncio
import aiohttp
import random
import matplotlib.pyplot as plt

# List of replica URLs
replicas = [
    "http://localhost:51546/home",  
    "http://localhost:51547/home",
    "http://localhost:51548/home",
    "http://localhost:51549/home",
    "http://localhost:51550/home",
    "http://localhost:51551/home"
]

# Weights for each replica
weights = [0.30, 0.15, 0.21,0.10,0.20,0.04]

async def fetch(session, url, counter):
    async with session.get(url) as response:
        counter[url] += 1
        return await response.text()

async def main():
    tasks = []
    counter = {url: 0 for url in replicas}
    async with aiohttp.ClientSession() as session:
        for i in range(10000):
            # Randomly distribute requests among replicas with given weights
            replica = random.choices(replicas, weights=weights, k=1)[0]
            task = asyncio.create_task(fetch(session, replica, counter))
            tasks.append(task)
        
        # Gather all the results
        await asyncio.gather(*tasks)
        
    return counter

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)

    # # Plotting the results
    # servers = list(result.keys())
    # counts = list(result.values())

    # plt.bar(servers, counts, color=['blue', 'green'])
    # plt.xlabel('Server Instances')
    # plt.ylabel('Number of Requests Handled')
    # plt.title('Requests Handled by Each Server Instance')
    # plt.show()