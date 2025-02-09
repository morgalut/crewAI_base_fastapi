from sqlalchemy.orm import Session
from models import AgentModel, TaskModel

def save_agent(db: Session, name: str, role: str, goal: str, backstory: str, tasks: list):
    agent = AgentModel(name=name, role=role, goal=goal, backstory=backstory)
    db.add(agent)
    db.commit()
    db.refresh(agent)

    for task_desc in tasks:
        task = TaskModel(description=task_desc, agent_id=agent.id)
        db.add(task)

    db.commit()
    return agent

def get_agents(db: Session):
    return db.query(AgentModel).all()
