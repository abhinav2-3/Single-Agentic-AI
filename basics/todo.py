import aiohttp
import asyncio

URL = "https://jsonplaceholder.typicode.com/todos"


async def get_all_todos(session: aiohttp.ClientSession):
    async with session.get(URL) as response:
        return await response.json()


async def get_todo_by_id(session: aiohttp.ClientSession, id: int):
    async with session.get(f"{URL}/{id}") as response:
        return await response.json()


async def get_multiple_todos(session: aiohttp.ClientSession, ids: list[int]):
    result = await asyncio.gather(*[get_todo_by_id(session, id) for id in ids])
    return result


async def main():

    async with aiohttp.ClientSession() as session:
        result = await get_all_todos(session)
        print("Result : ", result)

        result2 = await get_todo_by_id(session, 1)
        print("Result 2 : ", result2)

        result3 = await get_multiple_todos(session, [1, 2, 5])
        print("Result 3 : ", result3)


asyncio.run(main())
