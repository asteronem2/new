import time
from contextlib import asynccontextmanager

import asyncpg
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import routers
from db_pure.database import DB
from src.utils import slugify

db = None


@asynccontextmanager
async def lifespan(local_app: FastAPI):
    global db
    db = await DB().create_pool()
    print('Connection successful')
    yield
    db.close()


app = FastAPI(lifespan=lifespan)

origins = [
    'http://127.0.0.1:5173',
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routers.router, prefix='/api/v1/dishes')


@app.get('/')
async def index():
    return RedirectResponse('/api/v1/')


@app.get('/api/v1/ingredients/')
async def api():
    result = await db.fetch("""
    SELECT * FROM ingredient
    """)

    return result


@app.get('/api/v1/ingredients/{path_id}/')
async def api(path_id):
    result = await db.fetchrow("""
    SELECT * FROM ingredient
    WHERE id = $1;
    """, *(int(path_id),))
    return result


class Item(BaseModel):
    name: str
    category: str
    calories: float
    proteins: float = 0.0
    fats: float = 0.0
    carbs: float = 0.0
    price: float
    description: str = None
    photo_url: str = None


@app.post('/api/v1/ingredients/add')
async def api(item: Item):
    print('\033[33m', item, '\033[0m')

    items_dict = {
        'name': item.name,
        'slug': await slugify(item.name),
        'category': item.category,
        'description': item.description,
        'calories': item.calories,
        'proteins': item.proteins,
        'fats': item.fats,
        'carbs': item.carbs,
        'price': item.price,
        'photo_url': item.photo_url
    }

    len_items = len(items_dict.keys())

    result = await db.fetch(f"""
    INSERT INTO ingredient
    ({', '.join(items_dict.keys())})
    VALUES ({', '.join([f'${i}' for i in range(1, len_items + 1)])});
    """, *items_dict.values())

    print(result)
    return result


if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=4444)
