from fastapi import APIRouter, HTTPException
from app.data.mock_sensors import get_mock_readings
from app.services.irrigation_logic import evaluate_irrigation, evaluate_all

router = APIRouter(prefix="/irrigation", tags=["Riego"])


@router.get("/decision", summary="Decisión de riego para todos los sensores")
def get_all_decisions():
    """Evalúa todos los sensores y decide si se debe activar el riego en cada zona."""
    readings = get_mock_readings()
    decisions = evaluate_all(readings)
    active = sum(1 for d in decisions if d["should_irrigate"])
    return {
        "total_zones": len(decisions),
        "zones_irrigating": active,
        "decisions": decisions
    }


@router.get("/decision/{sensor_id}", summary="Decisión de riego para un sensor")
def get_decision(sensor_id: str):
    """Evalúa un sensor específico y retorna la decisión de riego."""
    readings = get_mock_readings()
    reading = next((r for r in readings if r["sensor_id"] == sensor_id), None)
    if not reading:
        raise HTTPException(status_code=404, detail=f"Sensor '{sensor_id}' no encontrado.")
    return evaluate_irrigation(reading)
