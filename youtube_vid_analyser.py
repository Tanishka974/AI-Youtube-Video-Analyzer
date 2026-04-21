from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.openai import OpenAIResponses
from agno.tools.youtube import YouTubeTools

load_dotenv("api_key.env")

def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YouTubeTools()],
        instructions=dedent("""\
            You are an expert YouTube content analyst...
        """),
        add_datetime_to_context=True,
        markdown=True,
    )


agent = build_youtube_agent()

#agent.print_response(
    #"Analyze this video: https://www.youtube.com/watch?v=hoN7_VMzw_g&list=PLGF9VeuyJzDfFEeiK2N9NYhHedyEHQHxI&index=7",
    #stream=True,
#)