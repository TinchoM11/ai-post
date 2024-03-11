import os
from autogen import ConversableAgent
from autogen import GroupChat
from autogen import GroupChatManager
import get_initial_post

import config

content_creator = ConversableAgent(
    "post_creator",
    system_message="You are a content media creator at a blockchain company called SPHEREONE"
    "You create posts for social media, but they must be reviewed by the company's content manager. "
    "You ask the editor to review the post and make any necessary corrections. "
    "You know that the post needs to be reviewed by both the content manager and the SEO expert."
    "Once analyzed, you deliver the final post for publication without any other description or comment. Just the post",

    llm_config=config.llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
)

content_manager = ConversableAgent(
    "post_editor",
    system_message="You are the content manager at a blockchain company called SPHEREONE"
    "You correct whatever you deem necessary, as you are an expert in engagement and organic positioning."
    "Just send the post with your suggestions. Don't add any description. Just the post"
    "You ask the SEO expert to review the post and make any necessary corrections."
    "Once analyzed, you deliver the final post for publication without any other description or comment. Just the post",
    llm_config=config.llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
)

seo_expert = ConversableAgent(
    "seo_expert",
    system_message="You are the SEO expert at a blockchain company called SPHEREONE"
    "Before making any posts, you analyze the keywords that should be used. "
    "You have extensive expertise in keyword usage, positioning, and content optimization. "
    "Once analyzed, you deliver the final post for publication without any other description or comment. Just the post"
    "Add the word 'TERMINATE' to end the conversation.",
    llm_config=config.llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
)

group_chat = GroupChat(
    agents=[content_creator, content_manager, seo_expert],
    messages=[],
    max_round=8,
    send_introductions=True,
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list": [
        {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

initialMessage = get_initial_post.get_post()

new_post_chat = content_creator.initiate_chat(
    group_chat_manager,
    message=initialMessage,
    summary_method="reflection_with_llm",
)
