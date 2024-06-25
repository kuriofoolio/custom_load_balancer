import asyncio
import aiohttp

# List of replica URLs
replicas = [
    "http://localhost:50975/home",  
    "http://localhost:50976/home",
    "http://localhost:50977/home"

]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(500):
            # Distribute requests among replicas
            replica = replicas[i % len(replicas)]
            task = asyncio.create_task(fetch(session, replica))
            tasks.append(task)
        
        # Gather all the results
        results = await asyncio.gather(*tasks)
        print(results)

if __name__ == "__main__":
    asyncio.run(main())
