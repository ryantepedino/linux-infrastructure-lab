from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Linux Infrastructure Lab API",
    description="API criada para laboratório prático de Linux, Docker e backend.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Linux Infrastructure Lab API",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": "docker-fastapi-linux",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/server-info")
def server_info():
    return {
        "lab": "Docker + FastAPI on Linux",
        "skills": ["Linux", "Docker", "FastAPI", "Backend", "Infrastructure"],
        "objective": "Demonstrar prática em infraestrutura Linux e deploy de aplicações."
    }
