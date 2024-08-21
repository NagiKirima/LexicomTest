import asyncio
from database import db_init, execute_query
from seeder import generate_names


async def main():    
    await db_init()
    await generate_names(count_full_names=500, count_short_names=700)

    # solve1
    with open("sql/solve1.sql", "r") as file:
        solve1_query = file.read()
    await execute_query(solve1_query)

    # solve2
    with open("sql/solve2.sql", "r") as file:
        solve2_query = file.read()
    await execute_query(solve2_query)


if __name__ == "__main__":
    asyncio.run(main())