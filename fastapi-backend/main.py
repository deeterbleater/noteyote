from fastapi import FastAPI
import users
import auth

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def read_rood():
    return {'message': 'FastAPI is working :3'}
