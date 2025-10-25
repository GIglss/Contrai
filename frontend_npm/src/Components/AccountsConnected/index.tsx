import React, { useState, useEffect } from "react";
import styles from "./AccountsConnected.module.scss";

interface Account {
  account_id: string;
  name: string;
  custom_name?: string;
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
  const [editingAccount, setEditingAccount] = useState<string | null>(null);
  const [customName, setCustomName] = useState("");

  const fetchAccounts = async (isRefresh = false, retryCount = 0) => {
    const maxRetries = 3;
    const retryDelay = 1500; // 1.5 seconds between retries

    if (isRefresh) {
      setRefreshing(true);
    } else if (retryCount === 0) {
      setLoading(true);
    }
    
    try {
      // Add a small delay to ensure token has been saved
      if (!isRefresh && retryCount === 0) {
        await new Promise(resolve => setTimeout(resolve, 1000));
      }
      
      const response = await fetch("/api/get_all_connected_accounts");
      if (!response.ok) {
        throw new Error("Failed to fetch accounts");
      }
      const data = await response.json();
      
      if (data.error) {
        setError(data.error);
        setLoading(false);
        setRefreshing(false);
      } else {
        const fetchedAccounts = data.accounts || [];
        
        // If no accounts found and this is the initial load (not a refresh), retry
        if (fetchedAccounts.length === 0 && !isRefresh && retryCount < maxRetries) {
          console.log(`No accounts found, retrying... (attempt ${retryCount + 1}/${maxRetries})`);
          setTimeout(() => {
            fetchAccounts(false, retryCount + 1);
          }, retryDelay);
          return; // Don't set loading to false yet
        }
        
        setAccounts(fetchedAccounts);
        setError(null);
        setLoading(false);
        setRefreshing(false);
      }
    } catch (err) {
      // If error occurred and we haven't exhausted retries, try again
      if (!isRefresh && retryCount < maxRetries) {
        console.log(`Error fetching accounts, retrying... (attempt ${retryCount + 1}/${maxRetries})`);
        setTimeout(() => {
          fetchAccounts(false, retryCount + 1);
        }, retryDelay);
        return; // Don't set loading to false yet
      }
      
      setError(err instanceof Error ? err.message : "An error occurred");
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

  const startEditing = (accountId: string, currentCustomName?: string) => {
    setEditingAccount(accountId);
    setCustomName(currentCustomName || "");
  };

  const cancelEditing = () => {
    setEditingAccount(null);
    setCustomName("");
  };

  const saveCustomName = async (accountId: string) => {
    try {
      const response = await fetch(`/api/accounts/${accountId}/custom_name`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ custom_name: customName }),
      });

      if (!response.ok) {
        throw new Error('Failed to update custom name');
      }

      // Update local state
      setAccounts(prevAccounts =>
        prevAccounts.map(account =>
          account.account_id === accountId
            ? { ...account, custom_name: customName || undefined }
            : account
        )
      );

      setEditingAccount(null);
      setCustomName("");
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update account name');
    }
  };

  const getDisplayName = (account: Account) => {
    return account.custom_name || account.name;
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
                {editingAccount === account.account_id ? (
                  <div className={styles.editingContainer}>
                    <input
                      type="text"
                      value={customName}
                      onChange={(e) => setCustomName(e.target.value)}
                      placeholder={account.name}
                      className={styles.customNameInput}
                      maxLength={50}
                      autoFocus
                    />
                    <div className={styles.editActions}>
                      <button
                        onClick={() => saveCustomName(account.account_id)}
                        className={styles.saveBtn}
                      >
                        ✓
                      </button>
                      <button
                        onClick={cancelEditing}
                        className={styles.cancelBtn}
                      >
                        ✕
                      </button>
                    </div>
                  </div>
                ) : (
                  <div className={styles.nameContainer}>
                    <h3 className={styles.accountName}>
                      {getDisplayName(account)}
                      {account.custom_name && (
                        <span className={styles.originalName}>({account.name})</span>
                      )}
                    </h3>
                    <button
                      onClick={() => startEditing(account.account_id, account.custom_name)}
                      className={styles.editBtn}
                      title="Edit account name"
                    >
                      ✏️
                    </button>
                  </div>
                )}
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