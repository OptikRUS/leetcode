import os
from time import time
import asyncio
import asyncpg


username = os.getenv('USERNAME', None)
password = os.getenv('PASSWORD', None)
QUERY = """
        INSERT INTO users 
        VALUES($1, $2, $3);
        """


async def fill_table_users(db_pool):
    await db_pool.fetch(QUERY, 'username', 'lastname', 18)


async def main():

    db_pool = await asyncpg.create_pool(f"postgresql://{username}:{password}@localhost:5432/pdb")

    for i in range(10000):
        asyncio.ensure_future(coro_or_future=fill_table_users(db_pool))


if __name__ == "__main__":
    start = time()
    asyncio.run(main())
    print(time() - start)

# 3.4167120456695557
# 3.0974180698394775
# 3.292059898376465
