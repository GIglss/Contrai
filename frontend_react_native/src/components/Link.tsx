import React, { useContext, useCallback } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  Alert,
} from "react-native";
import { 
  create,
  open,
  LinkSuccess,
  LinkExit,
} from 'react-native-plaid-link-sdk';

import Context from "../context/index";

const Link = () => {
  const { linkToken, isPaymentInitiation, isCraProductsExclusively, dispatch } =
    useContext(Context);

  const onSuccess = useCallback(
    async (success: LinkSuccess) => {
      const { publicToken } = success;
      
      // If the access_token is needed, send public_token to server
      const exchangePublicTokenForAccessToken = async () => {
        try {
          const response = await fetch("/api/set_access_token", {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            },
            body: `public_token=${publicToken}`,
          });
          
          if (!response.ok) {
            dispatch({
              type: "SET_STATE",
              state: {
                itemId: `no item_id retrieved`,
                accessToken: `no access_token retrieved`,
                isItemAccess: false,
              },
            });
            return;
          }
          
          const data = await response.json();
          dispatch({
            type: "SET_STATE",
            state: {
              itemId: data.item_id,
              accessToken: data.access_token,
              isItemAccess: true,
            },
          });
        } catch (error) {
          console.error("Error exchanging public token:", error);
          Alert.alert("Error", "Failed to exchange public token");
        }
      };

      // 'payment_initiation' products do not require the public_token to be exchanged for an access_token.
      if (isPaymentInitiation) {
        dispatch({ type: "SET_STATE", state: { isItemAccess: false } });
      } else if (isCraProductsExclusively) {
        // When only CRA products are enabled, only user_token is needed. access_token/public_token exchange is not needed.
        dispatch({ type: "SET_STATE", state: { isItemAccess: false } });
      } else {
        await exchangePublicTokenForAccessToken();
      }

      dispatch({ type: "SET_STATE", state: { linkSuccess: true } });
    },
    [dispatch, isPaymentInitiation, isCraProductsExclusively]
  );

  const onExit = useCallback(
    (exit: LinkExit) => {
      console.log("Plaid Link exited:", exit);
      if (exit.error) {
        dispatch({
          type: "SET_STATE",
          state: {
            linkTokenError: {
              error_type: exit.error.errorType,
              error_code: exit.error.errorCode,
              error_message: exit.error.errorMessage,
            },
          },
        });
      }
    },
    [dispatch]
  );

  const handlePress = useCallback(async () => {
    if (!linkToken) {
      Alert.alert("Error", "Link token not available");
      return;
    }

    try {
      const linkTokenConfiguration = {
        token: linkToken,
      };
      
      await create(linkTokenConfiguration);
      await open({
        onSuccess,
        onExit,
      });
    } catch (error) {
      console.error("Error opening Plaid Link:", error);
      Alert.alert("Error", "Failed to open Plaid Link");
    }
  }, [linkToken, onSuccess, onExit]);

  if (!linkToken) {
    return (
      <View style={styles.container}>
        <Text style={styles.loadingText}>Loading...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <TouchableOpacity style={styles.button} onPress={handlePress}>
        <Text style={styles.buttonText}>Connect your bank account</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  button: {
    backgroundColor: '#007AFF',
    paddingVertical: 15,
    paddingHorizontal: 30,
    borderRadius: 8,
    minWidth: 200,
  },
  buttonText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
    textAlign: 'center',
  },
  loadingText: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
  },
});

export default Link;