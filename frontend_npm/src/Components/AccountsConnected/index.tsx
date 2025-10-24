import React, { useState, useEffect } from "react";
import styles from "./AccountsConnected.module.scss";

interface Account {
  account_id: string;
  name: string;
  bank_name: string;
  account_type: string;
  subtype: string;
  balance: number;
  currency: string;
  mask: string;
}

const AccountsConnected = () => {
  const [accounts, setAccounts] = useState<Account[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  const fetchAccounts = async (isRefresh = false) => {
    if (isRefresh) {
      setRefreshing(true);
    } else {
      setLoading(true);
    }
    
    try {
      // Add a small delay to ensure token has been saved
      if (!isRefresh) {
        await new Promise(resolve => setTimeout(resolve, 1000));
      }
      
      const response = await fetch("/api/get_all_connected_accounts");
      if (!response.ok) {
        throw new Error("Failed to fetch accounts");
      }
      const data = await response.json();
      
      if (data.error) {
        setError(data.error);
      } else {
        setAccounts(data.accounts || []);
        setError(null);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    fetchAccounts();
  }, []);

  const formatCurrency = (amount: number, currency: string) => {
    if (amount == null) return "N/A";
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency || 'USD'
    }).format(amount);
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading accounts...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={styles.container}>
        <div className={styles.error}>Error: {error}</div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div>
          <h1 className={styles.title}>Accounts</h1>
          <p className={styles.subtitle}>Connect your bank accounts</p>
        </div>
        <button 
          className={styles.refreshButton} 
          onClick={() => fetchAccounts(true)}
          disabled={refreshing}
        >
          {refreshing ? "Refreshing..." : "Refresh"}
        </button>
      </div>
      
      {accounts.length === 0 ? (
        <div className={styles.noAccounts}>No accounts connected</div>
      ) : (
        <div className={styles.accountsList}>
          {accounts.map((account, index) => (
            <div key={account.account_id} className={styles.accountCard}>
              <div className={styles.accountIcon}>
                <div className={styles.bankIcon}>🏦</div>
              </div>
              <div className={styles.accountInfo}>
                <h3 className={styles.accountName}>{account.name}</h3>
                <p className={styles.bankName}>{account.bank_name}</p>
              </div>
              <div className={styles.accountBalance}>
                <div className={styles.balance}>
                  {formatCurrency(account.balance, account.currency)}
                </div>
                <div className={styles.accountType}>
                  {account.subtype}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

AccountsConnected.displayName = "AccountsConnected";

export default AccountsConnected;