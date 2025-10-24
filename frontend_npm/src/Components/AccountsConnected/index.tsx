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

  useEffect(() => {
    const fetchAccounts = async () => {
      try {
        const response = await fetch("/api/get_all_accounts");
        if (!response.ok) {
          throw new Error("Failed to fetch accounts");
        }
        const data = await response.json();
        
        if (data.error) {
          setError(data.error);
        } else {
          setAccounts(data.accounts || []);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

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
      <h1 className={styles.title}>Accounts</h1>
      <p className={styles.subtitle}>Connect your bank accounts</p>
      
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