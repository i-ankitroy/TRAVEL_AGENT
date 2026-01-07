import json
import re
from app.models import TripRequest, ItineraryResponse
from app.services import mock_providers, ranking
from app.llm import gemini_client, prompts

async def plan_trip(request: TripRequest) -> ItineraryResponse:
    # 1. Get Options
    flights = mock_providers.get_flight_options(request.origin, request.destination)
    hotels = []
    if request.need_hotel:
        hotels = mock_providers.get_hotel_options(request.destination)

    # 2. Heuristic Sorting
    flights, hotels = ranking.sort_options(flights, hotels, request.budget)

    # 3. Construct Prompt
    context = {
        "request": request.dict(),
        "available_flights": [f.dict() for f in flights],
        "available_hotels": [h.dict() for h in hotels]
    }
    
    user_prompt = f"Please select the best itinerary from this data:\n{json.dumps(context, indent=2)}"

    # 4. Call LLM
    llm_response_str = await gemini_client.call_llm(prompts.SYSTEM_PROMPT, user_prompt)
    
    # DEBUG: Print response to terminal to see what Gemini sent
    print(f"\n--- DEBUG LLM RESPONSE ---\n{llm_response_str}\n--------------------------\n")

    # 5. Parse LLM Selection
    try:
        # Clean up Markdown code blocks if present
        clean_str = llm_response_str.strip()
        # Remove ```json and ``` wrapper if they exist
        match = re.search(r"```json\s*(.*?)\s*```", clean_str, re.DOTALL)
        if match:
            clean_str = match.group(1)
        elif clean_str.startswith("```"):
             clean_str = clean_str.strip("`")

        selection = json.loads(clean_str)
        
        # Find the actual objects based on IDs selected by LLM
        # Default to first option if ID not found (fallback)
        selected_flight = next((f for f in flights if f.id == selection.get("selected_flight_id")), flights[0])
        
        selected_hotel = None
        hotel_cost = 0
        
        if request.need_hotel:
            # Try to find selected hotel, default to first if missing
            hid = selection.get("selected_hotel_id")
            if hid:
                selected_hotel = next((h for h in hotels if h.id == hid), hotels[0])
            else:
                selected_hotel = hotels[0] if hotels else None
                
            if selected_hotel:
                hotel_cost = selected_hotel.price_per_night

        total_price = selected_flight.price + hotel_cost

        return ItineraryResponse(
            selected_flight=selected_flight,
            selected_hotel=selected_hotel,
            total_price=total_price,
            explanation=selection.get("explanation", "Choice based on price and duration.")
        )

    except Exception as e:
        print(f"Error parsing LLM response: {e}")
        # Fallback if LLM fails: return the cheapest options (first in sorted list)
        fallback_flight = flights[0]
        fallback_hotel = hotels[0] if hotels else None
        return ItineraryResponse(
            selected_flight=fallback_flight,
            selected_hotel=fallback_hotel,
            total_price=fallback_flight.price + (fallback_hotel.price_per_night if fallback_hotel else 0),
            explanation="AI selection failed, showing most affordable options."
        )