from fastapi import FastAPI
import uvicorn
from routers import users

app = FastAPI()
app.include_router(users.router)

# fastapi dev main.py --host 0.0.0.0

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}




