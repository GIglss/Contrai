import React, { useState, useEffect } from "react";
import styles from "./Flows.module.scss";

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

const Flows = () => {
  const [accounts, setAccounts] = useState<Account[]>([]);
  const [rules, setRules] = useState<Rule[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [accountsResponse, rulesResponse] = await Promise.all([
        fetch('/api/get_all_connected_accounts'),
        fetch('/api/rules')
      ]);

      const accountsData = await accountsResponse.json();
      const rulesData = await rulesResponse.json();

      if (accountsData.error) {
        throw new Error(accountsData.error);
      }
      if (rulesData.error) {
        throw new Error(rulesData.error);
      }

      setAccounts(accountsData.accounts || []);
      setRules(rulesData.rules || []);
    } catch (err) {
      console.error('Error fetching data:', err);
      setError('Failed to load flow data');
    } finally {
      setLoading(false);
    }
  };

  const getAccountName = (accountId: string) => {
    const account = accounts.find(acc => acc.account_id === accountId);
    if (!account) return 'Unknown Account';
    return account.custom_name || account.name;
  };

  const getAccountBalance = (accountId: string) => {
    const account = accounts.find(acc => acc.account_id === accountId);
    return account ? account.balance : 0;
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  };

  const formatAmount = (rule: Rule) => {
    if (rule.transferType === 'percentage') {
      const percentage = typeof rule.percentage === 'string' ? Number.parseFloat(rule.percentage) : rule.percentage;
      return `${percentage || 0}%`;
    } else {
      const amount = typeof rule.amount === 'string' ? Number.parseFloat(rule.amount) : rule.amount;
      return formatCurrency(amount || 0);
    }
  };

  const getActiveRules = () => rules.filter(rule => rule.isActive);

  const getTotalBalance = () => {
    return accounts.reduce((total, account) => total + (account.balance || 0), 0);
  };

  const getUniqueAccounts = (): string[] => {
    const activeRules = getActiveRules();
    const accountIds = new Set<string>();
    
    activeRules.forEach(rule => {
      accountIds.add(rule.fromAccount);
      accountIds.add(rule.toAccount);
    });
    
    return Array.from(accountIds);
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading flow data...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={styles.container}>
        <div className={styles.error}>{error}</div>
      </div>
    );
  }

  const activeRules = getActiveRules();
  const uniqueAccounts = getUniqueAccounts();

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1 className={styles.title}>Flow Visualization</h1>
        <p className={styles.subtitle}>See how your money flows</p>
      </div>

      {activeRules.length === 0 ? (
        <div className={styles.noFlows}>
          <div className={styles.icon}>📊</div>
          <h3>No Active Flows</h3>
          <p>Create and activate rules to see your money flow visualization</p>
        </div>
      ) : (
        <div className={styles.content}>
          {/* Flow Visualization */}
          <div className={styles.visualizationSection}>
            <div className={styles.flowDiagram}>
              {activeRules.length === 1 ? (
                // Simple two-account flow
                <div className={styles.simpleFlow}>
                  <div className={styles.accountCircle}>
                    <span className={styles.accountLabel}>
                      {getAccountName(activeRules[0].fromAccount)}
                    </span>
                  </div>
                  
                  <div className={styles.connectionLine}>
                    <div className={styles.flowLine}></div>
                    <div className={styles.connectionDetails}>
                      <span className={styles.flowAmount}>{formatAmount(activeRules[0])}</span>
                      <span className={styles.flowFrequency}>{activeRules[0].frequency}</span>
                    </div>
                  </div>
                  
                  <div className={styles.accountCircle}>
                    <span className={styles.accountLabel}>
                      {getAccountName(activeRules[0].toAccount)}
                    </span>
                  </div>
                </div>
              ) : (
                // Complex multi-account flow with network layout
                <div className={styles.networkFlow}>
                  <svg className={styles.flowSvg} viewBox="0 0 400 300">
                    {/* Draw connection lines first */}
                    {activeRules.map((rule, index) => {
                      const fromIndex = uniqueAccounts.indexOf(rule.fromAccount);
                      const toIndex = uniqueAccounts.indexOf(rule.toAccount);
                      
                      // Calculate positions for accounts in a circle
                      const centerX = 200;
                      const centerY = 150;
                      const radius = 120;
                      const fromAngle = (fromIndex / uniqueAccounts.length) * 2 * Math.PI;
                      const toAngle = (toIndex / uniqueAccounts.length) * 2 * Math.PI;
                      
                      const fromX = centerX + radius * Math.cos(fromAngle);
                      const fromY = centerY + radius * Math.sin(fromAngle);
                      const toX = centerX + radius * Math.cos(toAngle);
                      const toY = centerY + radius * Math.sin(toAngle);
                      
                      // Calculate midpoint for the label
                      const midX = (fromX + toX) / 2;
                      const midY = (fromY + toY) / 2;
                      
                      return (
                        <g key={`connection-${index}`}>
                          {/* Connection line */}
                          <line
                            x1={fromX}
                            y1={fromY}
                            x2={toX}
                            y2={toY}
                            stroke="#007aff"
                            strokeWidth="2"
                            markerEnd="url(#arrowhead)"
                          />
                          
                          {/* Transfer details label */}
                          <foreignObject x={midX - 30} y={midY - 15} width="60" height="30">
                            <div className={styles.transferLabel}>
                              <div className={styles.transferAmount}>{formatAmount(rule)}</div>
                              <div className={styles.transferFreq}>{rule.frequency}</div>
                            </div>
                          </foreignObject>
                        </g>
                      );
                    })}
                    
                    {/* Arrow marker definition */}
                    <defs>
                      <marker
                        id="arrowhead"
                        markerWidth="10"
                        markerHeight="7"
                        refX="9"
                        refY="3.5"
                        orient="auto"
                      >
                        <polygon
                          points="0 0, 10 3.5, 0 7"
                          fill="#007aff"
                        />
                      </marker>
                    </defs>
                  </svg>
                  
                  {/* Account nodes positioned absolutely */}
                  {uniqueAccounts.map((accountId, index) => {
                    const centerX = 200;
                    const centerY = 150;
                    const radius = 120;
                    const angle = (index / uniqueAccounts.length) * 2 * Math.PI;
                    const x = centerX + radius * Math.cos(angle);
                    const y = centerY + radius * Math.sin(angle);
                    
                    return (
                      <div
                        key={accountId}
                        className={styles.networkNode}
                        style={{
                          left: `${(x / 400) * 100}%`,
                          top: `${(y / 300) * 100}%`,
                        }}
                      >
                        <div className={styles.accountCircle}>
                          <span className={styles.accountLabel}>
                            {getAccountName(accountId)}
                          </span>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>

          {/* Flow Summary */}
          <div className={styles.summarySection}>
            <h3>Flow Summary</h3>
            <div className={styles.summaryGrid}>
              <div className={styles.summaryCard}>
                <div className={styles.summaryLabel}>Total Accounts</div>
                <div className={styles.summaryValue}>{accounts.length}</div>
              </div>
              <div className={styles.summaryCard}>
                <div className={styles.summaryLabel}>Active Rules</div>
                <div className={styles.summaryValue}>{activeRules.length}</div>
              </div>
              <div className={styles.summaryCard}>
                <div className={styles.summaryLabel}>Total Balance</div>
                <div className={styles.summaryValue}>{formatCurrency(getTotalBalance())}</div>
              </div>
              <div className={styles.summaryCard}>
                <div className={styles.summaryLabel}>Automation</div>
                <div className={styles.summaryValue}>Active</div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

Flows.displayName = "Flows";

export default Flows;