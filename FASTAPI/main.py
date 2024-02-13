# To run using replit
# uvicorn main:app --reload --host 0.0.0.0 --port 5000

from typing import List
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware

# Define allowed origins (replace "*" with specific origins if needed)
origins = ["*"]
app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

track_record = []

class Input:
    def __init__(self, flag, full_name, lap_time, team, date):
        self.flag = flag
        self.full_name = full_name
        self.lap_time = lap_time
        self.team = team
        self.date = date


track_record.append(Input("au", "Selimon Shukurzad", "BUGATTI BOLIDE","1:00", "04/09/2023"))
track_record.append(Input("sx", "Max Verstappen", "Red Bull","1:22:30.450", "30/06/2023"))
track_record.append(Input("me", "Sergio Pérez", "Red Bull","1:44:30.450", "30/06/2023"))
track_record.append(Input("mc", "Charles Leclerc", "Ferrari","	1:54:30.450", "30/06/2023"))
track_record.append(Input("gb", "Lewis Hamilton", "Mercedes","2:11:30.450", "30/06/2023"))
track_record.append(Input("es", "Fernando Alonso", "Aston Martin","2:18:30.450", "30/06/2023"))
track_record.append(Input("gb", "George Russell", "Mercedes","2:23:30.450", "30/06/2023"))


@app.get("/")
async def read_root():
    return track_record


@app.get("/{id}")
def read_root(id: int):
    return {track_record[id]}


@app.get("/{id}/{info}")
def read_root(id: int, info: str):
    record = track_record[id]
    return {info: getattr(record, info)}
