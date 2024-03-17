from fastapi import FastAPI

app = FastAPI()
a = [312864, 174623, 192367126]
@app.get("/")
def read_root():
    return {"Hello": a}