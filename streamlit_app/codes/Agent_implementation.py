import os
from dotenv import load_dotenv
from LLM import *
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper
from langchain.agents import initialize_agent
from langchain.agents import AgentType

# Specify the path to the .env file and load environment variables from it
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Fetch the API key from environment variables
zapier_nla_api_key = os.getenv("ZAPIER_NLA_API_KEY")

zapier = ZapierNLAWrapper(zapier_nla_api_key=zapier_nla_api_key)
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)

agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)