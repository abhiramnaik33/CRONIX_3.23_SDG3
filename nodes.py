from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage,AIMessage
from graph.state import State
from scheama import Conv_Str,Context_schema,Emergency_schema


conversation_template = PromptTemplate.from_template(
    """
You must classify the user question as either "normal" or "emergency".

Respond ONLY in valid JSON that matches this schema:

  "conversation": "normal" | "emergency"


User question: {question}
"""
)

general_conversation_template = PromptTemplate.from_template(
    """
    based on the user question introduce your self ur a helpfull assistent

    user question : {question}
    """
)

dynamic_question_template = PromptTemplate.from_template("""
You are handling a possible emergency.

Ask ONLY ONE clear question to collect missing information.
Required info:
- Name
- Location
- Type of emergency

User message: {question}
""")

context_full_fill_template = PromptTemplate.from_template("""
Check if the following messages contains all the deatils for the this question:

question : {questions}
messages : {messages}")

If missing, return "missing"
Else return "complete"

Respond ONLY in valid JSON that matches this schema:

  "context": "missing"|"complete"

""")

emergency_detection_template = PromptTemplate.from_template("""
based on the conversation check this is the serious emergency need to call the help
or can llm soggestion can manage the situation
                                                            
conversation : {messages}
Respond ONLY in valid JSON that matches this schema:

  "emergency": ""yes"|"no""

""")

def messages_to_text(messages: list) -> str:
    conversation = []

    for msg in messages:
        if isinstance(msg, HumanMessage):
            conversation.append(f"Human: {msg.content}")
        elif isinstance(msg, AIMessage):
            conversation.append(f"AI: {msg.content}")

    return "\n".join(conversation)

def conversation_context_validation(state : State):
    llm = ChatOllama(model="gemini-3-flash-preview:cloud").with_structured_output(Conv_Str)
    text = state["text"]
    prompt = conversation_template.invoke({"question" : text})
    output = llm.invoke(prompt).conversation.lower()
    return {"messages" : HumanMessage(content = text),
            "conversation" : output
           }

def handle_general_conversation(state : State):
    llm = ChatOllama(model="gemini-3-flash-preview:cloud",reasoning=False)
    text = state["text"]
    prompt = general_conversation_template.invoke({"question" : text})
    output = llm.invoke(prompt)
    return {"output" : output
           }

def dyanamic_question(state : State):
    if state["context"] != state["contex"] == "no":
        llm = ChatOllama(model="gemini-3-flash-preview:cloud")  
        text = state["text"]
        prompt = dynamic_question_template.invoke({"question" : text})
        output = llm.invoke(prompt)
        return {"output" : output,
               "messages" : AIMessage(content = output.content)}

def context_full_fill(state:State):
    llm = ChatOllama(
        model="gemini-3-flash-preview:cloud"
    ).with_structured_output(Context_schema)
    history_text = messages_to_text(state["messages"])
    prompt = context_full_fill_template.invoke({"question" : state["text"],"messages" : history_text})
    output = llm.invoke(prompt).context.lower()
    return {"context" : output}

def emeragency_detection(state : State):
    llm = ChatOllama(
        model="gemini-3-flash-preview:cloud"
    ).with_structured_output(Emergency_schema)
    history_text = messages_to_text(state["messages"])
    prompt = context_full_fill_template.invoke({"messages" : history_text})
    output = llm.invoke(prompt).emeragency.lower()
    return {"emergency" : output}

def respond():
    pass

def respond_conversation():
    pass

def helping_process():
    pass


def context_route():
    pass

def emergency_route():
    pass

