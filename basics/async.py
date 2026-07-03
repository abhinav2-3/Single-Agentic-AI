import aiohttp
import asyncio


async def fetch_user():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com") as response:
            data = await response.json()
            return data


async def fetch_repo(session: aiohttp.ClientSession, repo: str) -> dict:
    url = f"https://api.github.com/repos/{repo}"
    async with session.get(url) as response:
        return await response.json()


async def main():
    data = await fetch_user()
    print(data["current_user_url"])

    repos = ["python/cpython", "nodejs/node", "facebook/react"]

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(
            fetch_repo(session, repos[0]),
            fetch_repo(session, repos[1]),
            fetch_repo(session, repos[2]),
        )
    for repo in result:
        print(f"{repo['full_name']} --> {repo['stargazers_count']}")


asyncio.run(main())
