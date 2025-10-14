import React, { useContext } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Alert,
} from "react-native";

import Link from "./Link";
import Context from "../context/index";

const Header = () => {
  const {
    itemId,
    accessToken,
    userToken,
    linkToken,
    linkSuccess,
    isItemAccess,
    backend,
    linkTokenError,
    isPaymentInitiation,
  } = useContext(Context);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Plaid Quickstart</Text>

      {!linkSuccess ? (
        <View>
          <Text style={styles.subtitle}>
            A sample end-to-end integration with Plaid
          </Text>
          <Text style={styles.introPar}>
            The Plaid flow begins when your user wants to connect their bank
            account to your app. Simulate this by clicking the button below to
            launch Link - the client-side component that your users will
            interact with in order to link their accounts to Plaid and allow you
            to access their accounts via the Plaid API.
          </Text>
          
          {/* message if backend is not running and there is no link token */}
          {!backend && (
            <View style={styles.warningContainer}>
              <Text style={styles.warningText}>
                Unable to fetch link_token: please make sure your backend server
                is running and that your .env file has been configured with your
                PLAID_CLIENT_ID and PLAID_SECRET.
              </Text>
            </View>
          )}
          
          {/* message if backend is running and there is no link token */}
          {linkToken == null && backend && (
            <View style={styles.warningContainer}>
              <Text style={styles.warningText}>
                Unable to fetch link_token: please make sure your backend server
                is running and your .env file has been configured correctly.
              </Text>
            </View>
          )}
          
          {/* show Link component when we have a link token */}
          {linkToken != null && (
            <Link />
          )}
          
          {/* Display any link token errors */}
          {linkTokenError.error_code && (
            <View style={styles.errorContainer}>
              <Text style={styles.errorText}>
                Error: {linkTokenError.error_message}
              </Text>
            </View>
          )}
        </View>
      ) : (
        <View>
          <Text style={styles.subtitle}>
            Connected successfully!
          </Text>
          <Text style={styles.introPar}>
            Your account is now connected to Plaid. You can now view your account data below.
          </Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 10,
    color: '#000',
  },
  subtitle: {
    fontSize: 18,
    fontWeight: '600',
    textAlign: 'center',
    marginBottom: 15,
    color: '#333',
  },
  introPar: {
    fontSize: 14,
    lineHeight: 20,
    textAlign: 'center',
    marginBottom: 20,
    color: '#666',
    paddingHorizontal: 10,
  },
  warningContainer: {
    backgroundColor: '#fff3cd',
    borderColor: '#ffeaa7',
    borderWidth: 1,
    borderRadius: 5,
    padding: 15,
    marginBottom: 15,
  },
  warningText: {
    color: '#856404',
    fontSize: 14,
    textAlign: 'center',
  },
  errorContainer: {
    backgroundColor: '#f8d7da',
    borderColor: '#f5c6cb',
    borderWidth: 1,
    borderRadius: 5,
    padding: 15,
    marginBottom: 15,
  },
  errorText: {
    color: '#721c24',
    fontSize: 14,
    textAlign: 'center',
  },
});

export default Header;