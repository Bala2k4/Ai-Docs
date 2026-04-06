from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Document
from app.s3 import upload_to_s3
import uuid

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_id = str(uuid.uuid4())
    filename = f"uploads/{file_id}_{file.filename}"

    file_url = upload_to_s3(file.file, filename)

    doc = Document(file_url=file_url)
    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {
        "message": "Upload successful",
        "file_url": file_url,
        "id": doc.id
    }