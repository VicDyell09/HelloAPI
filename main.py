from fastapi import FastAPI

app = FastAPI()

listdata = {
    1: {"NIM": "18220019", "Nama": "Vic Finnegan Dyell"}
}

@app.get("/")
async def get_data():
    return listdata

@app.post("/")
async def add_data(nim: str, nama: str):
    obj = {"NIM": nim, "Nama": nama}
    key = len(listdata) + 1
    listdata[key] = obj
    return {"message": "Data added"}