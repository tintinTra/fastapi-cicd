from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def start():
    return {"message": "Hallo von FastAPI!"}


@app.get("/summe")
def summe(a: int, b: int):
    return {"ergebnis": a + b}

