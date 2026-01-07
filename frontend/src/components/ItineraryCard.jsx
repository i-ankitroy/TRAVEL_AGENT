export const ItineraryCard = ({ data }) => {
  return (
    <div className="card result">
      <h2>Recommended Itinerary</h2>
      <p className="explanation">🤖 {data.explanation}</p>
      
      <div className="section">
        <h3>✈️ Flight: {data.selected_flight.airline}</h3>
        <p>Time: {data.selected_flight.departure_time} | Duration: {data.selected_flight.duration_hours}h</p>
        <p>Stops: {data.selected_flight.stops} | Price: ${data.selected_flight.price}</p>
      </div>

      {data.selected_hotel && (
        <div className="section">
          <h3>🏨 Hotel: {data.selected_hotel.name}</h3>
          <p>Rating: {data.selected_hotel.rating}⭐ | Location: {data.selected_hotel.location}</p>
          <p>Price: ${data.selected_hotel.price_per_night}/night</p>
        </div>
      )}

      <div className="total">
        <h3>Total Estimate: ${data.total_price}</h3>
      </div>
    </div>
  );
};