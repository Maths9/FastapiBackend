from tkinter.tix import STATUS
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.config.database import engine
from src.routers import rotas_produtos, rotas_usuarios, rotas_mensagens, rotas_login
   
criar_bd()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", 
                   "http://172.22.224.1:5173", "http://192.168.3.10:5173/"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(rotas_produtos.router)

app.include_router(rotas_usuarios.router)

app.include_router(rotas_mensagens.router)

app.include_router(rotas_login.router)


