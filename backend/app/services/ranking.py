from app.models import FlightOption, HotelOption

def score_flight(flight: FlightOption, budget: int) -> float:
    # Lower score is better
    score = flight.price
    score += flight.duration_hours * 20 # Value 1 hour as $20
    score += flight.stops * 50 # Penalty for stops
    return score

def sort_options(flights, hotels, budget):
    # Sort by a basic heuristic so the LLM sees the "best" math options first
    sorted_flights = sorted(flights, key=lambda x: score_flight(x, budget))
    sorted_hotels = sorted(hotels, key=lambda x: x.price_per_night) if hotels else []
    return sorted_flights, sorted_hotels