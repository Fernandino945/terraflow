from fastapi import APIRouter, HTTPException
from app.data.mock_sensors import get_mock_readings, get_mock_history
from app.models.sensor import SensorReading

router = APIRouter(prefix="/sensors", tags=["Sensores"])

# Almacén temporal de lecturas manuales (en memoria)
manual_readings: list = []


@router.get("/status", summary="Estado actual de todos los sensores")
def get_all_sensors():
    """Retorna la lectura simulada en tiempo real de todos los sensores IoT."""
    return {
        "status": "ok",
        "total_sensors": 4,
        "readings": get_mock_readings()
    }


@router.get("/status/{sensor_id}", summary="Estado de un sensor específico")
def get_sensor(sensor_id: str):
    """Retorna la lectura de un sensor por su ID."""
    readings = get_mock_readings()
    sensor = next((r for r in readings if r["sensor_id"] == sensor_id), None)
    if not sensor:
        raise HTTPException(status_code=404, detail=f"Sensor '{sensor_id}' no encontrado.")
    return sensor


@router.get("/history/{sensor_id}", summary="Historial de lecturas de un sensor")
def get_history(sensor_id: str, hours: int = 6):
    """Retorna el historial de lecturas de los últimas N horas (por defecto 6)."""
    history = get_mock_history(sensor_id, hours)
    if not history:
        raise HTTPException(status_code=404, detail=f"Sensor '{sensor_id}' no encontrado.")
    return {"sensor_id": sensor_id, "hours": hours, "history": history}


@router.post("/reading", summary="Registrar lectura manual de prueba")
def post_reading(reading: SensorReading):
    """Permite enviar una lectura manual, simulando lo que enviaría un microcontrolador."""
    data = reading.model_dump()
    if not data.get("timestamp"):
        from datetime import datetime
        data["timestamp"] = datetime.utcnow().isoformat()
    manual_readings.append(data)
    return {"status": "registered", "reading": data}


@router.get("/manual", summary="Ver lecturas manuales registradas")
def get_manual():
    return {"total": len(manual_readings), "readings": manual_readings}
