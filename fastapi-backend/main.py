from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import users
import auth

app = FastAPI()

origins = [
    "http://localhost:3000",  # Add your Svelte front end URL here
    "http://dev.thothclock.com", # You can add more origins as needed
]

app.include_router(users.router)
app.include_router(auth.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_rood():
    return {'message': 'FastAPI is working :3'}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
