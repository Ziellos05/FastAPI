from fastapi import FastAPI
from sqlalchemy import desc
from routes.user import user

app = FastAPI(
    title="My first FastApi",
    description="This is my first FastApi",
    version="0.0.1",
    openapi_tags=[{
        "name":"users",
        "description":"users routes"
    }]
)

@app.get('/')
def helloworld():
    return "hello world"

app.include_router(user)