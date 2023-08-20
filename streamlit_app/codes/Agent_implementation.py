from codes.LLM import *
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from Keys import *
# from dotenv import load_dotenv

# dotenv_path = os.path.join(os.path.dirname(os.getcwd()),'.env.sample')
# load_dotenv(dotenv_path=dotenv_path)

# # Fetch the API key from environment variables
# zapier_nla_api_key = "sk-ak-IOi22QQhkYLEphxT6ue8ASelM9"



zapier = ZapierNLAWrapper(zapier_nla_api_key=ZAPIER_API_KEY)
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)


agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True)
