from crewai import Agent
from textwrap import dedent
from langchain.llms import Ollama
from langchain_openai import ChatOpenAI

#from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool


#search = DuckDuckGoSearchRun()       # Not reliable, times-out too frequently
search = WikipediaAPIWrapper()

# Web Search Tool
search_tool = Tool(
    name="Web Search",
    func=search.run,
    description="A useful tool for searching the Internet. Search text should be 5 or less words",
)

class BloggingAgents:
    def __init__(self):

        self.ollama_llm_openhermes = Ollama(model="openhermes")
        self.ollama_llm_mistral = Ollama(model="mistral")
        self.llm_lmstudio = ChatOpenAI(
                                        openai_api_base="http://localhost:1234/v1",
                                        openai_api_key="xxxx",                 
                                        model_name="mistral"
                                    )


    def researcher(self):
        return Agent(
                    role='Senior Researcher',
                    goal='Discover groundbreaking technologies',
                    backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.',
                    verbose=True,
                    tools=[search_tool],
                    allow_delegation=False,
                    max_iter=5,
                    llm=self.ollama_llm_openhermes
                )

    def insight_researcher(self):
        return Agent(
                    role='Insight Researcher',
                    goal='Discover Key Insights',
                    backstory='You are able to find key insights from the data you are given.',
                    verbose=True,
                    allow_delegation=False,
                    llm=self.ollama_llm_openhermes
                )

    def writer(self):
        return Agent(
                    role='Tech Content Strategist',
                    goal='Craft compelling content on tech advancements',
                    backstory="""You are a content strategist known for making complex tech topics interesting and easy to understand.""",
                    verbose=True,
                    allow_delegation=False,
                    llm=self.ollama_llm_mistral
                )

    def formatter(self):
        return Agent(
                    role='Markdown Formatter',
                    goal='Format the text in markdown',
                    backstory='You are able to convert the text into markdown format',
                    verbose=True,
                    allow_delegation=False,
                    llm=self.ollama_llm_mistral
                )

