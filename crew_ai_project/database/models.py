from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from crew_ai_project.database.base import Base  # Import Base from base.py

class AgentModel(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    goal = Column(String, nullable=False)
    backstory = Column(String, nullable=True)

    tasks = relationship("TaskModel", back_populates="agent", cascade="all, delete-orphan")

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    description = Column(String, nullable=False)

    agent = relationship("AgentModel", back_populates="tasks")
