import axios from 'axios';

const API = axios.create({ baseURL: 'http://127.0.0.1:5000' });

export const startSimulation = (type) => API.post('/simulate', { type });
export const fetchLogs = () => API.get('/logs');
export const saveConfig = (config) => API.post('/save-config', config);
