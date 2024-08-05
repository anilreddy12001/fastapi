import websockets
import asyncio
import logging
import subprocess

from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:3001"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allowed HTTP methods (e.g., GET, POST)
    allow_headers=["*"],  # Allowed headers
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id^2": item_id*item_id, "q": q}
# Run the other script
subprocess.run(["python", "pymongo_test_query.py"])


# Server data
PORT = 10000
print("Server listening on Port " + str(PORT))
logging.basicConfig(level=logging.INFO)
logging.info("Server listening on Port" + str(PORT))


# A set of connected ws clients
connected = set()

