
# This script make 100 calls that would take 100 seconds to retrieve in about 4 seconds.

import aiohttp
import asyncio
import json

results = []

def generate_tasks(session):
    # generates 100 api calls with different values to hash.
    tasks = []
    
    for i in range(100):
        tasks.append(session.get(f'http://localhost:5000/hash/{i}'))
    
    return tasks


async def main():
    # dispatches all calls at the same time using asyncio and aiohttp.

    async with aiohttp.ClientSession() as session:
        
        tasks = generate_tasks(session)
        responses = await asyncio.gather(*tasks)

        for response in responses:
            results.append(await response.json())
        
        # save the results in a json document.
        with open('output.json', 'w') as file:
            json.dump(results, file, indent=4)
    

# execute main event loop
asyncio.run(main())
