import React, { useState, useEffect } from 'react';
import styles from './CreateRule.module.scss';

interface Account {
  account_id: string;
  name: string;
  custom_name?: string;
  type: string;
  subtype: string;
}

interface RuleData {
  name: string;
  description: string;
  fromAccount: string;
  toAccount: string;
  transferType: 'percentage' | 'amount';
  percentage?: number;
  amount?: number;
  frequency: string;
}

interface CreateRuleProps {
  onCancel?: () => void;
  onSuccess?: () => void;
}

const CreateRule: React.FC<CreateRuleProps> = ({ onCancel, onSuccess }) => {
  const [accounts, setAccounts] = useState<Account[]>([]);
  const [formData, setFormData] = useState<RuleData>({
    name: '',
    description: '',
    fromAccount: '',
    toAccount: '',
    transferType: 'percentage',
    frequency: 'monthly'
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
      const response = await fetch('/api/rules', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.error) {
        throw new Error(data.error);
      }

      // Reset form on success
      setFormData({
        name: '',
        description: '',
        fromAccount: '',
        toAccount: '',
        transferType: 'percentage',
        frequency: 'monthly'
      });

      if (onSuccess) {
        onSuccess();
      } else {
        alert('Rule created successfully!');
      }
    } catch (err) {
      console.error('Error creating rule:', err);
      setError(err instanceof Error ? err.message : 'Failed to create rule');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.createRule}>
      <div className={styles.header}>
        <h2>Create Flow Rule</h2>
        <p>Set up automatic transfers between your accounts</p>
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
            onClick={onCancel}
          >
            Cancel
          </button>
          <button
            type="submit"
            className={styles.createBtn}
            disabled={isLoading}
          >
            {isLoading ? 'Creating...' : 'Create Rule'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default CreateRule;