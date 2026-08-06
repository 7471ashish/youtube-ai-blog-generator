from crewai import Agent, LLM
from dotenv import load_dotenv
from tools import yt_tool
load_dotenv()

llm = LLM(
    model="gpt-4o-mini"
)

researcher = Agent(
    role="YouTube Researcher",
    goal="Research about {topic}",
    backstory="Expert researcher.",
    tools=[yt_tool], 
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Blog Writer",
    goal="Write a blog on {topic}",
    backstory="Expert technical writer.",
    llm=llm,
    verbose=True
)