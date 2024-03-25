import yaml
import tiktoken
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec

if __name__ == "__main__":
    """This script will describe the OpenAPI spec and the number of tokens in the raw OpenAPI spec."""
    with open("./petshop_openapi.yaml") as f:
        raw_content = f.read()
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo").encode(raw_content)
        print(f"Raw OpenAPI spec has {len(encoding)} tokens")

        raw_petshop_api_spec = yaml.load(raw_content, Loader=yaml.Loader)
        endpoints = [
            (route, operation)
            for route, operations in raw_petshop_api_spec["paths"].items()
            for operation in operations
            if operation in ["get", "post"]
        ]
        print(f"Found {len(endpoints)} endpoints")
