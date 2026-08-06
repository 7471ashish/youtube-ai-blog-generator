from crewai import Task
from agents import researcher, writer


research_task = Task(
    description="""
    Search YouTube for {topic}.
    Read transcript.
    Summarize important concepts.
    """,
    expected_output="Research Notes",
    agent=researcher
)

write_task = Task(
    description="""
    Using the research,
    write a detailed markdown blog with headings,
    examples,
    conclusion,
    and key takeaways.
    """,
    expected_output="Markdown blog.",
    agent=writer,
    output_file="new-blog.md"
)