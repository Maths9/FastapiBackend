from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas.schemas import Usuario

router = APIRouter()

@router.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    try:
        usuario_criado = RepositorioUsuario(db).criar(usuario)
        return usuario_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o usuário")
    
@router.get("/usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    try:
        usuario = RepositorioUsuario(db).listar()
        return usuario
    except:
        raise HTTPException(status_code=404, detail="Usuários não encontrados")

@router.get("/usuarios/{id}", status_code=status.HTTP_200_OK)
def listar_usuarios_id(id:int, db: Session = Depends(get_db)):
    try:
        usuario = RepositorioUsuario(db).listar_id(id)
        return usuario
    except:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.delete("/usuarios/{id}")
def remover_usuario(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioUsuario(db)
        repositorio.remover(id)
        return {"message": "Usuario removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")