from langchain_community.agent_toolkits.openapi import planner
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain.requests import RequestsWrapper
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import yaml

load_dotenv(find_dotenv())

if __name__ == "__main__":
    """
    This script will ask a question to the OpenAPI agent for Pet Shop API.

    Example Questions:
    * I want to get all pets with status sold.
    * Tell me what are pet statuses in the store.
    * I want to get all pets with status sold.
    """
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)
    with open("./petshop_openapi.yaml") as f:
        raw_openai_api_spec = yaml.load(f, Loader=yaml.Loader)
        openai_api_spec = reduce_openapi_spec(raw_openai_api_spec)
        petsop_agent = planner.create_openapi_agent(
            api_spec=openai_api_spec,
            llm=llm,
            requests_wrapper=RequestsWrapper(),
            verbose=True,
            # return_intermediate_steps=True
        )
        user_query = "I want to get all pets with status sold."
        response = petsop_agent.run(user_query)
        print(f"response ${response}")
