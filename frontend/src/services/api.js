import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api'; // Adjust the base URL as needed

export const fetchDevices = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/devices`);
        return response.data;
    } catch (error) {
        console.error('Error fetching devices:', error);
        throw error;
    }
};

export const addDevice = async (deviceData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/devices`, deviceData);
        return response.data;
    } catch (error) {
        console.error('Error adding device:', error);
        throw error;
    }
};

export const scanNetwork = async () => {
    try {
        const response = await axios.post(`${API_BASE_URL}/scan`);
        return response.data;
    } catch (error) {
        console.error('Error scanning network:', error);
        throw error;
    }
};