from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.repositorios.repositorio_login import RepositorioLogin
from src.schemas.schemas import Login

router = APIRouter()

@router.post("/login/", status_code=status.HTTP_201_CREATED)
def criar_logins(login: Login, db: Session = Depends(get_db)):
    try:
        login_criado =  RepositorioLogin(db).criar(login)
        return login_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o login")
    
@router.get("/login/",status_code=status.HTTP_200_OK)
def listar_logins(db: Session = Depends(get_db)):
    try:
        login = RepositorioLogin(db).listar()
        return login
    except:
        raise HTTPException(status_code=404, detail="logins não encontrados")

@router.get("/login/{id}")
def listar_login_id(id:int,db: Session = Depends(get_db)):    
    try:    
        login = RepositorioLogin(db).listar_id(id)
        return login
    except:
        raise HTTPException(status_code=404, detail="login não encontrado")

@router.delete("/login/{id}")
def remover_login(id:int,db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioLogin(db)
        repositorio.remover(id)
        return {"message": "login removido com sucesso"}
    except:
        raise HTTPException(status_code=404, detail="login não encontrada")
