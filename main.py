from fastapi import FastAPI

app = FastAPI()

ITEMS = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
]

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/items")
def items():
    return ITEMS
