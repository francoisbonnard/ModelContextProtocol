import asyncio

async def fetch_data(delay):
    print("fetching data...")
    await asyncio.sleep(delay)
    print("data fetched")
    return {"data":"some data"}

# define asynchronous function // coroutine function
async def main():
    print("start of main coroutine")
    task = fetch_data(2)
    result = await task
    print(f"Received result : {result}")
    print("End of main coroutine")

# run the main (we pass main as a coroutine)
asyncio.run(main())
