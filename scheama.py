from pydantic import BaseModel
from typing import Literal
class Conv_Str(BaseModel):
    """checking conversation is normal or emergency"""

    conversation : Literal["emergency","normal"]

class Context_schema(BaseModel):
    "checking context_schema"

    context : Literal["missing","complete"]

class Emergency_schema(BaseModel):
    """checking emergency """
    emergency : Literal["yes","no"]