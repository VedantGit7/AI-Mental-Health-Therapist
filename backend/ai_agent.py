# from langchain_core.tools import tool
# from tools import query_medgemma, call_emergency

# @tool
# def ask_mental_health_specialist(query: str) -> str:
#     """
#     Generate a therapeutic response using the MedGemma model.
#     Use this for all general user queries, mental health questions, emotional concerns,
#     or to offer empathetic, evidence-based guidance in a conversational tone.
#     """
#     return query_medgemma(query)


# @tool
# def emergency_call_tool(phone: str) -> str:
#     """
#     Place an emergency call to the safety helpline's phone number via Twilio.
#     Use this only if the user expresses suicidal ideation, intent to self-harm,
#     or describes a mental health emergency requiring immediate help.
#     """
#     call_emergency(phone)


# @tool
# def find_nearby_therapists_by_location(location: str) -> str:
#     """
#     Finds and returns a list of licensed therapists near the specified location.

#     Args:
#         location (str): The name of the city or area in which the user is seeking therapy support.

#     Returns:
#         str: A newline-separated string containing therapist names and contact info.
#     """
#     return (
#         f"Here are some therapists near {location}, {location}:\n"
#         "- Dr. Ayesha Kapoor - +1 (555) 123-4567\n"
#         "- Dr. James Patel - +1 (555) 987-6543\n"
#         "- MindCare Counseling Center - +1 (555) 222-3333"
#     )


# # Step1: Create an AI Agent & Link to backend
# from langchain_openai import ChatOpenAI
# from langchain.agents import create_agent
# from langgraph.prebuilt import create_react_agent
# from openai import OpenAI
# from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, NVIDIA_MODEL


# tools = [ask_mental_health_specialist, emergency_call_tool, find_nearby_therapists_by_location]
# llm = ChatOpenAI(
#     api_key=NVIDIA_API_KEY,
#     base_url=NVIDIA_BASE_URL,
#     model=NVIDIA_MODEL,
#     temperature=0.2,
#     max_tokens=4096,
#     streaming=True  # Enable streaming support
# )
# graph = create_agent(llm, tools=tools)

# SYSTEM_PROMPT = """
# You are an AI engine supporting mental health conversations with warmth and vigilance.
# You have access to three tools:

# 1. `ask_mental_health_specialist`: Use this tool to answer all emotional or psychological queries with therapeutic guidance.
# 2. `locate_therapist_tool`: Use this tool if the user asks about nearby therapists or if recommending local professional help would be beneficial.
# 3. `emergency_call_tool`: Use this immediately if the user expresses suicidal thoughts, self-harm intentions, or is in crisis.

# Always take necessary action. Respond kindly, clearly, and supportively.
# """

# def parse_response(stream):
#     tool_called_name = "None"
#     final_response = None

#     for s in stream:
#         # Check if a tool was called
#         tool_data = s.get('tools')
#         if tool_data:
#             tool_messages = tool_data.get('messages')
#             if tool_messages and isinstance(tool_messages, list):
#                 for msg in tool_messages:
#                     tool_called_name = getattr(msg, 'name', 'None')

#         # Check if agent returned a message
#         agent_data = s.get('agent')
#         if agent_data:
#             messages = agent_data.get('messages')
#             if messages and isinstance(messages, list):
#                 for msg in messages:
#                     if msg.content:
#                         final_response = msg.content

#     return tool_called_name, final_response


# """if __name__ == "__main__":
#     while True:
#         user_input = input("User: ")
#         print(f"Received user input: {user_input[:200]}...")
#         inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_input)]}
#         stream = graph.stream(inputs, stream_mode="updates")
#         tool_called_name, final_response = parse_response(stream)
#         print("TOOL CALLED: ", tool_called_name)
#         print("ANSWER: ", final_response)"""
        
from langchain_core.tools import tool
from tools import query_medgemma, call_emergency


@tool
def ask_mental_health_specialist(query: str) -> str:
    """
    Generate a therapeutic response using the MedGemma model.
    Use this for all general user queries, mental health questions, emotional concerns,
    or to offer empathetic, evidence-based guidance in a conversational tone.
    """
    return query_medgemma(query)


