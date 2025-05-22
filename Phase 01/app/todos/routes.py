from fastapi import APIRouter, Depends,status, HTTPException
from todo_data import todos
from schemas import ToDo

from typing import Optional, List

book_router = APIRouter()

@book_router.get("/tasks", response_model=List[ToDo])
async def root():
    return todos


@book_router.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_tasks(todo_data: ToDo):
    new_todo = todo_data.model_dump()
    todos.append(new_todo)
    return todos


@book_router.get("/task/{task_id}")
async def get_task(task_id: int):
    for todo in todos:
        if todo['id'] == task_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
