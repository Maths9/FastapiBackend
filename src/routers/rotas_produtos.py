from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.repositorios.produto import RepositorioProduto
from src.schemas.schemas import Produto, Mensagem

router = APIRouter()

@router.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    try:  
        produto_criado = RepositorioProduto(db).criar(produto)
        return produto_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o produto")

@router.get("/produtos", status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    try:
        Produto = RepositorioProduto(db).listar()
        return Produto
    except:
        raise HTTPException(status_code=404, detail="Produtos não encontrados")
    
@router.get("/produtos/{id}", status_code=status.HTTP_200_OK) 
def listar_produtos_id(id:int, db: Session = Depends(get_db)):  
    try:    
        Produto = RepositorioProduto(db).listar_id(id)
        return Produto
    except:
        raise HTTPException(status_code=404, detail="Produtos não encontrados")
    
@router.delete("/produtos/{id}")
def remover_produto(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioProduto(db)
        repositorio.remover(id)
        return {"message": "Produto removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Produto não encontrado")  