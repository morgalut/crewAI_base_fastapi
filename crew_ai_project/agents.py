from crewai import Agent
from crew_ai_project.config import OllamaConfig
from crew_ai_project.agent_storage import load_agents

class BaseAgent:
    """Base class for all CrewAI agents."""

    def __init__(self, name, role, goal, backstory):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = OllamaConfig.get_llm_config()

    def create_agent(self):
        """Creates a CrewAI agent instance."""
        return Agent(
            name=self.name,
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            llm=self.llm
        )
class ResearcherAgent(BaseAgent):
    """AI agent responsible for analyzing IoT event logs."""

    def __init__(self):
        super().__init__(
            name="Researcher",
            role="Data Analyst",
            goal="Gather IoT event logs and analyze patterns.",
            backstory="Expert in AI-driven data analysis."
        )

class WriterAgent(BaseAgent):
    """AI agent responsible for summarizing AI-generated insights."""

    def __init__(self):
        super().__init__(
            name="Writer",
            role="Technical Content Creator",
            goal="Summarize insights into structured reports.",
            backstory="Specialized in AI-generated documentation."
        )
class AgentManager:
    """Manages all CrewAI agents."""

    @staticmethod
    def get_agents():
        """Load agents from JSON storage."""
        agent_data_list = load_agents()
        return [BaseAgent(agent.name, agent.role, agent.goal, agent.backstory).create_agent() for agent in agent_data_list]
