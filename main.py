from fastapi import FastAPI
from app.database import database
from app.api import endpoints

app = FastAPI()

database.init_db(app)
app.include_router(endpoints.router)