from datetime import datetime, timedelta
import random

# Datos base de sensores simulados
BASE_SENSORS = [
    {
        "sensor_id": "S1",
        "zone": "Zona Norte",
        "crop": "Tomates",
        "humidity": 32.5,
        "temperature": 22.1,
        "conductivity": 1.1,
    },
    {
        "sensor_id": "S2",
        "zone": "Zona Sur",
        "crop": "Paltos",
        "humidity": 78.0,
        "temperature": 19.8,
        "conductivity": 0.9,
    },
    {
        "sensor_id": "S3",
        "zone": "Zona Este",
        "crop": "Lechugas",
        "humidity": 55.3,
        "temperature": 20.5,
        "conductivity": 1.3,
    },
    {
        "sensor_id": "S4",
        "zone": "Zona Oeste",
        "crop": "Papas",
        "humidity": 41.7,
        "temperature": 18.9,
        "conductivity": 1.0,
    },
]


def get_mock_readings():
    """Retorna lecturas simuladas con pequeña variación aleatoria."""
    now = datetime.utcnow()
    readings = []
    for s in BASE_SENSORS:
        readings.append({
            **s,
            "humidity": round(s["humidity"] + random.uniform(-2, 2), 1),
            "temperature": round(s["temperature"] + random.uniform(-0.5, 0.5), 1),
            "conductivity": round(s["conductivity"] + random.uniform(-0.05, 0.05), 2),
            "timestamp": now.isoformat(),
        })
    return readings


def get_mock_history(sensor_id: str, hours: int = 6):
    """Genera historial de lecturas para un sensor en las últimas N horas."""
    now = datetime.utcnow()
    base = next((s for s in BASE_SENSORS if s["sensor_id"] == sensor_id), None)
    if not base:
        return []

    history = []
    for i in range(hours * 4):  # cada 15 minutos
        t = now - timedelta(minutes=15 * (hours * 4 - i))
        history.append({
            "sensor_id": sensor_id,
            "humidity": round(base["humidity"] + random.uniform(-5, 5), 1),
            "temperature": round(base["temperature"] + random.uniform(-1, 1), 1),
            "conductivity": round(base["conductivity"] + random.uniform(-0.1, 0.1), 2),
            "timestamp": t.isoformat(),
        })
    return history
