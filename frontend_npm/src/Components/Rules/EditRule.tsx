import React, { useState, useEffect } from 'react';
import styles from './EditRule.module.scss';

interface Account {
  account_id: string;
  name: string;
  custom_name?: string;
  type: string;
  subtype: string;
}

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

interface EditRuleProps {
  rule: Rule;
  onBack: () => void;
  onSuccess: () => void;
}

const EditRule: React.FC<EditRuleProps> = ({ rule, onBack, onSuccess }) => {
  const [accounts, setAccounts] = useState<Account[]>([]);
  const [formData, setFormData] = useState({
    name: rule.name,
    description: rule.description,
    fromAccount: rule.fromAccount,
    toAccount: rule.toAccount,
    transferType: rule.transferType,
    percentage: rule.transferType === 'percentage' ? 
      (typeof rule.percentage === 'string' ? Number.parseFloat(rule.percentage) : rule.percentage) : undefined,
    amount: rule.transferType === 'amount' ? 
      (typeof rule.amount === 'string' ? Number.parseFloat(rule.amount) : rule.amount) : undefined,
    frequency: rule.frequency
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchAccounts();
  }, []);

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
      setError('Failed to load accounts');
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleTransferTypeChange = (type: 'percentage' | 'amount') => {
    setFormData(prev => ({
      ...prev,
      transferType: type,
      percentage: type === 'percentage' ? prev.percentage : undefined,
      amount: type === 'amount' ? prev.amount : undefined
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(`/api/rules/${rule.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error);
      }

      onSuccess();
    } catch (err) {
      console.error('Error updating rule:', err);
      setError(err instanceof Error ? err.message : 'Failed to update rule');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.editRule}>
      <div className={styles.header}>
        <button className={styles.backBtn} onClick={onBack}>
          ← Back
        </button>
        <div>
          <h2>Edit Rule</h2>
          <p>Update your automatic transfer rule</p>
        </div>
      </div>

      {error && (
        <div className={styles.error}>
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className={styles.form}>
        <div className={styles.field}>
          <label htmlFor="name">Rule Name *</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            placeholder="e.g., Emergency Fund Transfer"
            required
          />
        </div>

        <div className={styles.field}>
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleInputChange}
            placeholder="Optional description of this rule"
            rows={3}
          />
        </div>

        <div className={styles.fieldRow}>
          <div className={styles.field}>
            <label htmlFor="fromAccount">From Account *</label>
            <select
              id="fromAccount"
              name="fromAccount"
              value={formData.fromAccount}
              onChange={handleInputChange}
              required
            >
              <option value="">Select source account</option>
              {accounts.map(account => (
                <option key={account.account_id} value={account.account_id}>
                  {account.custom_name || account.name} ({account.type})
                </option>
              ))}
            </select>
          </div>

          <div className={styles.field}>
            <label htmlFor="toAccount">To Account *</label>
            <select
              id="toAccount"
              name="toAccount"
              value={formData.toAccount}
              onChange={handleInputChange}
              required
            >
              <option value="">Select destination account</option>
              {accounts.map(account => (
                <option key={account.account_id} value={account.account_id}>
                  {account.custom_name || account.name} ({account.type})
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className={styles.field}>
          <label>Transfer Type *</label>
          <div className={styles.transferTypeToggle}>
            <button
              type="button"
              className={`${styles.toggleBtn} ${formData.transferType === 'percentage' ? styles.active : ''}`}
              onClick={() => handleTransferTypeChange('percentage')}
            >
              Percentage
            </button>
            <button
              type="button"
              className={`${styles.toggleBtn} ${formData.transferType === 'amount' ? styles.active : ''}`}
              onClick={() => handleTransferTypeChange('amount')}
            >
              Fixed Amount
            </button>
          </div>
        </div>

        {formData.transferType === 'percentage' ? (
          <div className={styles.field}>
            <label htmlFor="percentage">Percentage *</label>
            <div className={styles.inputGroup}>
              <input
                type="number"
                id="percentage"
                name="percentage"
                value={formData.percentage || ''}
                onChange={handleInputChange}
                placeholder="10"
                min="0.01"
                max="100"
                step="0.01"
                required
              />
              <span className={styles.inputSuffix}>%</span>
            </div>
          </div>
        ) : (
          <div className={styles.field}>
            <label htmlFor="amount">Amount *</label>
            <div className={styles.inputGroup}>
              <span className={styles.inputPrefix}>$</span>
              <input
                type="number"
                id="amount"
                name="amount"
                value={formData.amount || ''}
                onChange={handleInputChange}
                placeholder="100.00"
                min="0.01"
                step="0.01"
                required
              />
            </div>
          </div>
        )}

        <div className={styles.field}>
          <label htmlFor="frequency">Frequency *</label>
          <select
            id="frequency"
            name="frequency"
            value={formData.frequency}
            onChange={handleInputChange}
            required
          >
            <option value="daily">Daily</option>
            <option value="weekly">Weekly</option>
            <option value="biweekly">Bi-weekly</option>
            <option value="monthly">Monthly</option>
            <option value="quarterly">Quarterly</option>
            <option value="yearly">Yearly</option>
          </select>
        </div>

        <div className={styles.actions}>
          <button
            type="button"
            className={styles.cancelBtn}
            onClick={onBack}
          >
            Cancel
          </button>
          <button
            type="submit"
            className={styles.updateBtn}
            disabled={isLoading}
          >
            {isLoading ? 'Updating...' : 'Update Rule'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditRule;