from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if __name__ == "__main__":
    """This script will ask a simple question to the GPT-3.5-turbo model."""
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)
    response = llm.invoke("how can langsmith help with testing?")
    print(response)
