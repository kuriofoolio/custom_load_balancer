import asyncio
import aiohttp
import random
import matplotlib.pyplot as plt
import time

# Initial list of replica URLs
replicas = [
    "http://localhost:51546/home",  
    "http://localhost:51547/home",
    "http://localhost:51548/home",
    # "http://localhost:51549/home",
    # "http://localhost:51550/home",
    # "http://localhost:51551/home"
]

# Weights for each replica
weights = [0.30, 0.45, 0.25]


async def fetch(session, url, counter):
    async with session.get(url) as response:
        counter[url] += 1
        return await response.text()

async def main():
    tasks = []
    counter = {url: 0 for url in replicas}
    failed_replica = None

    async with aiohttp.ClientSession() as session:
        for i in range(10000):
            # Introduce a failure after 5000 requests
            if i == 5000 and failed_replica is None:
                failed_replica = random.choice(replicas)
                #weight_of_failed_replica=replicas.index(failed_replica)
                print(f"Replica failed: {failed_replica}")
                replicas.remove(failed_replica)
                counter.pop(failed_replica)
                weights.pop(replicas.index(failed_replica))

            # Simulate adding a new replica after 8000 requests
            if i == 8000 and failed_replica is not None:
                new_replica = f"http://localhost:51549/home"
                print(f"New replica added: {new_replica}")
                replicas.append(new_replica)
                counter[new_replica] = 0
                #weights.append(weights[weight_of_failed_replica])  # Adjust the weight as needed
                weights.append(0.25)

            # Randomly distribute requests among replicas with given weights
            if replicas:
                replica = random.choices(replicas, weights=weights, k=1)[0]
                task = asyncio.create_task(fetch(session, replica, counter))
                tasks.append(task)
        
        # Gather all the results
        await asyncio.gather(*tasks)
        
    return counter

if __name__ == "__main__":
    start_time = time.time()
    result = asyncio.run(main())
    elapsed_time = time.time() - start_time
    print(result)
    print(f"Total time taken: {elapsed_time} seconds")

    # # Plotting the results
    # servers = list(result.keys())
    # counts = list(result.values())

    # plt.bar(servers, counts, color=['blue', 'green', 'red', 'purple', 'orange'])
    # plt.xlabel('Server Instances')
    # plt.ylabel('Number of Requests Handled')
    # plt.title('Requests Handled by Each Server Instance')
    # plt.show()
