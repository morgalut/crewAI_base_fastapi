import logging
from fastapi import FastAPI, HTTPException
from crew_ai_project.crew_orchestrator import CrewOrchestrator
from crew_ai_project.agent_storage import AgentCreate, add_agent, get_all_agents, AgentData

from uuid import uuid4  # ✅ Import UUID generator
from crew_ai_project.agent_storage import AgentCreate  # Add TaskCreate to imports

# Initialize FastAPI app
app = FastAPI()

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@app.post("/agents/")
async def create_agent(agent: AgentCreate):
    """Add an agent to the system."""
    try:
        agent_obj = AgentData(
            id=str(uuid4()),
            name=agent.name,
            role=agent.role,
            goal=agent.goal,
            backstory=agent.backstory,
            tasks=[task.description for task in agent.tasks],  # Extract descriptions
            restrictions=agent.restrictions
        )
        return add_agent(agent_obj)
    except Exception as e:
        logger.error(f"❌ Error adding agent: {e}")
        raise HTTPException(status_code=500, detail=f"Error adding agent: {e}")


@app.get("/agents/")
async def list_agents():
    """Fetch all agents."""
    try:
        return get_all_agents()
    except Exception as e:
        logger.error(f"❌ Error fetching agents: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching agents: {e}")


@app.post("/run-tasks/")
async def run_tasks():
    """
    Executes all defined CrewAI tasks in sequential order.

    Response:
    {
        "message": "Tasks executed",
        "result": {...}
    }
    """
    try:
        result = CrewOrchestrator.execute_tasks()
        logger.info("✅ Tasks executed successfully.")
        return {"message": "Tasks executed", "result": result}
    except Exception as e:
        logger.error(f"❌ Error running tasks: {e}")
        raise HTTPException(status_code=500, detail="Task execution failed")
