from fastapi import APIRouter, HTTPException
from app.models import TripRequest, ItineraryResponse
from app.agent import travel_agent

router = APIRouter()

@router.post("/agent/plan-trip", response_model=ItineraryResponse)
async def plan_trip_endpoint(request: TripRequest):
    try:
        result = await travel_agent.plan_trip(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))