# 4 steps to create chat bot for your API

Description how to create LLM chat bit for existing API using Langchain, Streamlit and Python.

## Start

1. Virtual Environment

> pipenv shell
> pipenv install

1. Update .env file
Use your OpenAI token
https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key

1. Start Chat application

> pipenv run streamlit run ./04-chatbot.py

1. Start chating

`Please list all names of pets in the store with status sold.`

## Packages

Main modules:
* langchain 
* tiktoken 
* langchain-community

## Example Petshop API:

Swagger UI: https://petstore.swagger.io/#/
> !wget https://petstore.swagger.io/v2/swagger.yaml -O petshop_openapi.yaml

## Readings

* (LangChaing)[https://www.langchain.com/]
* (OpenAPI Agent)[https://python.langchain.com/docs/integrations/toolkits/openapi]
* (Streamlit)[https://docs.streamlit.io/]
* (Pet Shop API)[https://petstore.swagger.io/#/]