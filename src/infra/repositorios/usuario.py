from sqlalchemy.orm import Session
from src.schemas import schemas
from src.models import models


class RepositorioUsuario():
    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(id = usuario.id, nome = usuario.nome, telefone = usuario.telefone)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    
    def listar(self):
        usuario = self.db.query(models.Usuario).all()
        return usuario
    