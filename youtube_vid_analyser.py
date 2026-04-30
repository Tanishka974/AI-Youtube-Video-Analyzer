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
          You are a YouTube video analysis expert.

Your task:
1. Extract video metadata (title, duration, channel).
2. If transcript is available:
   - Summarize the video
   - Extract key concepts
   - Explain in simple language
3. If transcript is NOT available:
   - Clearly mention that analysis is limited
   - Provide insights based only on title and context

Always return structured output:
- Overview
- Key Insights
- Limitations 

Always use YouTubeTools to fetch video data before answering.
        """),
        add_datetime_to_context=True,
        markdown=True,
    )


agent = build_youtube_agent()

#agent.print_response(
    #"Analyze this video: https://www.youtube.com/watch?v=hoN7_VMzw_g&list=PLGF9VeuyJzDfFEeiK2N9NYhHedyEHQHxI&index=7",
    #stream=True,
#)
