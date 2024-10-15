from fastapi import FastAPI
from pydantic import BaseModel
from beauty import main
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

class Item(BaseModel):
    root: str
    depth: int


@app.post('/api/crawl')
def me(data : Item ):
    return {"data" : main(data.root, data.depth)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

