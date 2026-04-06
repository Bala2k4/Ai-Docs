from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentResponse(BaseModel):
    id: int
    file_url: str
    extracted_data: Optional[dict]
    created_at: datetime

    class Config:
        from_attributes = True