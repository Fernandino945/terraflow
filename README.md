# 🌱 TerraFlow — Sistema de Riego Automatizado Inteligente
**Fase 1: API FastAPI + Dashboard · Desplegado en Render.com**

Integrantes: Benjamin Concha · Fernando Salazar · Juan Rojas

---

## 🚀 Despliegue en Render (producción)

### Paso 1 — Subir a GitHub
```bash
git init
git add .
git commit -m "TerraFlow Fase 1"
git remote add origin https://github.com/tu-usuario/terraflow.git
git push -u origin main
```

### Paso 2 — Desplegar la API en Render
1. Ve a **https://render.com** y crea cuenta gratis
2. Click en **New → Web Service**
3. Conecta tu repositorio de GitHub
4. Configura así:
   - **Name:** `terraflow-api`
   - **Runtime:** `Docker`
   - **Plan:** `Free`
5. Click en **Deploy** y espera ~3 minutos
6. Copia la URL que te genera: `https://terraflow-api.onrender.com`

### Paso 3 — Desplegar el Frontend en Render
1. Click en **New → Static Site**
2. Conecta el mismo repositorio
3. Configura así:
   - **Name:** `terraflow-frontend`
   - **Publish directory:** `frontend`
   - **Plan:** `Free`
4. En **Environment Variables** agrega:
   - Key: `TERRAFLOW_API_URL`
   - Value: `https://terraflow-api.onrender.com` ← la URL del paso anterior
5. Click en **Deploy**

### Paso 4 — Actualizar la URL de la API en el frontend
Abre `frontend/index.html` y reemplaza esta línea:
```javascript
const API = window.TERRAFLOW_API_URL || 'https://terraflow-api.onrender.com';
```
Cambia `https://terraflow-api.onrender.com` por la URL real que te dio Render en el Paso 2.

Haz commit y push — Render redespliega automáticamente.

---

## 💻 Desarrollo local (con Docker)

```bash
# Levantar API + Frontend localmente
docker-compose up --build

# API:       http://localhost:8000
# Dashboard: http://localhost:3000
# API Docs:  http://localhost:8000/docs
```

---

## 🗂 Estructura del proyecto

```
terraflow/
├── app/
│   ├── main.py                     # FastAPI app principal
│   ├── routes/
│   │   ├── sensors.py              # CAPA PRESENTACIÓN
│   │   └── irrigation.py           # CAPA PRESENTACIÓN
│   ├── services/
│   │   └── irrigation_logic.py     # CAPA LÓGICA DE NEGOCIO
│   ├── data/
│   │   └── mock_sensors.py         # CAPA DE DATOS
│   └── models/
│       └── sensor.py               # Modelos Pydantic
├── frontend/
│   ├── index.html                  # Dashboard web
│   └── nginx.conf                  # Config nginx (local)
├── Dockerfile                      # Imagen Docker API
├── docker-compose.yml              # Orquestación local
├── render.yaml                     # Config despliegue Render
└── requirements.txt
```

---

## 🔌 Endpoints de la API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Info del proyecto |
| GET | `/health` | Estado de la API |
| GET | `/sensors/status` | Lecturas de todos los sensores |
| GET | `/sensors/status/{id}` | Lectura de un sensor específico |
| GET | `/sensors/history/{id}` | Historial (últimas 6h) |
| POST | `/sensors/reading` | Registrar lectura manual |
| GET | `/irrigation/decision` | Decisión de riego para todas las zonas |
| GET | `/irrigation/decision/{id}` | Decisión de riego por sensor |

Documentación interactiva: **https://terraflow-api.onrender.com/docs**

---

## ☁ Arquitectura Cloud (IaaS / PaaS / SaaS)

```
SaaS  → Dashboard público en Render (URL permanente)
PaaS  → Render gestiona el runtime, deploys y escalado
IaaS  → Servidor virtual de Render corriendo el contenedor Docker
```
