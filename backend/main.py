from typing import List, Optional

from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from models import ActionRequest, EvaluationResponse
from engine import StrategyEngine
from storage import storage
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class ActionRequest(BaseModel):
    scenario_id: int
    user_action: str
    strategy_type: str
    dynamic_hand: Optional[List[str]] = None

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "OK"}

@app.on_event("startup")
async def startup_event():
    await storage.reload_scenarios()

# @app.post("/api/evaluate", response_model=EvaluationResponse)
# async def evaluate(req: ActionRequest):
#     scenario = storage.get_by_id(req.scenario_id)
#     result = StrategyEngine.evaluate(req.user_action, scenario, req.strategy_type)
    
#     return {
#         **result,
#         "next_scenario_id": req.scenario_id + 1 if req.scenario_id < 100 else None
#     }

@app.post("/api/evaluate")
async def evaluate(req: ActionRequest):
    scenario = storage.get_by_id(req.scenario_id)
    
    currentHand = req.dynamic_hand if req.dynamic_hand else scenario.get("hand")
    
    result = StrategyEngine.evaluate(
        req.user_action,
        scenario,
        req.strategy_type,
        currentHand
    )

    return result

@app.get("/api/scenarios")
async def get_scenario():
    return storage.get_all()

@app.post("/api/admin/reload")
async def reload_data(background_tasks: BackgroundTasks):
    background_tasks.add_task(storage.reload_scenarios)
    return {"message": "Reloading in background..."}
