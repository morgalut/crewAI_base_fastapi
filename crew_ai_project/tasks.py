from crewai import Task
from crew_ai_project.agents import AgentManager

class BaseTask:
    """Base class for all CrewAI tasks."""

    def __init__(self, description, agent, expected_output):
        self.description = description
        self.agent = agent
        self.expected_output = expected_output

    def create_task(self, output_handler=None):
        """Creates a CrewAI task instance."""
        return Task(
            description=self.description,
            agent=self.agent,
            expected_output=self.expected_output,
            output_handler=output_handler
        )

class DataCollectionTask(BaseTask):
    """Task for collecting IoT event logs."""

    def __init__(self, agent):
        super().__init__(
            description="Collect IoT event logs from sensors.",
            agent=agent,
            expected_output="Raw IoT event data"
        )

class DataProcessingTask(BaseTask):
    """Task for processing IoT event logs."""

    def __init__(self, agent, previous_result):
        super().__init__(
            description=f"Process IoT data: {previous_result}",
            agent=agent,
            expected_output="Insights from IoT logs"
        )

class TaskManager:
    """Manages task creation and execution."""

    @staticmethod
    def define_tasks():
        """Defines and sequences tasks for CrewAI."""
        agents = AgentManager.get_agents()
        
        first_task = DataCollectionTask(agents[0]).create_task(
            output_handler=lambda result: TaskManager.create_followup_task(result, agents, 1)
        )
        
        return [first_task]

    @staticmethod
    def create_followup_task(previous_result, agents, next_agent_index):
        """Creates the next task in the sequence."""
        if next_agent_index >= len(agents):
            return None  # Stop if all agents have completed their tasks

        return DataProcessingTask(agents[next_agent_index], previous_result).create_task(
            output_handler=lambda result: TaskManager.create_followup_task(result, agents, next_agent_index + 1)
        )
