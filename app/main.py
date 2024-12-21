from fastapi import FastAPI
from app.routers import task, user


app = FastAPI()
app.include_router(task.router_task)
app.include_router(user.router_user)


@app.get('/')
async def root():
    return {"message": "Welcome to Taskmanager"}