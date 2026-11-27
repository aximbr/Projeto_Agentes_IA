### Notas de aula ###
# agent_loop.py
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Replace the block below with the multi-turn loop
questions = [
    "What is an agent?",
    "How is that different from a chatbot?",
    "Give me one example."
]

for question in questions:
    messages.append({"role": "user", "content": question})
    while True:
        response = client.chat.completions.create(
            model="gpt-5.6-luna",
            messages=messages,
        )
        finish_reason = response.choices[0].finish_reason
        if finish_reason == "stop":
            reply = response.choices[0].message.content
            print(f"Q: {question}")
            print(f"A: {reply}")
            print()
            messages.append({"role": "assistant", "content": reply})
            break
        else:
            break
#####FIM LAB2######
 agent_components.py
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

model = "gpt-5.6-luna"

messages = [
    {
        "role": "system",
        "content": "You are a helpful personal assistant. Use your tools when you need real data."
    }
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "check_calendar",
            "description": "Check the user's calendar for events on a given date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date to check, e.g. 2026-03-14"
                    }
                },
                "required": ["date"]
            }
        }
    }
]

def check_calendar(date):
    return "10am: Team standup, 2pm: Dentist appointment"

messages.append({"role": "user", "content": "Today is 11/25/2026. What's on my calendar today?"})

while True:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools
    )
    finish_reason = response.choices[0].finish_reason
    assistant_message = response.choices[0].message
    messages.append(assistant_message)

    if finish_reason == "tool_calls":
        for tool_call in assistant_message.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            if name == "check_calendar":
                result = check_calendar(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })
    elif finish_reason == "stop":
        print(assistant_message.content)
        break

##### LAB3 ########
# tools.py
tools = [
    {
        "type": "function",
        "function": {
            "name": "check_calendar",
            "description": "Returns today's calendar events.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    }
]

def check_calendar():
    return "10am: Team standup, 2pm: Dentist appointment"

def execute_tool(name, args):
    if name == "check_calendar":
        return check_calendar()
    return f"Unknown tool: {name}"

#####################
### agent_memory.py
#####################
import os, json
from openai import OpenAI
from tools import tools, execute_tool

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

SYSTEM_PROMPT = "You are a helpful personal assistant. Use your tools when you need real data."

def run_agent(messages):
    while True:
        response = client.chat.completions.create(
            model="gpt-5.6-luna",
            messages=messages,
            tools=tools,
        )
        choice = response.choices[0]
        messages.append(choice.message)
        if choice.finish_reason == "tool_calls":
            for tc in choice.message.tool_calls:
                args = json.loads(tc.function.arguments) if tc.function.arguments else {}
                result = execute_tool(tc.function.name, args)
                messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
        else:
            return choice.message.content

def trim_history(messages, max_messages=6):
    if len(messages) > max_messages:
        return [messages[0]] + messages[-(max_messages - 1):]
    return messages

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

questions = [
    "What's on my calendar today?",
    "Tell me about the standup.",
    "What time is my dentist?",
    "Am I free at 3pm?",
    "Summarise my day.",
]

for q in questions:
    messages.append({"role": "user", "content": q})
    answer = run_agent(messages)
    messages = trim_history(messages, max_messages=6)
    print(f"Q: {q}")
    print(f"A: {answer}")
    print(f"Messages in history: {len(messages)}")
    print()

######################
"""
The Truncation Strategy
When history gets too long, the simplest fix is to drop the oldest non-system messages and keep only the most recent ones.

The rule is straightforward:

Always keep the message at index 0 - that is the system message. It is the agent's identity and instructions. Removing it breaks the agent.
After that, keep only the last N-1 messages, where N is your maximum allowed history length.
This is called a sliding window. The window moves forward through the conversation, always keeping the system prompt plus the most recent context.
"""
######################
def trim_history(messages, max_messages=6):
    if len(messages) > max_messages:
        return [messages[0]] + messages[-(max_messages - 1):]
    return messages
 #####################
 

######################
# Create react_agent.py
######################
import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

def check_calendar(day):
    events = {
        "monday": "Team standup at 9am",
        "tuesday": "Dentist at 2pm",
        "wednesday": "No events",
        "thursday": "1pm lunch with Alex, 3pm product review",
        "friday": "Weekly retro at 4pm"
    }
    return events.get(day.lower(), "No events found for that day.")

def search_contacts(name):
    contacts = {
        "sarah": "sarah@email.com",
        "alex": "alex@email.com",
        "jordan": "jordan@email.com"
    }
    return contacts.get(name.lower(), "Contact not found.")

tools = [
    {
        "type": "function",
        "function": {
            "name": "check_calendar",
            "description": "Check the calendar for a given day.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {"type": "string", "description": "Day of the week"}
                },
                "required": ["day"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_contacts",
            "description": "Look up a contact's email address by name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "The contact's name"}
                },
                "required": ["name"]
            }
        }
    }
]


user_message = "What's on my calendar today? Also find Sarah's email and send me a summary."

def run_agent(system_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    while True:
        response = client.chat.completions.create(
            model="gpt-5.6-luna",
            messages=messages,
            tools=tools
        )
        msg = response.choices[0].message
        messages.append(msg)
        if msg.content:
            print(msg.content)
        if msg.tool_calls:
            for tc in msg.tool_calls:
                args = json.loads(tc.function.arguments)
                if tc.function.name == "check_calendar":
                    result = check_calendar(**args)
                elif tc.function.name == "search_contacts":
                    result = search_contacts(**args)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result
                })
        else:
            break

print("--- No ReAct ---")
run_agent("You are a helpful personal assistant.")

print("\n--- ReAct ---")
run_agent("You are a helpful personal assistant. Before every tool call, write 'Thought: [your reasoning]'. After every tool result, write 'Observation: [what you learned]'. Then decide your next step.")