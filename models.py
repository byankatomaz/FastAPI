from typing import Optional
from pydantic import BaseModel
  
class Options(BaseModel):
    answer_a: str
    answer_b: str
    answer_c: str
    
class Question(BaseModel):
    id: Optional[int] = None
    question: str
    options: Options
    answer: str