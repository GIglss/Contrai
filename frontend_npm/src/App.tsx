import React, { useEffect, useContext, useCallback, useState } from "react";

import Header from "./Components/Headers";
import AccountsConnected from "./Components/AccountsConnected";
import Rules from "./Components/Rules";
import Flows from "./Components/Flows";
import BottomNavigation from "./Components/BottomNavigation";
import Context from "./Context";

import styles from "./App.module.scss";
import { CraCheckReportProduct } from "plaid";

const App = () => {
  const { linkSuccess, isPaymentInitiation, itemId, dispatch } =
    useContext(Context);
  const [activeTab, setActiveTab] = useState<'accounts' | 'rules' | 'flows'>('accounts');

  const getInfo = useCallback(async () => {
    const response = await fetch("/api/info", { method: "POST" });
    if (!response.ok) {
      dispatch({ type: "SET_STATE", state: { backend: false } });
      return { paymentInitiation: false };
    }
    const data = await response.json();
    const paymentInitiation: boolean =
      data.products.includes("payment_initiation");
    const craEnumValues = Object.values(CraCheckReportProduct);
    const isUserTokenFlow: boolean = data.products.some(
      (product: CraCheckReportProduct) => craEnumValues.includes(product)
    );
    const isCraProductsExclusively: boolean = data.products.every(
      (product: CraCheckReportProduct) => craEnumValues.includes(product)
    );
    dispatch({
      type: "SET_STATE",
      state: {
        products: data.products,
        isPaymentInitiation: paymentInitiation,
        isCraProductsExclusively: isCraProductsExclusively,
        isUserTokenFlow: isUserTokenFlow,
      },
    });
    return { paymentInitiation, isUserTokenFlow };
  }, [dispatch]);

  const generateUserToken = useCallback(async () => {
    const response = await fetch("api/create_user_token", { method: "POST" });
    if (!response.ok) {
      dispatch({ type: "SET_STATE", state: { userToken: null } });
      return;
    }
    const data = await response.json();
    if (data) {
      if (data.error != null) {
        dispatch({
          type: "SET_STATE",
          state: {
            linkToken: null,
            linkTokenError: data.error,
          },
        });
        return;
      }
      dispatch({ type: "SET_STATE", state: { userToken: data.user_token } });
      return data.user_token;
    }
  }, [dispatch]);

  const generateToken = useCallback(
    async (isPaymentInitiation) => {
      // Link tokens for 'payment_initiation' use a different creation flow in your backend.
      const path = isPaymentInitiation
        ? "/api/create_link_token_for_payment"
        : "/api/create_link_token";
      const response = await fetch(path, {
        method: "POST",
      });
      if (!response.ok) {
        dispatch({ type: "SET_STATE", state: { linkToken: null } });
        return;
      }
      const data = await response.json();
      if (data) {
        if (data.error != null) {
          dispatch({
            type: "SET_STATE",
            state: {
              linkToken: null,
              linkTokenError: data.error,
            },
          });
          return;
        }
        dispatch({ type: "SET_STATE", state: { linkToken: data.link_token } });
      }
      // Save the link_token to be used later in the Oauth flow.
      localStorage.setItem("link_token", data.link_token);
    },
    [dispatch]
  );

  useEffect(() => {
    const init = async () => {
      const { paymentInitiation, isUserTokenFlow } = await getInfo(); // used to determine which path to take when generating token
      // do not generate a new token for OAuth redirect; instead
      // setLinkToken from localStorage
      if (window.location.href.includes("?oauth_state_id=")) {
        dispatch({
          type: "SET_STATE",
          state: {
            linkToken: localStorage.getItem("link_token"),
          },
        });
        return;
      }

      if (isUserTokenFlow) {
        await generateUserToken();
      }
      generateToken(paymentInitiation);
    };
    init();
  }, [dispatch, generateToken, generateUserToken, getInfo]);

  const renderCurrentPage = () => {
    switch (activeTab) {
      case 'accounts':
        return <AccountsConnected />;
      case 'rules':
        return <Rules />;
      case 'flows':
        return <Flows />;
      default:
        return <AccountsConnected />;
    }
  };

  return (
    <div className={styles.App}>
      <div className={styles.container}>
        <div className={styles.content}>
          {renderCurrentPage()}
        </div>
        <BottomNavigation 
          activeTab={activeTab} 
          onTabChange={setActiveTab} 
        />
      </div>
    </div>
  );
};

export default App;