@tool
def emergency_call_tool() -> str:
    """
    Place an emergency call to the safety helpline's phone number via Twilio.
    Use this only if the user expresses suicidal ideation, intent to self-harm,
    or describes a mental health emergency requiring immediate help.
    
    This tool automatically calls the configured EMERGENCY_CONTACT number and provides
    UAE-specific crisis helpline information.
    """
    from config import EMERGENCY_CONTACT
    call_result = call_emergency(EMERGENCY_CONTACT)
    
    # Add UAE crisis helpline information
    uae_helplines = """

🇦🇪 UAE Crisis & Mental Health Support:
• National Mental Support Line: 800 4673 (HOPE) - 24/7 via call/WhatsApp
• Dubai Mental Health Helpline: 800 111 - 24/7 psychological support
• Abu Dhabi Estijaba: 800 1717 - Bilingual support (Arabic/English)
• Emergency: 999 (Police) / 998 (Ambulance)
"""
    
    return call_result + uae_helplines


@tool
def find_nearby_therapists_by_location(location: str) -> str:
    """
    Finds and returns a list of licensed therapists near the specified location.

    Args:
        location (str): The name of the city or area in which the user is seeking therapy support.

    Returns:
        str: A newline-separated string containing therapist names and contact info.
    """
    return (
        f"Here are some therapists near {location}:\n"
        "- Dr. Ayesha Kapoor - +1 (555) 123-4567\n"
        "- Dr. James Patel - +1 (555) 987-6543\n"
        "- MindCare Counseling Center - +1 (555) 222-3333"
    )


# Step 1: Create an AI Agent & Link to backend
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, NVIDIA_MODEL


tools = [ask_mental_health_specialist, emergency_call_tool, find_nearby_therapists_by_location]

llm = ChatOpenAI(
    api_key=NVIDIA_API_KEY,
    base_url=NVIDIA_BASE_URL,
    model=NVIDIA_MODEL,
    temperature=0.2,
    max_tokens=4096,
    streaming=True
)

graph = create_react_agent(llm, tools=tools)

SYSTEM_PROMPT = """
You are an AI engine supporting mental health conversations with warmth and vigilance.
You have access to three tools:

1. `ask_mental_health_specialist`: Use this tool to answer all emotional or psychological queries with therapeutic guidance.
2. `find_nearby_therapists_by_location`: Use this tool if the user asks about nearby therapists or if recommending local professional help would be beneficial.
3. `emergency_call_tool`: Use this immediately if the user expresses suicidal thoughts, self-harm intentions, or is in crisis.

When responding to crisis situations, always provide local crisis helpline numbers including:
- India: 9152987821 (Samaritans) or 1098
- United States: 988 (Suicide & Crisis Lifeline)
- United Kingdom: 116 123 (Samaritans)
- Australia: 13 11 14 (Lifeline)
- UAE: 800 4673 (HOPE), Dubai: 800 111, Abu Dhabi: 800 1717

Always take necessary action. Respond kindly, clearly, and supportively.
"""


def parse_response(stream):
    """Parse streaming response from LangGraph agent"""
    tool_called_name = "None"
    final_response = None

    for s in stream:
        # Check if a tool was called
        tool_data = s.get('tools')
        if tool_data:
            tool_messages = tool_data.get('messages')
            if tool_messages and isinstance(tool_messages, list):
                for msg in tool_messages:
                    tool_called_name = getattr(msg, 'name', 'None')

        # Check if agent returned a message
        agent_data = s.get('agent')
        if agent_data:
            messages = agent_data.get('messages')
            if messages and isinstance(messages, list):
                for msg in messages:
                    if msg.content:
                        final_response = msg.content

    return tool_called_name, final_response


"""if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        print(f"Received user input: {user_input[:200]}...")
        
        inputs = {
            "messages": [
                ("system", SYSTEM_PROMPT),
                ("user", user_input)
            ]
        }
        
        stream = graph.stream(inputs, stream_mode="updates")
        tool_called_name, final_response = parse_response(stream)
        
        print("TOOL CALLED: ", tool_called_name)
        print("ANSWER: ", final_response)"""
