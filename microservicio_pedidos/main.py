import sys
import os

# --- CORRECCIÓN DE IMPORTACIONES ---
# Esto agrega la carpeta raíz del proyecto al path de Python
# para que encuentre el paquete 'microservicio_pedidos' correctamente.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
# Import absoluto
from microservicio_pedidos.infrastructure.api.router import router

app = FastAPI(title="Microservicio de Pedidos")

# Incluimos las rutas definidas en el router
app.include_router(router)

if __name__ == "__main__":
    # Ejecuta en el puerto 8002 como se solicitó
    uvicorn.run(app, host="0.0.0.0", port=8002)