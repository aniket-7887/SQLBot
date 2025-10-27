from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import mysql.connector as connector
from dotenv import load_dotenv
import os
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

LLM = GoogleGenerativeAI(
    model='gemini-2.0-flash',
    google_api_key = GOOGLE_API_KEY,
    top_p=0.8
)

EMBEDDING = GoogleGenerativeAIEmbeddings(
    model='gemini-embedding-001',
    google_api_key = GOOGLE_API_KEY,
    output_dimensions=3072
)

# Pinecone Vector Store configuration
pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
index = pc.Index(os.getenv('INDEX_NAME'))
PINECONE = PineconeVectorStore(
    index=index,
    embedding=EMBEDDING
)

def get_db_connection():
    try:
        conn = connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password='',
            database=os.getenv("DATABASE")
        )
        return conn
    except:
        return "error while connecting the database!!!!"
    