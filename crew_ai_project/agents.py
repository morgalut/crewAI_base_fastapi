from crewai import Agent

def create_agents():
    researcher = Agent(
        name="Researcher",
        role="Data Analyst",
        goal="Gather data on IoT events and generate insights.",
        backstory="Expert in data collection and analysis."
    )

    writer = Agent(
        name="Writer",
        role="Technical Content Creator",
        goal="Translate insights into well-structured reports.",
        backstory="A professional technical writer."
    )

    return [researcher, writer]
