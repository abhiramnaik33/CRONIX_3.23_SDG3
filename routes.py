from graph.state import State
from typing import Literal

def conversation_route(state : State)->Literal["normal_conversation" , "emergency_conversation"]:
    if state["conversation"] == "emergency" :
        return "normal_conversation"

    else:
        return "emergency_conversation"

def context_route(state: State) -> Literal["full_context_not_given", "full_context_given"]:
    if state["context"] == "missing":
        return "full_context_not_given"
    return "full_context_given"

def emergency_route():
    pass