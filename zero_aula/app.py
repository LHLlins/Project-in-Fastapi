from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"message": "Server is running"}

@app.get("/")
def read_root():

    return {"message": "hello World"}





