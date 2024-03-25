import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain_community.agent_toolkits.openapi import planner
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain.requests import RequestsWrapper
from langchain_openai import ChatOpenAI
import yaml

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

"""
This script will ask a question to the OpenAPI agent for Pet Shop API.

Example Questions:
* Tell me what are pet statuses in the store.
* Please list all names of pets in the store with status sold.
"""

@st.cache_resource
def load_model():
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.0)
    with open("./petshop_openapi.yaml") as f:
        raw_openai_api_spec = yaml.load(f, Loader=yaml.Loader)
        openai_api_spec = reduce_openapi_spec(raw_openai_api_spec)
        return planner.create_openapi_agent(
            api_spec=openai_api_spec,
            llm=llm,
            requests_wrapper=RequestsWrapper(),
            verbose=True,
        )


if __name__ == "__main__":
    agent = load_model()
    with st.sidebar:
        """
        ## Resources
         * [OpenApi Module](https://platform.openai.com/account/api-keys)
         * [Streamlit](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)
         * [Langchain](http://langchain.com)
        """

    st.title("API Chatbot for Pet Shop API")
    st.caption("A LLM chatbot powered by Langchain.")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        with st.spinner("Generating response..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = agent.invoke(prompt)
            msg = response["output"]
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)
