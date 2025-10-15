# Use Node.js LTS version
FROM node:18-bullseye

# Set working directory
WORKDIR /app

# Configure apt for better reliability and timeouts
RUN echo "Acquire::Retries \"3\";" > /etc/apt/apt.conf.d/80-retries && \
    echo "Acquire::http::Timeout \"300\";" > /etc/apt/apt.conf.d/80-timeout && \
    echo "Acquire::ftp::Timeout \"300\";" > /etc/apt/apt.conf.d/80-timeout

# Update package lists
RUN apt-get update

# Install basic tools first
RUN apt-get install -y --no-install-recommends \
    wget \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Java separately with better error handling
RUN apt-get update && \
    apt-get install -y --no-install-recommends --fix-missing \
    openjdk-11-jdk \
    && rm -rf /var/lib/apt/lists/*

# Install Android tools separately
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    android-tools-adb \
    android-tools-fastboot \
    && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Install Android SDK
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH=${PATH}:${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin:${ANDROID_SDK_ROOT}/platform-tools

RUN mkdir -p ${ANDROID_SDK_ROOT} && \
    cd ${ANDROID_SDK_ROOT} && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip && \
    unzip commandlinetools-linux-9477386_latest.zip && \
    mkdir -p cmdline-tools/latest && \
    mv cmdline-tools/* cmdline-tools/latest/ 2>/dev/null || true && \
    rm commandlinetools-linux-9477386_latest.zip

# Accept Android licenses
RUN yes | sdkmanager --licenses

# Install Android SDK components
RUN sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.0"

# Install React Native CLI globally
RUN npm install -g react-native-cli @react-native-community/cli

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Expose Metro bundler port and ADB port
EXPOSE 8081 5037

# # Set up entrypoint script
# RUN echo '#!/bin/bash\n\
# # Start ADB server\n\
# adb start-server\n\
# \n\
# # Start Metro bundler in background\n\
# npm start &\n\
# \n\
# # Wait for Metro to start\n\
# sleep 10\n\
# \n\
# # Keep container running\n\
# tail -f /dev/null' > /app/entrypoint.sh && \
#     chmod +x /app/entrypoint.sh

# CMD ["/bin/bash", "/app/entrypoint.sh"]

# Start ADB server and Metro bundler
CMD ["sh", "-c", "adb start-server && npm start"]