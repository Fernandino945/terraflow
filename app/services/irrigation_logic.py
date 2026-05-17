from datetime import datetime


# Umbrales del motor predictivo (basado en lógica TerraFlow)
HUMIDITY_LOW = 40.0      # % → activa riego si está por debajo
HUMIDITY_HIGH = 85.0     # % → bloquea riego por saturación
TEMP_LOW = 8.0           # °C → bloquea riego por frío extremo


def evaluate_irrigation(reading: dict) -> dict:
    """
    Motor predictivo de lazo cerrado.
    Responde 3 preguntas:
      1. ¿El suelo está seco? → activa riego
      2. ¿El suelo está saturado? → bloquea riego
      3. ¿Hace frío extremo? → bloquea riego
    """
    humidity = reading["humidity"]
    temperature = reading["temperature"]
    sensor_id = reading["sensor_id"]
    now = datetime.utcnow().isoformat()

    if temperature < TEMP_LOW:
        return {
            "sensor_id": sensor_id,
            "should_irrigate": False,
            "reason": f"Temperatura crítica ({temperature}°C < {TEMP_LOW}°C). Riego bloqueado para proteger raíces.",
            "humidity": humidity,
            "temperature": temperature,
            "timestamp": now,
        }

    if humidity > HUMIDITY_HIGH:
        return {
            "sensor_id": sensor_id,
            "should_irrigate": False,
            "reason": f"Suelo saturado ({humidity}% > {HUMIDITY_HIGH}%). Riego bloqueado para evitar asfixia radicular.",
            "humidity": humidity,
            "temperature": temperature,
            "timestamp": now,
        }

    if humidity < HUMIDITY_LOW:
        return {
            "sensor_id": sensor_id,
            "should_irrigate": True,
            "reason": f"Humedad baja ({humidity}% < {HUMIDITY_LOW}%). Activando riego.",
            "humidity": humidity,
            "temperature": temperature,
            "timestamp": now,
        }

    return {
        "sensor_id": sensor_id,
        "should_irrigate": False,
        "reason": f"Humedad óptima ({humidity}%). No se requiere riego.",
        "humidity": humidity,
        "temperature": temperature,
        "timestamp": now,
    }


def evaluate_all(readings: list) -> list:
    return [evaluate_irrigation(r) for r in readings]
