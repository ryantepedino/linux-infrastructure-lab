from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Nginx Reverse Proxy FastAPI Lab",
    description="Laboratório Linux com Nginx atuando como reverse proxy para uma API FastAPI em Docker.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "API atrás do Nginx Reverse Proxy",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "fastapi-backend",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/infra")
def infra():
    return {
        "architecture": "Nginx Reverse Proxy -> FastAPI Container",
        "skills": ["Linux", "Nginx", "Docker", "Docker Compose", "FastAPI"],
        "objective": "Simular publicação de aplicação backend usando reverse proxy."
    }
