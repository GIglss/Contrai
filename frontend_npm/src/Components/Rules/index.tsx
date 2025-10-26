import React, { useState, useEffect } from 'react';
import CreateRule from './CreateRule';
import EditRule from './EditRule';
import styles from './Rules.module.scss';

interface Rule {
  id: string;
  name: string;
  description: string;
  fromAccount: string;
  toAccount: string;
  transferType: 'percentage' | 'amount';
  percentage?: number | string;
  amount?: number | string;
  frequency: string;
  isActive: boolean;
  createdAt: string;
  lastExecuted?: string;
}

interface Account {
  account_id: string;
  name: string;
  custom_name?: string;
  type: string;
  subtype: string;
}

const Rules: React.FC = () => {
  const [rules, setRules] = useState<Rule[]>([]);
  const [accounts, setAccounts] = useState<Account[]>([]);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [editingRule, setEditingRule] = useState<Rule | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchRules();
    fetchAccounts();
  }, []);

  const fetchRules = async () => {
    try {
      const response = await fetch('/api/rules');
      const data = await response.json();
      console.log(data);
      if (data.error) {
        throw new Error(data.error);
      }
      
      setRules(data.rules || []);
    } catch (err) {
      console.error('Error fetching rules:', err);
      setError('Failed to load rules');
    } finally {
      setIsLoading(false);
    }
  };

  const fetchAccounts = async () => {
    try {
      const response = await fetch('/api/get_all_connected_accounts');
      const data = await response.json();
      
      if (data.error) {
        throw new Error(data.error);
      }
      
      setAccounts(data.accounts || []);
    } catch (err) {
      console.error('Error fetching accounts:', err);
    }
  };

  const getAccountName = (accountId: string) => {
    const account = accounts.find(acc => acc.account_id === accountId);
    if (!account) return accountId;
    
    const displayName = account.custom_name || account.name;
    return `${displayName}`;
  };

  const formatAmount = (rule: Rule) => {
    if (rule.transferType === 'percentage') {
      const percentage = typeof rule.percentage === 'string' ? Number.parseFloat(rule.percentage) : rule.percentage;
      return `${percentage || 0}%`;
    } else {
      const amount = typeof rule.amount === 'string' ? Number.parseFloat(rule.amount) : rule.amount;
      return `$${(amount || 0).toFixed(2)}`;
    }
  };

  const formatFrequency = (frequency: string) => {
    return frequency.charAt(0).toUpperCase() + frequency.slice(1);
  };

  const handleRuleCreated = () => {
    setShowCreateForm(false);
    fetchRules(); // Refresh the rules list
  };

  const handleRuleUpdated = () => {
    setEditingRule(null);
    fetchRules(); // Refresh the rules list
  };

  const handleRuleCardClick = (rule: Rule, event: React.MouseEvent) => {
    // Don't open edit if clicking on the status button
    if ((event.target as HTMLElement).closest('button')) {
      return;
    }
    setEditingRule(rule);
  };

  const toggleRuleStatus = async (ruleId: string, currentStatus: boolean) => {
    try {
      const response = await fetch(`/api/rules/${ruleId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          isActive: !currentStatus
        }),
      });

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error);
      }

      // Update the local state
      setRules(prevRules => 
        prevRules.map(rule => 
          rule.id === ruleId 
            ? { ...rule, isActive: !currentStatus }
            : rule
        )
      );
    } catch (err) {
      console.error('Error toggling rule status:', err);
      setError(err instanceof Error ? err.message : 'Failed to update rule status');
    }
  };

  if (showCreateForm) {
    return (
      <CreateRule 
        onCancel={() => setShowCreateForm(false)}
        onSuccess={handleRuleCreated}
      />
    );
  }

  if (editingRule) {
    return (
      <EditRule 
        rule={editingRule} 
        onBack={() => setEditingRule(null)} 
        onSuccess={handleRuleUpdated} 
      />
    );
  }

  return (
    <div className={styles.rules}>
      <div className={styles.header}>
        <h2>Flow Rules</h2>
        <p>Manage your automatic transfer rules</p>
        <button 
          className={styles.createBtn}
          onClick={() => setShowCreateForm(true)}
        >
          + Create New Rule
        </button>
      </div>

      {error && (
        <div className={styles.error}>
          {error}
        </div>
      )}

      {isLoading ? (
        <div className={styles.loading}>Loading rules...</div>
      ) : rules.length === 0 ? (
        <div className={styles.empty}>
          <div className={styles.emptyIcon}>📋</div>
          <h3>No rules created yet</h3>
          <p>Create your first automatic transfer rule to get started</p>
          <button 
            className={styles.createBtn}
            onClick={() => setShowCreateForm(true)}
          >
            Create First Rule
          </button>
        </div>
      ) : (
        <div className={styles.rulesList}>
          {rules.map(rule => (
            <div 
              key={rule.id} 
              className={`${styles.ruleCard} ${!rule.isActive ? styles.inactive : ''}`}
              onClick={(e) => handleRuleCardClick(rule, e)}
            >
              <div className={styles.ruleHeader}>
                <h3>{rule.name}</h3>
                <button
                  className={`${styles.status} ${rule.isActive ? styles.active : styles.inactive}`}
                  onClick={() => toggleRuleStatus(rule.id, rule.isActive)}
                  title={`Click to ${rule.isActive ? 'deactivate' : 'activate'} this rule`}
                >
                  {rule.isActive ? 'Active' : 'Inactive'}
                </button>
              </div>
              
              {rule.description && (
                <p className={styles.description}>{rule.description}</p>
              )}
              
              <div className={styles.ruleDetails}>
                <div className={styles.transfer}>
                  <div className={styles.fromTo}>
                    <span className={styles.from}>From: {getAccountName(rule.fromAccount)}</span>
                    <span className={styles.arrow}>→</span>
                    <span className={styles.to}>To: {getAccountName(rule.toAccount)}</span>
                  </div>
                </div>
                
                <div className={styles.amountFreq}>
                  <span className={styles.amount}>{formatAmount(rule)}</span>
                  <span className={styles.frequency}>{formatFrequency(rule.frequency)}</span>
                </div>
              </div>
              
              <div className={styles.ruleFooter}>
                <span className={styles.created}>
                  Created: {new Date(rule.createdAt).toLocaleDateString()}
                </span>
                {rule.lastExecuted && (
                  <span className={styles.lastExecuted}>
                    Last run: {new Date(rule.lastExecuted).toLocaleDateString()}
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

Rules.displayName = "Rules";

export default Rules;