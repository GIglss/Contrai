# Simple React Native App

A simple React Native application designed to run in Docker and be tested on Android Studio emulator.

## 🚀 Features

- Simple and clean React Native interface
- Docker containerization for easy deployment
- Android Studio emulator ready
- Cross-platform compatibility
- Modern React Native 0.73 setup

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Docker Desktop** (for Windows/Mac) or Docker Engine (for Linux)
- **Android Studio** with Android SDK
- **Android Emulator** set up in Android Studio
- **Git** (optional, for version control)

## 🛠️ Setup Instructions

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd SimpleReactNativeApp
```

### 2. Android Studio Setup

1. **Install Android Studio** from [developer.android.com](https://developer.android.com/studio)

2. **Create an Android Virtual Device (AVD)**:
   - Open Android Studio
   - Go to Tools → AVD Manager
   - Click "Create Virtual Device"
   - Select a device (e.g., Pixel 4)
   - Choose a system image (API level 33 recommended)
   - Click Finish

3. **Start the Android Emulator**:
   - In AVD Manager, click the ▶️ button next to your virtual device
   - Wait for the emulator to fully boot up

### 3. Docker Setup

#### Method 1: Using Docker Compose (Recommended)

```bash
# Build and start the container
docker-compose up --build

# The app will be available at http://localhost:8081
```

#### Method 2: Using Docker Commands

```bash
# Build the Docker image
docker build -t simple-react-native-app .

# Run the container
docker run -p 8081:8081 -p 5037:5037 --privileged simple-react-native-app
```

### 4. Connect to Android Emulator

1. **Enable ADB over network** (if needed):
   ```bash
   # Connect to running container
   docker exec -it simple-react-native-app bash
   
   # Inside container, connect to host's ADB
   adb connect host.docker.internal:5555
   ```

2. **Install the app on emulator**:
   ```bash
   # From your host machine (outside Docker)
   # Make sure Android SDK is in your PATH
   adb install android/app/build/outputs/apk/debug/app-debug.apk
   ```

## 🚀 Quick Start Options

### Option 1: Simple Version (Recommended for Development)

If you're experiencing Docker build timeouts or just want to run the Metro bundler:

```cmd
cd C:\Users\TC434LA\SelfDev\Contrai\SimpleReactNativeApp
docker-compose -f docker-compose.alternative.yml up react-native-metro --build
```

This runs only the Metro bundler in a lightweight container. You'll need React Native CLI on your host machine to connect to Android emulator.

### Option 2: Full Version (Complete Android Environment)

For full Android development with ADB support:

```cmd
cd C:\Users\TC434LA\SelfDev\Contrai\SimpleReactNativeApp
docker-compose up --build
```

This includes Android SDK and ADB tools but requires larger downloads.

## 🎯 Usage

### Running the Development Server

The Docker container automatically starts the Metro bundler on port 8081.

### Building the Android APK

```bash
# Connect to the container
docker exec -it simple-react-native-app bash

# Build the Android APK
cd android
./gradlew assembleDebug
```

### Testing on Emulator

1. Ensure your Android emulator is running
2. The Docker container should automatically detect and connect to it
3. The app will be installed and can be launched from the emulator

## 🐛 Troubleshooting

### Common Issues

#### 1. "npm is not recognized" Error
- Install Node.js from [nodejs.org](https://nodejs.org/)
- Restart your terminal/command prompt
- Verify installation: `node --version` and `npm --version`

#### 2. Docker Build Timeout (Connection timed out)
**Problem**: Large packages (like OpenJDK) fail to download due to network timeouts.

**Solutions**:

**Option A: Use the Simple Dockerfile (Recommended)**
```cmd
# Use the lightweight version that only runs Metro bundler
docker-compose -f docker-compose.alternative.yml up react-native-metro
```

**Option B: Retry with improved Dockerfile**
```cmd
# The main Dockerfile now has better timeout handling
docker-compose up --build
```

**Option C: Build with different Docker settings**
```cmd
# Increase Docker build timeout
set DOCKER_BUILDKIT=0
docker build --network=host --progress=plain .
```

**Option D: Use different base image**
```cmd
# Try with Ubuntu instead of Debian
# Modify Dockerfile to use: FROM node:18-ubuntu
```

#### 3. Docker Container Won't Start
- Ensure Docker Desktop is running
- Check if ports 8081 and 5037 are available
- Try: `docker-compose down` then `docker-compose up --build`

#### 4. Can't Connect to Android Emulator
- Ensure the Android emulator is running before starting Docker
- Check ADB connection: `adb devices`
- Try restarting the ADB server: `adb kill-server` then `adb start-server`

#### 5. Metro Bundler Issues
- Clear Metro cache: `npx react-native start --reset-cache`
- Check if port 8081 is already in use
- Restart the Docker container

#### 6. Android Build Errors
- Ensure Android SDK is properly installed
- Check Java version (Java 11 required)
- Clean and rebuild: `cd android && ./gradlew clean && ./gradlew assembleDebug`

### Environment Variables

You can customize the app behavior using environment variables:

```bash
# In docker-compose.yml or when running docker run
REACT_NATIVE_PACKAGER_HOSTNAME=0.0.0.0  # Allow external connections
ANDROID_SDK_ROOT=/opt/android-sdk         # Android SDK location
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64  # Java installation path
```

## 📁 Project Structure

```
SimpleReactNativeApp/
├── App.js                 # Main React Native component
├── index.js              # App entry point
├── package.json          # Dependencies and scripts
├── app.json              # App configuration
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── babel.config.js       # Babel configuration
├── metro.config.js       # Metro bundler configuration
├── android/              # Android specific files
│   ├── app/
│   │   ├── build.gradle
│   │   └── src/main/
│   ├── build.gradle
│   └── gradle.properties
└── README.md             # This file
```

## 🔧 Development

### Making Changes

1. Edit the React Native code in `App.js`
2. The Docker container will automatically reload changes
3. Check the changes in your Android emulator

### Adding Dependencies

1. Modify `package.json` to add new dependencies
2. Rebuild the Docker container: `docker-compose up --build`

### Debugging

- Use React Native Debugger or Chrome DevTools
- Access Metro bundler at `http://localhost:8081`
- Check container logs: `docker-compose logs -f`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Ensure all prerequisites are installed correctly
3. Check Docker and Android Studio logs for detailed error messages
4. Create an issue in the repository with detailed error information

---

**Happy coding! 🎉**