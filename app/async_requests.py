import asyncio
import aiohttp
import matplotlib.pyplot as plt

# List of replica URLs
replicas = [
    "http://localhost:50975/home",  
    "http://localhost:50976/home",
    "http://localhost:50977/home"

]

async def fetch(session, url, counter):
    async with session.get(url) as response:
        counter[url] += 1
        return await response.text()

async def main():
    tasks = []
    counter = {url: 0 for url in replicas}
    async with aiohttp.ClientSession() as session:
        for i in range(10000):
            # Distribute requests among replicas
            replica = replicas[i % len(replicas)]
            task = asyncio.create_task(fetch(session, replica, counter))
            tasks.append(task)
        
        # Gather all the results
        await asyncio.gather(*tasks)
        
    return counter

if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)

    # Plotting the results
    servers = list(result.keys())
    counts = list(result.values())

    plt.bar(servers, counts, color=['blue', 'green', 'red'])
    plt.xlabel('Server Instances')
    plt.ylabel('Number of Requests Handled')
    plt.title('Requests Handled by Each Server Instance')
    plt.show()