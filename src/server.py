from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.schemas.schemas import Produto, Usuario
from src.infra.repositorios.produto import RepositorioProduto
from src.infra.repositorios.usuario import RepositorioUsuario

criar_bd()
app = FastAPI()

@app.post('/produtos')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/usuarios')
def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).listar()
    return usuario