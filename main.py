from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3000",  # React frontend URL
    "https://yummipizza-api-test.herokuapp.com",  # Your deployed frontend URL (if applicable)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite+aiosqlite:///./sqlite/meals.db"

# Create database engine and session
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

metadata = MetaData()
meals_table = Table(
    "meals", metadata, autoload_with=create_engine("sqlite:///./sqlite/meals.db")
)


# http://localhost:5000/api/meals
@app.get("/api/meals")
async def get_meals():
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(meals_table))
            meals = result.fetchall()
            return [
                {
                    "id": meal.id,
                    "name": meal.name,
                    "description": meal.description,
                    "price": meal.price,
                    "path_to_photo": meal.path_to_photo,
                }
                for meal in meals
            ]
