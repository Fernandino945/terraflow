from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SensorReading(BaseModel):
    sensor_id: str
    humidity: float        # % humedad del suelo
    temperature: float     # °C temperatura del suelo
    conductivity: float    # mS/cm conductividad
    timestamp: Optional[str] = None

    model_config = {"json_schema_extra": {
        "example": {
            "sensor_id": "S1",
            "humidity": 35.2,
            "temperature": 21.5,
            "conductivity": 1.2,
            "timestamp": "2026-05-09T10:00:00"
        }
    }}


class IrrigationDecision(BaseModel):
    sensor_id: str
    should_irrigate: bool
    reason: str
    humidity: float
    temperature: float
    timestamp: str
