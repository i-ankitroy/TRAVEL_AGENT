import random
from app.models import FlightOption, HotelOption

def get_flight_options(origin: str, dest: str) -> list[FlightOption]:
    airlines = ["SkyHigh Air", "BudgetWings", "ComfortJet", "GlobalFly"]
    options = []
    
    # Generate 4 random options
    for i in range(4):
        base_price = random.randint(150, 800)
        stops = 0 if base_price > 500 else random.randint(0, 2)
        duration = random.randint(2, 15) + (stops * 2)
        
        options.append(FlightOption(
            id=f"fl_{i}",
            airline=random.choice(airlines),
            price=base_price,
            duration_hours=duration,
            departure_time=f"{random.randint(6, 22)}:00",
            stops=stops
        ))
    return options

def get_hotel_options(dest: str) -> list[HotelOption]:
    names = ["Grand Plaza", "Cozy Stay", "Budget Inn", "Luxury Suites"]
    options = []
    
    for i in range(4):
        options.append(HotelOption(
            id=f"ht_{i}",
            name=f"{random.choice(names)} {dest}",
            price_per_night=random.randint(50, 400),
            rating=round(random.uniform(2.5, 5.0), 1),
            location="City Center" if random.random() > 0.5 else "Airport Area"
        ))
    return options