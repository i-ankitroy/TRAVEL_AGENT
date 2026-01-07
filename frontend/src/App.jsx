import { useState } from 'react';
import { SearchForm } from './components/SearchForm';
import { ItineraryCard } from './components/ItineraryCard';
import { planTrip } from './api/agentClient';
import './App.css';

function App() {
  const [itinerary, setItinerary] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (req) => {
    setLoading(true);
    setError('');
    setItinerary(null);
    try {
      const result = await planTrip(req);
      setItinerary(result);
    } catch (err) {
      setError('Failed to plan trip. Ensure backend is running.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>✈️ AI Travel Agent</h1>
        <p>Your smart companion for perfect trips.</p>
      </header>
      <div className="content">
        <SearchForm onSearch={handleSearch} isLoading={loading} />
        {error && <p className="error">{error}</p>}
        {itinerary && <ItineraryCard data={itinerary} />}
      </div>
    </div>
  );
}

export default App;