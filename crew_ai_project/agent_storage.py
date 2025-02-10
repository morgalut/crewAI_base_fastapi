import json
import os
import uuid
from typing import List, Dict, Optional
from pydantic import BaseModel

# Define storage directory for agents
data_dir = "crew_ai_project/data/agents"
os.makedirs(data_dir, exist_ok=True)

# Define agent model
class AgentData(BaseModel):
    id: str
    name: str
    role: str
    goal: str
    backstory: Optional[str] = None
    tasks: List[str]
    restrictions: Optional[List[str]] = []  # Ensure restrictions is always a list

def get_agent_file_path(agent_id: str) -> str:
    """Generate file path for an agent's JSON file."""
    return os.path.join(data_dir, f"{agent_id}.json")

def load_agents() -> List[AgentData]:
    """Load all agents from individual JSON files."""
    agents = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            with open(os.path.join(data_dir, filename), "r") as f:
                agents.append(AgentData(**json.load(f)))
    return agents

def save_agent(agent: AgentData):
    """Save an agent to its own JSON file."""
    agent_file = get_agent_file_path(agent.id)
    with open(agent_file, "w") as f:
        json.dump(agent.dict(), f, indent=4)

def add_agent(agent: AgentData) -> Dict[str, str]:
    """Add a new agent to storage with a unique ID."""
    agent.id = str(uuid.uuid4())  # Generate a unique ID for each agent
    save_agent(agent)
    return {"message": "Agent created", "id": agent.id}

def get_all_agents() -> List[AgentData]:
    """Retrieve all stored agents."""
    return load_agents()

class TaskCreate(BaseModel):
    description: str

class AgentCreate(BaseModel):
    name: str
    role: str
    goal: str
    backstory: Optional[str] = None
    tasks: List[TaskCreate]  # Change from List[str] to List[TaskCreate]
    restrictions: Optional[List[str]] = []# Ensure restrictions is included in AgentCreate


