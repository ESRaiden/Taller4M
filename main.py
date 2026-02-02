from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#Modelo de datos para el POST
class Receta(BaseModel):
    nombre: str
    ingredientes: list
    preparacion: Optional[str] = None


@app.get("/")
def read_root():
    return "Bienvenidos a la UNACH"


#Este endpoint responde a urls como: /receta/100, /receta/5, etc.
@app.get("/receta/{id_receta}")
def consultar_receta(id_receta: int):
    return {
        "mensaje": f"Consultando la receta {id_receta}",
        "equipo_base": [
            "Sartén de teflón",
            "Cuchillo de chef",
            "Espátula"
        ]
    }


#endpoint que permite "crear" o recibir datos de una receta
@app.post("/receta")
def crear_receta(receta: Receta):
    return {
        "mensaje": "Receta recibida correctamente",
        "nombre_receta": receta.nombre,
        "ingredientes_recibidos": len(receta.ingredientes)
    }