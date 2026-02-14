import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
# OJO: infraestructura
from microservicio_pedidos.infraestructura.api.router import router

app = FastAPI(title="Microservicio de Pedidos")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)