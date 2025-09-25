from fastapi import FastAPI
from sqlmodel import SQLModel
app = FastAPI()
class Usuario(SQLModel):
    nombre_usuario: str
    contrasena: str
usuarios_db = [
    {"nombre_usuario": "admin", "contrasena": "password123"},
    {"nombre_usuario": "user1", "contrasena": "1234"}
]
class UsuarioLogin(SQLModel):
    nombre_usuario: str
    contrasena: str
@app.get("/")
async def leer_raiz():
    return {"Hello": "World"}
@app.post("/login")
async def iniciar_sesion(usuario: UsuarioLogin):
    for u in usuarios_db:
        if usuario.nombre_usuario == u["nombre_usuario"] and usuario.contrasena == u["contrasena"]:
            return {"mensaje": "Login correcto"}
    return {"mensaje": "Credenciales inválidas"}

