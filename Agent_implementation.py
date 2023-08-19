from LLM import *
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper
from langchain.agents import initialize_agent
from langchain.agents import AgentType

zapier = ZapierNLAWrapper(zapier_nla_api_key="sk-ak-IOi22QQhkYLEphxT6ue8ASelM9")
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)


agent = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True)