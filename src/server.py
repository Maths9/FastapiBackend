from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import get_db, criar_bd
<<<<<<< HEAD
from src.schemas.schemas import Produto, Usuario, Mensagem, Login
from src.infra.repositorios.produto import RepositorioProduto
from src.infra.repositorios.usuario import RepositorioUsuario
from src.infra.repositorios.mensagem import RepositorioMensagem
from src.infra.repositorios.login import RepositorioLogin
=======
>>>>>>> 7b4c28b9ef00b3b1618b88f6b27a9577b5bb9ed7
from src.infra.sqlalchemy.config.database import engine
from src.routers import rotas_produtos, rotas_usuarios, rotas_mensagens, rotas_login
   
<<<<<<< HEAD
=======
   
>>>>>>> 7b4c28b9ef00b3b1618b88f6b27a9577b5bb9ed7
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

<<<<<<< HEAD
@app.post('/usuarios/', status_code=status.HTTP_201_CREATED)
async def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db)):
    try:
        usuario_criado = await RepositorioUsuario(db).criar(usuario)
        return usuario_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o usuário")
    
@app.get("/usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
        usuario = RepositorioUsuario(db).listar()
        return usuario
    

@app.get("/usuarios/{id}", status_code=status.HTTP_200_OK)
async def listar_usuarios_id(id:int, db: Session = Depends(get_db)):
        usuario = RepositorioUsuario(db).listar_id(id)
        return usuario
    
@app.delete("/usuarios/{id}")
async def remover_usuario(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioUsuario(db)
        repositorio.remover(id)
        return {"message": "Usuario removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    
@app.post('/logins/', status_code=status.HTTP_201_CREATED)
async def criar_login(login: Login, db: Session = Depends(get_db)):
    try:
        login_criado = await RepositorioLogin(db).criar(login)
        return login_criado
    except:
        raise HTTPException(status_code=400, detail="Erro ao criar o login")
    
@app.get("/logins", status_code=status.HTTP_200_OK)
async def listar_logins(db: Session = Depends(get_db)):
    try:
        login = RepositorioLogin(db).listar()
        return login
    except:
        raise HTTPException(status_code=404, detail="Logins não encontrados")
    
@app.get("/logins/{id}", status_code=status.HTTP_200_OK)
async def listar_logins_id(id:int, db: Session = Depends(get_db)):
    try:
        login = RepositorioLogin(db).listar_id(id)
        return login
    except:
        raise HTTPException(status_code=404, detail="Login não encontrado")
    
@app.delete("/logins/{id}")
async def remover_login(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioLogin(db)
        repositorio.remover(id)
        return {"message": "Login removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Login não encontrado")
    
@app.delete("/logins/{id}")
async def remover_login(id:int, db: Session = Depends(get_db)):
    try:
        repositorio = RepositorioLogin(db)
        repositorio.remover(id)
        return {"message": "Login removido com sucesso"} 
    except:
        raise HTTPException(status_code=404, detail="Login não encontrado")
    

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
=======
app.include_router(rotas_mensagens.router)

app.include_router(rotas_login.router)

>>>>>>> 7b4c28b9ef00b3b1618b88f6b27a9577b5bb9ed7
