import os
from crewai import Crew
from tasks import define_tasks

# Ensure the API key is set
os.environ["OPENAI_API_KEY"] = "api_key"

def execute_tasks():
    tasks = define_tasks()
    
    # Extract unique agents from tasks
    agents = list({task.agent for task in tasks})

    crew = Crew(
        agents=agents,
        tasks=tasks
    )

    result = crew.kickoff()
    return result
