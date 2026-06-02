from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat
from app.core.config import settings

app = FastAPI(
    title="COMPARTIR API",
    description="Compañero IA para aprender inglés"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",

        # Agregar aquí tu dominio de Vercel cuando despliegues
        "https://compartirai.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(chat.router)


@app.get("/")
def root():
    return {
        "service": "COMPARTIR API",
        "status": "online",
        "deepseek_configured": bool(settings.DEEPSEEK_API_KEY),
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }