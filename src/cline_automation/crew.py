import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

# Load environment variables from .env file
load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class DietPlanCrew():
    """DietPlanCrew crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        # Initialize the LLM using environment variables
        self.llm = LLM(
            model=os.environ.get("MODEL"),
            api_key=os.environ.get("GEMINI_API_KEY")
        )

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def diet_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['diet_planner'],
            llm=self.llm,
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def diet_plan_task(self) -> Task:
        # The context dictionary will be populated by the inputs provided to the kickoff method
        return Task(
            config=self.tasks_config['diet_plan_task'],
            agent=self.diet_planner(), # Pass the agent instance
            # context=context # Context is implicitly passed if the task description uses placeholders like {gender}
            output_file='diet_plan.md' # Save the output to a markdown file
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DietPlanCrew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=[self.diet_planner()], # Pass agent instances
            tasks=[self.diet_plan_task()], # Pass task instances
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
