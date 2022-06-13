from fastapi import FastAPI

from src.main.routes import starships_routes

app = FastAPI(title="Request Star Wars api project")

app.include_router(starships_routes)
