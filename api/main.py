from fastapi import FastAPI
from database.models import User, session


app = FastAPI()


@app.get("/users")
def users():
    users = session.query(User).all()
    return users


# uvicorn.run()
