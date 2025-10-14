// React Native compatible data utilities
// Note: Some types from 'plaid/dist/api' may need to be replaced with React Native compatible types

const formatCurrency = (
  number: number | null | undefined,
  code: string | null | undefined
) => {
  if (number != null && number !== undefined) {
    return ` ${parseFloat(number.toFixed(2)).toLocaleString("en")} ${code}`;
  }
  return "no data";
};

export interface Categories {
  title: string;
  field: string;
}

// Interfaces for categories in each individual product
interface AuthDataItem {
  routing: string;
  account: string;
  balance: string;
  name: string;
}

interface TransactionsDataItem {
  amount: string;
  date: string;
  name: string;
}

interface IdentityDataItem {
  addresses: string;
  phoneNumbers: string;
  emails: string;
  names: string;
}

interface BalanceDataItem {
  balance: string;
  subtype: string | null;
  mask: string;
  name: string;
}

interface InvestmentsDataItem {
  mask: string;
  quantity: string;
  price: string;
  value: string;
  name: string;
}

interface InvestmentsTransactionItem {
  amount: number;
  date: string;
  name: string;
}

interface LiabilitiesDataItem {
  amount: string;
  date: string;
  name: string;
  type: string;
}

interface PaymentDataItem {
  paymentId: string;
  amount: string;
  status: string;
  statusUpdate: string;
  recipientId: string;
}

interface ItemDataItem {
  billed: string;
  available: string;
  name: string;
}

interface AssetsDataItem {
  account: string;
  balance: string;
  daysAvailable: string;
  transactions: string;
}

// API utility functions for React Native
export const apiRequest = async (endpoint: string, options: RequestInit = {}) => {
  try {
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API request failed:', error);
    throw error;
  }
};

// Export utility functions
export {
  formatCurrency,
  type AuthDataItem,
  type TransactionsDataItem,
  type IdentityDataItem,
  type BalanceDataItem,
  type InvestmentsDataItem,
  type InvestmentsTransactionItem,
  type LiabilitiesDataItem,
  type PaymentDataItem,
  type ItemDataItem,
  type AssetsDataItem,
};