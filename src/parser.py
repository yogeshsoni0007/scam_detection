from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel, Field

class ScamIntentResponse(BaseModel):
    category: Literal["Scam", "Not a Scam", "Uncertain"]
    risk_score:int=Field(ge=0, le=5)
    reasoning:str
    intent_type:Literal["Financial", "Phishing", "Social Engineering", "Other"]

parser = PydanticOutputParser(pydantic_object=ScamIntentResponse)