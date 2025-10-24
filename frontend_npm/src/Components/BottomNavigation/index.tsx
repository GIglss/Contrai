import React from "react";
import styles from "./BottomNavigation.module.scss";

interface BottomNavigationProps {
  activeTab: 'accounts' | 'rules' | 'flows';
  onTabChange: (tab: 'accounts' | 'rules' | 'flows') => void;
}

const BottomNavigation: React.FC<BottomNavigationProps> = ({ activeTab, onTabChange }) => {
  return (
    <div className={styles.navigation}>
      <button 
        className={`${styles.navItem} ${activeTab === 'accounts' ? styles.active : ''}`}
        onClick={() => onTabChange('accounts')}
      >
        <div className={styles.icon}>💳</div>
        <span className={styles.label}>Accounts</span>
      </button>
      
      <button 
        className={`${styles.navItem} ${activeTab === 'rules' ? styles.active : ''}`}
        onClick={() => onTabChange('rules')}
      >
        <div className={styles.icon}>⚙️</div>
        <span className={styles.label}>Rules</span>
      </button>
      
      <button 
        className={`${styles.navItem} ${activeTab === 'flows' ? styles.active : ''}`}
        onClick={() => onTabChange('flows')}
      >
        <div className={styles.icon}>📊</div>
        <span className={styles.label}>Flows</span>
      </button>
    </div>
  );
};

BottomNavigation.displayName = "BottomNavigation";

export default BottomNavigation;