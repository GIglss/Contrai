import React from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Alert,
} from 'react-native';

const App = () => {
  const showAlert = () => {
    Alert.alert(
      'Hello!',
      'Welcome to your Simple React Native App!',
      [{text: 'OK', onPress: () => console.log('OK Pressed')}]
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#f8f9fa" />
      <ScrollView
        contentInsetAdjustmentBehavior="automatic"
        style={styles.scrollView}>
        <View style={styles.header}>
          <Text style={styles.title}>Simple React Native App</Text>
          <Text style={styles.subtitle}>Running in Docker Container</Text>
        </View>
        
        <View style={styles.content}>
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Welcome!</Text>
            <Text style={styles.sectionDescription}>
              This is a simple React Native app designed to run in Docker and be tested on Android Studio emulator.
            </Text>
          </View>
          
          <TouchableOpacity style={styles.button} onPress={showAlert}>
            <Text style={styles.buttonText}>Press Me!</Text>
          </TouchableOpacity>
          
          <View style={styles.infoBox}>
            <Text style={styles.infoTitle}>App Information:</Text>
            <Text style={styles.infoText}>• Built with React Native 0.73</Text>
            <Text style={styles.infoText}>• Dockerized for easy deployment</Text>
            <Text style={styles.infoText}>• Android Studio emulator ready</Text>
            <Text style={styles.infoText}>• Simple and clean interface</Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  scrollView: {
    flex: 1,
  },
  header: {
    backgroundColor: '#007bff',
    padding: 30,
    alignItems: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#ffffff',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#e3f2fd',
    marginTop: 8,
    textAlign: 'center',
  },
  content: {
    padding: 20,
  },
  section: {
    marginBottom: 30,
  },
  sectionTitle: {
    fontSize: 22,
    fontWeight: '600',
    color: '#212529',
    marginBottom: 10,
  },
  sectionDescription: {
    fontSize: 16,
    color: '#6c757d',
    lineHeight: 24,
  },
  button: {
    backgroundColor: '#28a745',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginBottom: 30,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 3.84,
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: '600',
  },
  infoBox: {
    backgroundColor: '#e9ecef',
    padding: 20,
    borderRadius: 8,
    borderLeftWidth: 4,
    borderLeftColor: '#007bff',
  },
  infoTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#212529',
    marginBottom: 10,
  },
  infoText: {
    fontSize: 14,
    color: '#495057',
    marginBottom: 5,
  },
});

export default App;