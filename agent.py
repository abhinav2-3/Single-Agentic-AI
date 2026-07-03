import os
import certifi
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

from weather import get_weather_data

# from langchain_core.utils import SecretStr

os.environ["SSL_CERT_FILE"] = certifi.where()
load_dotenv()

GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY: str | None = os.getenv("TAVILY_API_KEY")

# print("GROQ_API_KEY : ", GROQ_API_KEY)
# print("TAVILY_API_KEY : ", TAVILY_API_KEY)
# api_key=SecretStr(GROQ_API_KEY) if GROQ_API_KEY else None

search_tool = TavilySearchResults(max_results=2)

# result = search_tool.invoke("Capital of Uttar Pradesh")
# print("Result :  ", result)


# LLM ===============

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7, api_key=GROQ_API_KEY)

# result2 = llm.invoke("What year it is?")
# print("Result 2 :  ", result2.content)

prompt = hub.pull("hwchase17/react")
# print(prompt)

tools = []

agent = create_react_agent(llm, tools, prompt)

agent_executer = AgentExecutor(agent=agent, tools=tools, verbose=True)

response = agent_executer.invoke(
    {
        "input": (
            "Where is Red fort is situated in India",
            "What is the weather of Varanasi, U.P",
        )
    }
)

# print(response)
print(response["output"])
