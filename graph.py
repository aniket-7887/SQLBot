from langchain.agents import create_agent
from utils import tools, react_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv

sql_agent = create_agent(
    model=ChatGoogleGenerativeAI(model='gemini-2.0-flash'),
    tools=[tools.execute_sql_query, tools.get_schema],
    system_prompt=react_prompt.prompt1
)
