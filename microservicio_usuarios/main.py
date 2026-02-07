import sys
import os
# AGREGAR ESTO AL INICIO: Truco para que Python reconozca la carpeta raíz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
# CAMBIO: Usar la ruta completa
from microservicio_usuarios.infrastructure.api.router import router

app = FastAPI(title="Microservicio de Usuarios")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)