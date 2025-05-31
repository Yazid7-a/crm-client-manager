from sqlalchemy.orm import Session
from ..models.client import Client
from ..schemas.client import ClientCreate, ClientUpdate

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db: Session, client_id: int, updated_client: ClientUpdate):
    db_client = get_client(db, client_id)
    if db_client is None:
        return None
    for field, value in updated_client.dict(exclude_unset=True).items():
        setattr(db_client, field, value)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if db_client is None:
        return None
    db.delete(db_client)
    db.commit()
    return db_client
