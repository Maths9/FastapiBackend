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
async def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    try:  
        produto_criado = await RepositorioProduto(db).criar(produto)
        return produto_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o produto")

@app.get("/produtos", status_code=status.HTTP_200_OK)
async def listar_produtos(db: Session = Depends(get_db)):
    try:
        Produto = RepositorioProduto(db).listar()
        return Produto
    except:
        raise HTTPException(status_code=404, detail="Produtos não encontrados")
    
@app.get("/produtos/{id}", status_code=status.HTTP_200_OK) 
async def listar_produtos_id(id:int, db: Session = Depends(get_db)):  
    try:    
        Produto = RepositorioProduto(db).listar_id(id)
        return Produto
    except:
        raise HTTPException(status_code=404, detail="Produtos não encontrados")
    
@app.delete("/produtos/{id}")
async def remover_produto(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioProduto(db)
        repositorio.remover(id)
        return {"message": "Produto removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Produto não encontrado")  

@app.post('/usuarios', status_code=status.HTTP_201_CREATED)
async def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    try:
        usuario_criado = await RepositorioUsuario(db).criar(usuario)
        return usuario_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o usuário")
    
@app.get("/usuarios", status_code=status.HTTP_200_OK)
async def listar_usuarios(db: Session = Depends(get_db)):
    try:
        usuario = RepositorioUsuario(db).listar()
        return usuario
    except:
        raise HTTPException(status_code=404, detail="Usuários não encontrados")

@app.get("/usuarios/{id}", status_code=status.HTTP_200_OK)
async def listar_usuarios_id(id:int, db: Session = Depends(get_db)):
    try:
        usuario = RepositorioUsuario(db).listar_id(id)
        return usuario
    except:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/usuarios/{id}")
async def remover_usuario(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioUsuario(db)
        repositorio.remover(id)
        return {"message": "Usuario removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

@app.post("/mensagens/", status_code=status.HTTP_201_CREATED)
async def criar_mensagens(mensagem: Mensagem, db: Session = Depends(get_db)):
    try:
        mensagem_criada = await RepositorioMensagem(db).criar(mensagem)
        return mensagem_criada
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar a mensagem")
    
@app.get("/mensagens/",status_code=status.HTTP_200_OK)
async def listar_mensagens(db: Session = Depends(get_db)):
    try:
        mensagem = RepositorioMensagem(db).listar()
        return mensagem
    except:
        raise HTTPException(status_code=404, detail="Mensagens não encontradas")

@app.get("/mensagens/{id}")
async def listar_mensagens_id(id:int, str = "id" ,db: Session = Depends(get_db)):    
    try:    
        mensagem = RepositorioMensagem(db).listar_id(id)
        return mensagem
    except:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")

@app.delete("/mensagens/{id}")
async def remover_mensagens(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioMensagem(db)
        repositorio.remover(id)
        return {"message": "Mensagem removida com sucesso"}
    except:
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
