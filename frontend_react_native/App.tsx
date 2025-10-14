import React, { useEffect, useContext, useCallback } from "react";
import {
  SafeAreaView,
  ScrollView,
  StyleSheet,
  Text,
  View,
  StatusBar,
} from "react-native";

import Header from "./src/components/Header";
// import Products from "./src/components/Products";
// import Items from "./src/components/Items";
import { QuickstartProvider } from "./src/context";
import Context from "./src/context";

const AppContent = () => {
  const { linkSuccess, isPaymentInitiation, itemId, dispatch } =
    useContext(Context);

  const getInfo = useCallback(async () => {
    try {
      const response = await fetch("/api/info", { method: "POST" });
      if (!response.ok) {
        dispatch({ type: "SET_STATE", state: { backend: false } });
        return { paymentInitiation: false };
      }
      const data = await response.json();
      const paymentInitiation: boolean =
        data.products.includes("payment_initiation");
      // TODO: Add CRA product handling for React Native
      const isUserTokenFlow: boolean = false;
      const isCraProductsExclusively: boolean = false;
      
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
    } catch (error) {
      console.error("Error fetching info:", error);
      dispatch({ type: "SET_STATE", state: { backend: false } });
      return { paymentInitiation: false };
    }
  }, [dispatch]);

  const generateUserToken = useCallback(async () => {
    try {
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
    } catch (error) {
      console.error("Error generating user token:", error);
    }
  }, [dispatch]);

  const generateToken = useCallback(
    async (isPaymentInitiation: boolean) => {
      try {
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
      } catch (error) {
        console.error("Error generating token:", error);
      }
    },
    [dispatch]
  );

  useEffect(() => {
    const init = async () => {
      const { paymentInitiation, isUserTokenFlow } = await getInfo();
      
      if (isUserTokenFlow) {
        await generateUserToken();
      }
      generateToken(paymentInitiation);
    };
    init();
  }, [dispatch, generateToken, generateUserToken, getInfo]);

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#ffffff" />
      <ScrollView contentInsetAdjustmentBehavior="automatic" style={styles.scrollView}>
        <View style={styles.body}>
          <Header />
          {linkSuccess && (
            <View style={styles.sectionContainer}>
              <Text style={styles.sectionTitle}>Connected Successfully!</Text>
              <Text style={styles.sectionDescription}>
                Your bank account has been connected to Plaid.
              </Text>
              {/* TODO: Add Products and Items components */}
              {/* <Products />
              {!isPaymentInitiation && itemId && <Items />} */}
            </View>
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const App = () => {
  return (
    <QuickstartProvider>
      <AppContent />
    </QuickstartProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
  scrollView: {
    backgroundColor: '#ffffff',
  },
  body: {
    backgroundColor: '#ffffff',
    padding: 20,
  },
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
    color: '#000000',
    textAlign: 'center',
    marginBottom: 8,
  },
  sectionDescription: {
    fontSize: 16,
    fontWeight: '400',
    color: '#666666',
    textAlign: 'center',
  },
});

export default App;