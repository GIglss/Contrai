// API Configuration for React Native
// Update these URLs to match your backend server
import { Platform } from 'react-native';

export const API_CONFIG = {
  // For iOS Simulator - use localhost
  // For Android Emulator - use 10.0.2.2
  // For physical devices - use your computer's IP address
  BASE_URL: __DEV__ 
    ? (Platform.OS === 'ios' ? 'http://localhost:8000' : 'http://10.0.2.2:8000')
    : 'https://your-production-api.com',
    
  ENDPOINTS: {
    INFO: '/api/info',
    CREATE_LINK_TOKEN: '/api/create_link_token',
    CREATE_LINK_TOKEN_PAYMENT: '/api/create_link_token_for_payment',
    SET_ACCESS_TOKEN: '/api/set_access_token',
    CREATE_USER_TOKEN: '/api/create_user_token',
  }
};

// Helper function to build full API URLs
export const getApiUrl = (endpoint: string): string => {
  return `${API_CONFIG.BASE_URL}${endpoint}`;
};