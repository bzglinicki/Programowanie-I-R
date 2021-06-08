# Programowanie I R
# Programowanie asynchroniczne

import asyncio

async def print_after(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = asyncio.create_task(print_after("Frodo", 2))
    task2 = asyncio.create_task(print_after("Baggins", 1))

    await task1
    await task2

asyncio.run(main())