from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.schemas.schemas import Produto, Usuario, Mensagem
from src.infra.repositorios.produto import RepositorioProduto
from src.infra.repositorios.usuario import RepositorioUsuario
from src.infra.repositorios.mensagem import RepositorioMensagem
from src.infra.sqlalchemy.config.database import engine
   
# criar_bd()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post('/produtos', status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    try:  
        produto_criado = RepositorioProduto(db).criar(produto)
        return produto_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o produto")

@app.get("/produtos", status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    try:
        Produto = RepositorioProduto(db).listar()
        return Produto
    except:
        raise HTTPException(status_code=404, detail="Produtos não encontrados")
    
@app.delete("/produtos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_produto(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioProduto(db)
        repositorio.remover(id)
        return {"message": "Produto removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Produto não encontrado")  

@app.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    try:
        usuario_criado = RepositorioUsuario(db).criar(usuario)
        return usuario_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o usuário")
    
@app.get("/usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    try:
        usuario = RepositorioUsuario(db).listar()
        return usuario
    except:
        raise HTTPException(status_code=404, detail="Usuários não encontrados")
    
@app.delete("/usuarios/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_usuario(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioUsuario(db)
        repositorio.remover(id)
        return {"message": "Usuario removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

@app.post("/mensagens/", status_code=status.HTTP_201_CREATED)
def criar_mensagens(mensagem: Mensagem, db: Session = Depends(get_db)):
    try:
        mensagem_criada = RepositorioMensagem(db).criar(mensagem)
        return mensagem_criada
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar a mensagem")
    
@app.get("/mensagens/",status_code=status.HTTP_200_OK)
def listar_mensagens(db: Session = Depends(get_db)):
    try:
        mensagem = RepositorioMensagem(db).listar()
        return mensagem
    except:
        raise HTTPException(status_code=404, detail="Mensagens não encontradas")

@app.delete("/mensagens/{id}")
def remover_mensagens(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioMensagem(db)
        repositorio.remover(id)
        return {"message": "Mensagem removida com sucesso"}
    except:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
