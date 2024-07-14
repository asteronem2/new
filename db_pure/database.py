import asyncio

import asyncpg

from db_pure import config


class DB:
    def __init__(self):
        db_conf = config.Settings()
        self.config = db_conf.config_dict()
        self.connection = None

    async def connect(self):
        self.connection = await asyncpg.connect(
            host=self.config['DB_HOST'],
            port=self.config['DB_PORT'],
            user=self.config['DB_USER'],
            password=self.config['DB_PASS'],
            database=self.config['DB_NAME'],
        )
        text = f'Connection to db ({self.config["DB_NAME"]}) successfully'
        print(text)
        return text

    async def fetch(self, query, values: list = None):
        # query.replace('\n', ' ')
        # query = 'BEGIN;\n\n ' + query + '\n\n COMMIT;'
        async with self.connection.transaction():
            if self.connection:
                if values:
                    result = await self.connection.fetch(query, *values)
                else:
                    result = await self.connection.fetch(query)
                return result
            else:
                raise Exception('A connection to the database was not established')

    async def create_pool(self):
        res = await asyncpg.create_pool(
            host=self.config['DB_HOST'],
            port=self.config['DB_PORT'],
            user=self.config['DB_USER'],
            password=self.config['DB_PASS'],
            database=self.config['DB_NAME'],
        )
        return res

    def __del__(self):
        async def close_connection():
            await self.connection.close()

        if self.connection:
            asyncio.create_task(close_connection())
