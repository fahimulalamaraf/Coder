import uvicorn
from fastapi import FastAPI, HTTPException, Depends
import uvicorn
from sqlalchemy.sql.annotation import Annotated


import models.tasks
from .database.db import engine, sessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

models.tasks.Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/task")
async  def create_task(task: models.tasks.Task, db: Session = Depends(db_dependency)):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task






def main():
    print("Hello from phase-01!")
    uvicorn.run(app, host="localhost", port=8000)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    main()
