import asyncpg
import asyncio
import random
import string
from database import get_db_connection


extensions = ['txt', 'pdf', 'doc', 'jpg', 'png', 'xlsx', 'mp3', 'mp4', 'zip']


def get_random_name(min:int = 10, max:int = 200):
    '''Generate random name with random length in range (min, max)'''

    characters = string.ascii_letters + string.digits + " _-"
    name_length = random.randint(min, max)
    return ''.join(random.choice(characters) for i in range(name_length))


def get_random_extension():
    '''Returning radom file extension'''

    return random.choice(extensions)


def get_random_status():
    '''Return random status'''

    return True if random.random() > 0.5 else False


async def insert_full_name(connection:asyncpg.Connection, name: str, extension):
    '''Insert value into full_names table'''

    query = 'INSERT INTO full_names (name) VALUES($1)'
    await connection.execute(query, f'{name}.{extension}')


async def insert_short_name(connection:asyncpg.Connection, name: str, status: bool):
    '''Insert value into short_names table'''

    query = 'INSERT INTO short_names (name, status) VALUES($1, $2)'
    await connection.execute(query, name, status)


async def generate_names(count_full_names:int = 500, count_short_names:int = 700):
    '''Seed data in db'''
    async for connection in get_db_connection():
        for i in range(max(count_full_names,count_short_names)):
            name = get_random_name()
            extension = get_random_extension()
            status = get_random_status()
            
            if i < count_full_names:
                await insert_full_name(connection, name, extension)
            
            await insert_short_name(connection, name, status)
