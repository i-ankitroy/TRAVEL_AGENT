from pydantic import BaseModel
from typing import List, Optional

class UserPreferences(BaseModel):
    avoid_layovers: bool = False
    prefer_morning: bool = False
    hotel_rating_min: int = 3

class TripRequest(BaseModel):
    origin: str
    destination: str
    departure_date: str
    return_date: Optional[str] = None
    budget: int
    need_hotel: bool
    preferences: UserPreferences

class FlightOption(BaseModel):
    id: str
    airline: str
    price: float
    duration_hours: float
    departure_time: str
    stops: int

class HotelOption(BaseModel):
    id: str
    name: str
    price_per_night: float
    rating: float
    location: str

class ItineraryResponse(BaseModel):
    selected_flight: FlightOption
    selected_hotel: Optional[HotelOption] = None
    total_price: float
    explanation: str