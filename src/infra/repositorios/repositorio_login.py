from sqlalchemy.orm import Session
from src.schemas import schemas
from src.models import models
from sqlalchemy import delete
from src.models.models import Base, engine
from sqlalchemy import delete
from src.infra.repositorios import repositorio_login

class RepositorioLogin():
    def __init__(self, db: Session):
        self.db = db
        
    def criar(self, login: schemas.Login):
        db_login = models.Login(id = login.id, login = login.login)
        self.db.add(db_login)
        self.db.commit()
        self.db.refresh(db_login)
        return db_login
    
    def listar(self):
        login = self.db.query(models.login).all()
        return login
    
    def listar_id(self, id:int):
        login = self.db.query(models.login).filter(models.login.id == id).first()
        return login
    
    def remover(self, id:int):
        delete_login = delete(models.login).where(models.login.id == id)
        self.db.execute(delete_login)
        self.db.commit()