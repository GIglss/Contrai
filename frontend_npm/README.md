# Frontend React App

This is a React TypeScript application that can be run in the browser or deployed to iOS using Capacitor.

## Prerequisites

- **Node.js**: Version `>=14.0.0` (recommended: `v20.11.1` as specified in `.nvmrc`)
- **npm**: Should come with Node.js
- **For iOS deployment**: Xcode (macOS required)

## Running the App in Browser

### 1. Install Dependencies
If not already installed:
```bash
npm install
```

### 2. Start the Development Server
```bash
npm start
```

The app will automatically open in your browser at `http://localhost:3000`

### 3. Available Scripts
- `npm start` - Runs the app in development mode
- `npm run build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm run eject` - Ejects from Create React App (one-way operation)

## Backend Server Setup

Before running the frontend, make sure the backend server is running:

### 1. Navigate to Backend Directory
```bash
cd ..\backend\backend_plaid\python
```

### 2. Start the Backend Server
```bash
python server.py
```

The backend should be running and accessible for the frontend to communicate with it.

## Deploying to iOS with Capacitor

### 1. Install Capacitor
```bash
npm install @capacitor/core @capacitor/cli
```

### 2. Initialize Capacitor
```bash
npx cap init
```
- **App name**: Enter your app name (e.g., "Contrai App")
- **App ID**: Enter a unique identifier (e.g., "com.contrai.app")

### 3. Build the React App
```bash
npm run build
```
This creates a `build` folder with your production-ready app.

### 4. Add the iOS Platform
```bash
npx cap add ios
```

### 5. Copy Build to Native Project
```bash
npx cap copy
```

### 6. Open in Xcode
```bash
npx cap open ios
```

### 7. Build and Deploy from Xcode
- From Xcode, you can:
  - Run on iOS Simulator
  - Deploy to a physical iOS device
  - Submit to the App Store

### 8. Sync Changes (After Making Updates)
When you make changes to your React app:
```bash
npm run build
npx cap copy
```

## Relaunching on iOS After App Updates

When you make changes to your React app and want to test them on iOS:

### Quick Update Process
1. **Build the updated React app:**
   ```bash
   npm run build
   ```

2. **Copy changes to iOS project:**
   ```bash
   npx cap copy
   ```

3. **Open Xcode (if not already open):**
   ```bash
   npx cap open ios
   ```

4. **Clean and rebuild in Xcode:**
   - In Xcode: `Product` → `Clean Build Folder` (Cmd+Shift+K)
   - Then: `Product` → `Build` (Cmd+B)

5. **Run on device/simulator:**
   - Click the Play button in Xcode or press Cmd+R

### Alternative: Sync Command
You can also use the sync command which combines copy and update:
```bash
npx cap sync ios
```

### When to Use Full Rebuild
If you've made significant changes (added new plugins, changed configuration):
1. **Stop any running instances**
2. **Clean everything:**
   ```bash
   npm run build
   npx cap sync ios
   ```
3. **In Xcode, clean build folder and rebuild**
4. **Run the app**

### Live Reload (Development)
For faster development cycles, you can enable live reload:
1. **Start your React dev server:**
   ```bash
   npm start
   ```
2. **Update your capacitor.config.ts to point to your local server:**
   ```typescript
   server: {
     url: 'http://localhost:3000',
     cleartext: true
   }
   ```
3. **Sync and run:**
   ```bash
   npx cap copy ios
   npx cap open ios
   ```

**Note:** Remember to remove the server configuration before building for production!

## Project Structure

```
frontend_npm/
├── public/              # Static assets
├── src/                 # Source code
├── build/              # Production build (created after npm run build)
├── ios/                # iOS native project (created after npx cap add ios)
├── package.json        # Dependencies and scripts
├── tsconfig.json       # TypeScript configuration
├── capacitor.config.ts # Capacitor configuration
└── README.md          # This file
```

## Troubleshooting

### Common Issues
1. **Port already in use**: Change the port by setting the `PORT` environment variable
2. **Build errors**: Check that all dependencies are installed with `npm install`
3. **Capacitor issues**: Ensure you've run `npm run build` before `npx cap copy`

### Development Tips
- The app uses TypeScript, so type errors will be shown in the terminal and browser
- Hot reloading is enabled in development mode
- Check the browser console for any runtime errors

## Environment Configuration

The app may require environment variables. Check if there's a `.env` file or create one based on your backend configuration:

```
REACT_APP_API_URL=http://localhost:5000
```

Replace the URL with your actual backend server address.