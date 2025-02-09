from crewai import Task, Agent  # Import CrewAI Agent
from sqlalchemy.orm import Session
from database import SessionLocal
from models import AgentModel, TaskModel

def convert_to_crewai_agent(agent_model):
    """Convert an AgentModel instance into a CrewAI Agent."""
    return Agent(
        name=agent_model.name,
        role=agent_model.role,
        goal=agent_model.goal,
        backstory=agent_model.backstory or "No backstory provided."
    )

def define_tasks():
    db: Session = SessionLocal()
    
    agents = db.query(AgentModel).all()
    tasks = []

    for agent in agents:
        agent_tasks = db.query(TaskModel).filter(TaskModel.agent_id == agent.id).all()
        crew_agent = convert_to_crewai_agent(agent)  # ✅ Convert ORM Agent to CrewAI Agent

        for task in agent_tasks:
            tasks.append(Task(
                description=task.description,
                agent=crew_agent,  # ✅ Assign a CrewAI agent, not an ORM object
                expected_output=f"Completion of task: {task.description}"  # ✅ Fix: Add expected_output
            ))

    db.close()
    return tasks
