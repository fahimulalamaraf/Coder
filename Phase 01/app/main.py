from typing import List

from fastapi import FastAPI, status, HTTPException, Depends
import uvicorn
from pydantic import BaseModel
from sqlalchemy.orm import defer

app = FastAPI()


class ToDo(BaseModel):
    id: int
    name: str
    description: str
    completed: bool


def main():
    print("Hello from phase-01!")
    uvicorn.run(app, host="localhost", port=8000)


todos = [
    {"id": 1, "name": "Buy groceries", "description": "Milk, Eggs, Bread, and Fruits", "completed": False},
    {"id": 2, "name": "Finish report", "description": "Complete the monthly sales report", "completed": False},
    {"id": 3, "name": "Workout", "description": "1-hour gym session with cardio and strength training", "completed": True},
    {"id": 4, "name": "Call mom", "description": "Catch up with mom on the phone", "completed": False},
    {"id": 5, "name": "Water plants", "description": "Water all indoor and outdoor plants", "completed": True},
    {"id": 6, "name": "Book flight", "description": "Book tickets for the upcoming vacation", "completed": False},
    {"id": 7, "name": "Read book", "description": "Read 50 pages of 'Atomic Habits'", "completed": False},
    {"id": 8, "name": "Pay electricity bill", "description": "Pay the utility bill before due date", "completed": True},
    {"id": 9, "name": "Plan weekend trip", "description": "Research and plan a short weekend getaway", "completed": False},
    {"id": 10, "name": "Clean kitchen", "description": "Deep clean stove, counters, and fridge", "completed": True},
    {"id": 11, "name": "Meeting with team", "description": "Weekly sync-up with project team", "completed": True},
    {"id": 12, "name": "Practice Python", "description": "Work on FastAPI and database models", "completed": False},
    {"id": 13, "name": "Buy birthday gift", "description": "Find a nice present for Sarah's birthday", "completed": False},
    {"id": 14, "name": "Submit tax documents", "description": "Send required files to the accountant", "completed": True},
    {"id": 15, "name": "Fix bike", "description": "Repair the flat tire and oil the chain", "completed": False},
    {"id": 16, "name": "Grocery inventory", "description": "Check pantry for stock and expiry dates", "completed": True},
    {"id": 17, "name": "Write blog post", "description": "Draft and edit blog about productivity hacks", "completed": False},
    {"id": 18, "name": "Organize files", "description": "Clean up and reorganize computer folders", "completed": False},
    {"id": 19, "name": "Dentist appointment", "description": "Annual dental check-up at 3 PM", "completed": True},
    {"id": 20, "name": "Prepare slides", "description": "Make presentation slides for Monday’s meeting", "completed": False},
    {"id": 21, "name": "Renew license", "description": "Renew driver’s license online", "completed": True},
    {"id": 22, "name": "Laundry", "description": "Wash, dry, and fold clothes", "completed": False},
    {"id": 23, "name": "Buy dog food", "description": "Visit pet store for supplies", "completed": False},
    {"id": 24, "name": "Yoga session", "description": "Attend morning yoga class", "completed": True},
    {"id": 25, "name": "Write thank you notes", "description": "Send emails to event attendees", "completed": False},
    {"id": 26, "name": "Study SQL", "description": "Practice queries and joins using Sakila DB", "completed": False},
    {"id": 27, "name": "Meal prep", "description": "Cook meals for the week ahead", "completed": False},
    {"id": 28, "name": "Car wash", "description": "Take the car for a wash and vacuum", "completed": True},
    {"id": 29, "name": "Research new phone", "description": "Compare models and prices", "completed": False},
    {"id": 30, "name": "Declutter desk", "description": "Throw out old papers and organize drawers", "completed": True}
]



@app.get("/tasks", response_model=List[ToDo])
async def root():
    return todos


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_tasks(todo_data: ToDo):
    new_todo = todo_data.model_dump()
    todos.append(new_todo)
    return todos


@app.get("/task/{task_id}")
async def get_task(task_id: int):
    for todo in todos:
        if todo['id'] == task_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


if __name__ == "__main__":
    main()
