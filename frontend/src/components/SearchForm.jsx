import { useState } from 'react';

export const SearchForm = ({ onSearch, isLoading }) => {
  const [formData, setFormData] = useState({
    origin: '',
    destination: '',
    departure_date: '',
    budget: 1000,
    need_hotel: true,
    preferences: {
      avoid_layovers: false,
      prefer_morning: false,
      hotel_rating_min: 3,
    },
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="card">
      <h2>Plan Your Trip</h2>
      
      <div className="input-group">
        <label>Origin</label>
        <input 
          type="text" 
          value={formData.origin}
          onChange={e => setFormData({...formData, origin: e.target.value})}
          required 
          placeholder="e.g. New York"
        />
      </div>

      <div className="input-group">
        <label>Destination</label>
        <input 
          type="text" 
          value={formData.destination}
          onChange={e => setFormData({...formData, destination: e.target.value})}
          required 
          placeholder="e.g. London"
        />
      </div>

      <div className="row">
        <div className="input-group">
          <label>Budget ($)</label>
          <input 
            type="number" 
            value={formData.budget}
            onChange={e => setFormData({...formData, budget: Number(e.target.value)})}
          />
        </div>
        <div className="input-group checkbox">
          <label>
            <input 
              type="checkbox" 
              checked={formData.need_hotel}
              onChange={e => setFormData({...formData, need_hotel: e.target.checked})}
            />
            Need Hotel?
          </label>
        </div>
      </div>

      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Planning...' : 'Ask AI Agent'}
      </button>
    </form>
  );
};