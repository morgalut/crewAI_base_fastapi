from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import save_agent, get_agents
from services import execute_tasks
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class TaskCreate(BaseModel):
    description: str

class AgentCreate(BaseModel):
    name: str
    role: str
    goal: str
    backstory: Optional[str] = None
    tasks: List[TaskCreate]  # Accepts multiple tasks per agent

@app.post("/agents/")
async def add_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    agent_obj = save_agent(db, agent.name, agent.role, agent.goal, agent.backstory, [task.description for task in agent.tasks])
    return {"message": "Agent created", "id": agent_obj.id}

@app.get("/agents/")
async def fetch_agents(db: Session = Depends(get_db)):
    return get_agents(db)

@app.post("/run-tasks/")
async def run_tasks():
    result = execute_tasks()
    return {"message": "Tasks executed", "result": result}
