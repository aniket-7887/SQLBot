from langchain_pinecone import Pinecone
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from .state import ThisIsState
import os
from utils.connections import LLM, PINECONE, get_db_connection
from utils.prompt import build_prompt
INDEX_NAME = os.getenv('INDEX_NAME')

def fetch_context(state: ThisIsState) -> dict:
    try:
        # vector_store = PINECONE.from_existing_index(INDEX_NAME, EMBEDDING)
        raw_context = PINECONE.similarity_search_with_relevance_scores(query=state['user_query'], k=5)
        context = [item[0].page_content for item in raw_context]
        return {'db_schema': context}
    except Exception as e:
        print(e)
        return 'Error while fetching database schema!!!'   

def generate_sql_query(state: ThisIsState) -> dict:
    try:
        prompt = build_prompt(state=state)
        response = LLM.invoke(input=prompt)
        sql_query = response.content if hasattr(response, "content") else str(response)
        if str(sql_query).startswith("```"):
            temp = str(sql_query[6:])
            temp = str(temp[:-4])
            return {'sql_query': temp.strip()}
        return {'sql_query': sql_query.strip()}
    except:
        return 'Error while fetching query!!!'

def execute_sql_query(state: ThisIsState) -> list:
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(state['sql_query'])
        return {'data': cursor.fetchall()}
    except:
        return "error while ecxecuting the query!!!"

def present_data(state: ThisIsState) -> str:
    try:
        # Here we have used another google api due to api rate limiting, if you don't have rate limiting problem, you can use same LLM
        llm = ChatGoogleGenerativeAI(
            model = 'gemini-2.0-flash',
            google_api_key = os.getenv("MY_ENV"),
            top_p = 0.3
        )
        prompt_template = ChatPromptTemplate.from_messages([
            ('system', '''Represent the following data returned from the database to natural language.
             The data is generated using this user query: {query}.'''),
            ('user', 'Data: {data}')
        ])
        return {'result': llm.invoke(prompt_template.invoke({'query': state['user_query'], 'data': state['data']})).content}
    except:
        return "error while presenting data in natural language!!!"
