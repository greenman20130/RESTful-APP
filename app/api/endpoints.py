from fastapi import APIRouter
from .models import models

router = APIRouter()

@router.get("/example")
async def read_example():
    return {"message": "Hello, World!"}