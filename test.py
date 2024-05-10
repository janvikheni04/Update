from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()
data = []

db_name = "apitest"
db_user = "postgres"
db_pswd = "1234"
db_host = "localhost"
db_port = "5432"

conn = psycopg2.connect(
    dbname = db_name,
    user = db_user,
    password = db_pswd,
    host = db_host,
    port = db_port
)


class Book(BaseModel):
    title: str
    author: str
    publisher: str


@app.post("/book")
def createbook(book: Book):
    data.append(book.dict())

    return data

@app.get("/{id}")
def readbook(id: int):
    return data[id]


@app.put("/book/{id}")
def updatebook(title: str, book: Book):
    data[id] = book
    return book
    


@app.delete("/book/{id}")
def deletebook(id: int):
    data.pop(id)
    return data
    