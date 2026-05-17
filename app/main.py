from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sensors, irrigation

app = FastAPI(
    title="TerraFlow API",
    description="Sistema de Gestión Hídrica Autónoma IoT — Fase 1: Datos simulados",
    version="1.0.0",
    contact={"name": "Benjamin Concha, Fernando Salazar, Juan Rojas"},
)

# CORS habilitado para que el frontend pueda consumir la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensors.router)
app.include_router(irrigation.router)


@app.get("/", tags=["Root"])
def root():
    return {
        "project": "TerraFlow",
        "description": "Sistema de Riego Automatizado Inteligente",
        "version": "1.0.0",
        "fase": "Fase 1 - Docker + Datos simulados",
        "docs": "/docs",
    }


@app.get("/health", tags=["Root"])
def health():
    return {"status": "healthy", "service": "terraflow-api"}
