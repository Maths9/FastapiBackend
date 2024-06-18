from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.repositorios.mensagem import RepositorioMensagem
from src.schemas.schemas import Mensagem

router = APIRouter()

@router.post("/mensagens/", status_code=status.HTTP_201_CREATED)
def criar_mensagens(mensagem: Mensagem, db: Session = Depends(get_db)):
    try:
        mensagem_criada =  RepositorioMensagem(db).criar(mensagem)
        return mensagem_criada
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar a mensagem")
    
@router.get("/mensagens/",status_code=status.HTTP_200_OK)
def listar_mensagens(db: Session = Depends(get_db)):
    try:
        mensagem = RepositorioMensagem(db).listar()
        return mensagem
    except:
        raise HTTPException(status_code=404, detail="Mensagens não encontradas")

@router.get("/mensagens/{id}")
def listar_mensagens_id(id:int,db: Session = Depends(get_db)):    
    try:    
        mensagem = RepositorioMensagem(db).listar_id(id)
        return mensagem
    except:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")

@router.delete("/mensagens/{id}")
def remover_mensagens(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioMensagem(db)
        repositorio.remover(id)
        return {"message": "Mensagem removida com sucesso"}
    except:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
