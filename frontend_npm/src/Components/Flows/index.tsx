import React from "react";
import styles from "./Flows.module.scss";

const Flows = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Flows</h1>
      <p className={styles.subtitle}>Monitor your cash flows and transactions</p>
      
      <div className={styles.content}>
        <div className={styles.placeholder}>
          <div className={styles.icon}>📊</div>
          <h3>No Flow Data</h3>
          <p>Connect accounts to see your cash flow analytics</p>
        </div>
      </div>
    </div>
  );
};

Flows.displayName = "Flows";

export default Flows;