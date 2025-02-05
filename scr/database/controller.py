import aiosqlite
from scr.configs.config import DataBase_PATH


class DataBase:
    @staticmethod
    async def create_db():
        async with aiosqlite.connect(DataBase_PATH) as db:
            await db.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
            await db.commit()

    @staticmethod
    async def add_user(name):
        async with aiosqlite.connect(DataBase_PATH) as db:
            await db.execute('INSERT INTO users (name) VALUES (?)', (name,))
            await db.commit()
