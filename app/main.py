from fastapi import FastAPI
from routers import users, expenses
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Daily Expenses Sharing Application"}

