from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from ..schemas.client import ClientCreate, ClientUpdate, ClientOut
from ..dependencies import get_db, get_current_user
from ..crud import client as crud_client

router = APIRouter()

@router.post("/clients", response_model=ClientOut, status_code=status.HTTP_201_CREATED)
def create_client(client: ClientCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud_client.create_client(db, client)

@router.get("/clients/{client_id}", response_model=ClientOut)
def get_client(client_id: int = Path(..., gt=0), db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_client = crud_client.get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.put("/clients/{client_id}", response_model=ClientOut)
def update_client(client_id: int, updated_client: ClientUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_client = crud_client.update_client(db, client_id, updated_client)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    deleted_client = crud_client.delete_client(db, client_id)
    if deleted_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"detail": "Client deleted successfully"}
