from crewai import Crew
from tasks import TaskManager
from config import OllamaConfig  # ✅ Import Ollama config

def execute_tasks():
    """Executes defined tasks with CrewAI and handles any API authentication issues."""

    tasks = TaskManager.define_tasks()  # ✅ Corrected method call
    agents = list({task.agent for task in tasks})  # ✅ Extract unique agents

    crew = Crew(
        agents=agents,
        tasks=tasks,
        execution_mode="sequential",
        llm=OllamaConfig.get_llm_config()  # ✅ Corrected LLM config retrieval
    )

    try:
        result = crew.kickoff()
        return result
    except Exception as e:
        print(f"❌ Error executing CrewAI tasks: {e}")
        return {"error": str(e)}
