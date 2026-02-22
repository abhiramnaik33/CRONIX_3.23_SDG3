from pydantic import BaseModel
from typing import Literal,Optional,TypedDict,Annotated,List
from langgraph.graph import add_messages

class State(TypedDict):
    # Conversation
    messages: Annotated[list, add_messages]
    text : str
    voice : str
    images : str
    output : str
    conversation : str
    context : str
    emergency :  str
    name : str

class Input_schema(BaseModel):
    text : str
    voice : str
    images : str

class Output_schema(TypedDict):
    output : str

class Context_schema(TypedDict):
    name : str