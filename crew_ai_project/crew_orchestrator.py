from crewai import Crew
from crew_ai_project.config import OllamaConfig
from crew_ai_project.tasks import TaskManager
import logging

# ✅ Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CrewOrchestrator:
    """Orchestrates CrewAI execution with proper error handling."""

    @staticmethod
    def execute_tasks():
        """Executes defined tasks with CrewAI and logs the execution process."""

        tasks = TaskManager.define_tasks()
        agents = list({task.agent for task in tasks})  # ✅ Extract unique agents

        crew = Crew(
            agents=agents,
            tasks=tasks,
            execution_mode="sequential",
            llm=OllamaConfig.get_llm_config()
        )

        try:
            logger.info("🚀 Crew execution started.")
            result = crew.kickoff()
            logger.info("✅ Crew execution completed successfully.")
            return result
        except Exception as e:
            logger.error(f"❌ CrewAI Execution Error: {e}", exc_info=True)
            return {"error": str(e)}
