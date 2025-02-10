from sqlalchemy.orm import Session
from crew_ai_project.database.models import AgentModel, TaskModel

def save_agent(db: Session, name: str, role: str, goal: str, backstory: str, tasks: list):
    """Saves an agent and its tasks to the database."""
    try:
        agent = AgentModel(name=name, role=role, goal=goal, backstory=backstory)
        db.add(agent)
        db.commit()
        db.refresh(agent)

        for task_desc in tasks:
            task = TaskModel(description=task_desc, agent_id=agent.id)
            db.add(task)

        db.commit()
        return agent
    except Exception as e:
        db.rollback()
        print(f"❌ Database error: {e}")
        return None

def get_agents(db: Session):
    """Fetches all agents from the database."""
    return db.query(AgentModel).all()
