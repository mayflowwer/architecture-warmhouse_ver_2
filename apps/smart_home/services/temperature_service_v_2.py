from fastapi import FastAPI, Query
from pydantic import BaseModel
import random


app = FastAPI()

class TemperatureResponse(BaseModel):
    location: str
    sensorId: str
    temperature: float


@app.get("/temperature", response_model=TemperatureResponse)
def get_temperature(location: str = Query(default="", description="Name of the room"),
                    sensorId: str = Query(default="", description="Sensor identifier")):

    if not location:
        if sensorId == "1":
            location = "Living Room"
        elif sensorId == "2":
            location = "Bedroom"
        elif sensorId == "3":
            location = "Kitchen"
        else:
            location = "Unknown"

    if not sensorId:
        if location == "Living Room":
            sensorId = "1"
        elif location == "Bedroom":
            sensorId = "2"
        elif location == "Kitchen":
            sensorId = "3"
        else:
            sensorId = "0"

    temperature = random(1, 100)

    return TemperatureResponse(location=location, sensorId=sensorId, temperature=temperature)
