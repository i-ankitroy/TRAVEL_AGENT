import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const planTrip = async (req) => {
  const response = await axios.post(`${API_URL}/agent/plan-trip`, req);
  return response.data;
};