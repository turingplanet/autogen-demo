import autogen

config_dict = {
    "seed": 42,  
    "config_list": [{
        'model': 'gpt-4',
        'api_key': '<OPENAI_API_KEY>'
    }]
}

user_proxy = autogen.UserProxyAgent(
   name="user_proxy",
   human_input_mode="ALWAYS",
   system_message="A human administrator will provide the idea and execute the code developed by the programmer.",
   code_execution_config={"work_dir": "2-tic-tac-toe"},
)

pm = autogen.AssistantAgent(
    name="product_manager",
    llm_config=config_dict,
    system_message="""
    A project manager who will assist in decomposing the initial idea into a well-defined requirement for the coder; 
    will not be involved in subsequent discussions or error resolution.",
    """
)

programmer = autogen.AssistantAgent(
    name="programmer",
    llm_config=config_dict,
    system_message="Responsible for writing code in accordance with the project's defined requirements."
)

group_chat = autogen.GroupChat(agents=[user_proxy, pm, programmer], messages=[], max_round=50)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=config_dict)

user_proxy.initiate_chat(
    manager,
    message="Develop a classic Tic-Tac-Toe game using Python3 and PyQt."
)



