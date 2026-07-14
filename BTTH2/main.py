from fastapi import FastAPI, Depends, HTTPException
from IT215_SS17_BTTH1.BTTH1.database import engine, get_db, Base
from sqlalchemy import text
from sqlalchemy.orm import Session
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/database-health")
def db_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"message": "Database OK"}