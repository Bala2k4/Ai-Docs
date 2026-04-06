from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Document

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("/")
def get_documents(db: Session = Depends(get_db)):
    docs = db.query(Document).all()
    return docs