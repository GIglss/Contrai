import React from "react";
import styles from "./BottomNavigation.module.scss";

interface BottomNavigationProps {
  activeTab: 'accounts' | 'rules' | 'flows' | 'chat';
  onTabChange: (tab: 'accounts' | 'rules' | 'flows' | 'chat') => void;
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
      
      <button 
        className={`${styles.navItem} ${activeTab === 'chat' ? styles.active : ''}`}
        onClick={() => onTabChange('chat')}
      >
        <div className={styles.icon}>💬</div>
        <span className={styles.label}>Chat</span>
      </button>
    </div>
  );
};

BottomNavigation.displayName = "BottomNavigation";

export default BottomNavigation;