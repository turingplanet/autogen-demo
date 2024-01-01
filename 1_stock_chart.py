from autogen import AssistantAgent, UserProxyAgent


config_list = [
    {
        'model': 'gpt-4',
        'api_key': '<OPENAI_API_KEY>'
    }
]

assistant = AssistantAgent(
    "assistant",
    llm_config={
        "cache_seed": None,
        "config_list": config_list
    }
)

user_proxy = UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "1-stock-chart"}
)

user_proxy.initiate_chat(
    assistant,
    message="Plot a chart comparing the year-to-date (YTD) stock price changes of NVIDIA (NVDA) and Tesla."
)

