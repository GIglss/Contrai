# Plaid React Native Quickstart

This is a React Native version of the Plaid Quickstart application, converted from the original React DOM version in `frontend_npm`.

## Overview

This React Native app demonstrates how to integrate Plaid Link SDK to connect bank accounts in a mobile application. It's based on the web version but adapted for native mobile development.

## Key Differences from Web Version

### Technology Stack
- **React Native** instead of React DOM
- **react-native-plaid-link-sdk** instead of react-plaid-link
- **StyleSheet** instead of CSS/SCSS modules
- **AsyncStorage** instead of localStorage (when needed)
- **fetch** polyfill required for older React Native versions

### Architecture Changes
- Converted CSS/SCSS styles to React Native StyleSheet
- Replaced web-specific components with React Native equivalents
- Updated API calls to work in mobile environment
- Removed browser-specific features (OAuth redirects simplified)

## Project Structure

```
src/
├── components/
│   ├── Header.tsx          # Main header component (converted from web)
│   └── Link.tsx            # Plaid Link integration (adapted for RN)
├── context/
│   └── index.tsx           # Global state management (same as web)
└── utils/
    └── dataUtilities.ts    # Data formatting utilities (adapted for RN)
```

## Setup Instructions

### Prerequisites
- Node.js (≥18)
- React Native development environment set up
- iOS/Android development tools
- Backend server running (same as web version)

### Installation

1. Install dependencies:
```bash
npm install
```

2. For iOS development:
```bash
cd ios && pod install && cd ..
```

3. Run the application:
```bash
# For iOS
npm run ios

# For Android
npm run android
```

## Backend Requirements

This React Native app requires the same backend server as the web version. Make sure your backend:

1. Serves the same API endpoints:
   - `/api/info`
   - `/api/create_link_token`
   - `/api/create_link_token_for_payment`
   - `/api/set_access_token`
   - `/api/create_user_token`

2. Has CORS properly configured for mobile requests

3. Uses the same Plaid configuration

## Key Components

### App.tsx
Main application component that:
- Wraps the app in QuickstartProvider for state management
- Handles initial API calls to get info and generate tokens
- Renders the Header component and success states

### Header.tsx
Displays the main UI including:
- Title and description
- Error messages for backend connectivity
- Link component when token is available
- Success message when connected

### Link.tsx
Handles Plaid Link integration:
- Uses react-native-plaid-link-sdk
- Manages the OAuth flow for bank account connection
- Exchanges public token for access token
- Handles success and error callbacks

### Context
Global state management using React Context API:
- Same interface as web version
- Manages link tokens, access tokens, and connection state
- Handles all application state updates

## Mobile-Specific Considerations

### Navigation
- Uses React Navigation for multi-screen support (when extended)
- SafeAreaView for proper iOS notch handling

### Permissions
- May require network permissions on Android
- iOS requires proper Info.plist configuration for HTTP requests

### Storage
- Can use AsyncStorage for persisting tokens
- Keychain/Keystore integration for sensitive data

## Development Notes

### API Integration
The app expects the backend to be running on localhost. For mobile development:

1. **iOS Simulator**: Use `localhost` or `127.0.0.1`
2. **Android Emulator**: Use `10.0.2.2` instead of `localhost`
3. **Physical Devices**: Use your computer's IP address

### Debugging
- Use React Native Debugger for debugging
- Check Metro bundler for build issues
- Use device logs for runtime errors

## Next Steps

To complete this React Native version:

1. **Add remaining components**:
   - Products component for displaying connected accounts
   - Items component for account details
   - Transaction listings

2. **Add navigation**:
   - Multiple screens for different features
   - Tab navigation or stack navigation

3. **Add mobile features**:
   - Push notifications for transaction alerts
   - Biometric authentication
   - Offline support

4. **Testing**:
   - Unit tests for components
   - Integration tests for Plaid integration
   - Device testing on various screen sizes

## Troubleshooting

### Common Issues

1. **Metro bundler errors**: Clear cache with `npx react-native start --reset-cache`
2. **iOS build issues**: Clean build folder and rebuild
3. **Android build issues**: Clean gradle cache
4. **Network errors**: Check backend URL configuration for mobile environment

### Plaid Link Issues

1. **Link token errors**: Verify backend is running and configured correctly
2. **OAuth redirects**: Simplified for mobile, but ensure proper URL schemes if using custom redirects
3. **Public token exchange**: Check network connectivity and backend endpoints

This React Native version provides a solid foundation for building a mobile banking application with Plaid integration.