import os
from time import time
import asyncio
import asyncpg


username = os.getenv('USERNAME', None)
password = os.getenv('PASSWORD', None)
QUERY = """
        INSERT INTO users ("username", "lastname", "age")
        VALUES('username', 'lastname', 18);
        """


async def fill_table_users(connect):
    await connect.execute(QUERY)
    # await db_pool.fetch(QUERY, 'username', 'lastname', 18)
    # await connect.close()


async def main():

    # db_pool = await asyncpg.create_pool(f"postgresql://{username}:{password}@localhost:5432/pdb")

    # await asyncpg.connect(
    #     database="pdb",
    #     user="username",
    #     password="password",
    #     host="127.0.0.1",
    #     port=5432
    # )

    connect = await asyncpg.connect("postgresql://optikrus:password123456@localhost:5432/pdb")

    for i in range(10000):
        await asyncio.create_task(fill_table_users(connect))


if __name__ == "__main__":
    start = time()
    asyncio.run(main())
    print(time() - start)

# 8.116582155227661
# 8.281738996505737
# 8.277981042861938
