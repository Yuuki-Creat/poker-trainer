from typing import Optional
from pydantic import BaseModel

class ActionRequest(BaseModel):
    scenario_id: int
    user_action: str
    strategy_type: str
    gist_id: Optional[str] = None

class EvaluationResponse(BaseModel):
    status: str
    score: int
    feedback: str
    next_scenario_id: Optional[int]