from fastapi import FastAPI
from app.database import Base, engine
from app.routes import upload, documents

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Document System")

app.include_router(upload.router)
app.include_router(documents.router)

@app.get("/")
def root():
    return {"message": "API is running"}