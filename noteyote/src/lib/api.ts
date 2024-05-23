import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://localhost:8000', // FastAPI backend URL
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default {
    getItems() {
        return apiClient.get('/items');
    },
    getItem({itemId}: { itemId: any }) {
        return apiClient.get(`/items/${itemId}`);
    },
    createItem({data}: { data: any }) {
        return apiClient.post('/items', data);
    },
    startNotebook() {
        return apiClient.post('/notebooks/start');
    },
    stopNotebook() {
        return apiClient.post('/notebooks/stop');
    }
    // Add other API methods as needed
};
