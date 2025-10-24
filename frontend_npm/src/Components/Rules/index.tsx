import React from "react";
import styles from "./Rules.module.scss";

const Rules = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Rules</h1>
      <p className={styles.subtitle}>Set up your financial rules and automation</p>
      
      <div className={styles.content}>
        <div className={styles.placeholder}>
          <div className={styles.icon}>⚙️</div>
          <h3>No Rules Set</h3>
          <p>Create rules to automate your financial management</p>
        </div>
      </div>
    </div>
  );
};

Rules.displayName = "Rules";

export default Rules;