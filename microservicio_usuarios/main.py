import sys
import os

# Ajustar el path para que encuentre los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
from microservicio_usuarios.infraestructura.api.router import router

app = FastAPI(title="Microservicio de Usuarios")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)