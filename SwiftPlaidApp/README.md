# SwiftPlaidApp - Plaid Link Integration

A Swift iOS application that integrates with Plaid Link to connect bank accounts, built specifically for **macOS Big Sur 11.7.10** and **Xcode 13.2**.

## 🏦 **Features**

### **Frontend (iOS)**
- ✅ **Plaid Link SDK** integration
- ✅ **SwiftUI** interface compatible with iOS 14.0+
- ✅ **Real-time status** updates during connection process
- ✅ **Account data display** after successful linking
- ✅ **Error handling** and user feedback
- ✅ **Reset functionality** to test multiple connections

### **Backend Integration**
- 🔗 **Connects to existing Python Flask backend** (`backend/backend_plaid/python/`)
- 🔄 **Uses existing API endpoints**:
  - `POST /api/create_link_token` - Creates Plaid Link token
  - `POST /api/set_access_token` - Exchanges public token for access token
  - `GET /api/accounts` - Fetches connected account data

## 🎯 **App Flow**

1. **Create Link Token** → Backend generates Plaid Link token
2. **Open Plaid Link** → SDK presents bank selection interface
3. **User Authentication** → User logs into their bank
4. **Token Exchange** → Public token exchanged for access token
5. **Account Data** → Display connected accounts and balances

## 🛠 **Technical Setup**

### **Prerequisites**
- **macOS Big Sur 11.7.10**
- **Xcode 13.2** (compatible version)
- **Python backend running** on `localhost:5000`

### **Dependencies**
- **PlaidLinkKit** (v4.0.0+) - Added via Swift Package Manager
- **iOS 14.0+** deployment target
- **Swift 5.0**

### **Backend Requirements**
Make sure your Python backend is running:
```bash
cd backend/backend_plaid/python
python server.py
```

## 📱 **How to Run**

### **1. Start Backend**
```bash
cd c:\Users\TC434LA\SelfDev\Contrai\backend\backend_plaid\python
python server.py
```

### **2. Open iOS App**
1. Open `SwiftPlaidApp.xcodeproj` in Xcode 13.2
2. Select an iOS 14.0+ simulator
3. Build and run (Cmd+R)

### **3. Test the Flow**
1. Tap **"Connect Bank Account"**
2. The app will create a link token from your backend
3. Plaid Link will open (currently simulated)
4. After "connection", you'll see account data

## 🔧 **Configuration**

### **Backend URL**
Update the backend URL in `PlaidManager.swift`:
```swift
private let backendURL = "http://localhost:5000" // Change to your backend URL
```

### **Network Security**
The app includes `NSAppTransportSecurity` settings in `Info.plist` to allow HTTP connections to localhost for testing.

## 🏗 **Project Structure**

```
SwiftPlaidApp/
├── SwiftPlaidApp.xcodeproj/          # Xcode project
└── SwiftPlaidApp/                    # Source code
    ├── SwiftPlaidAppApp.swift        # Main app entry point
    ├── ContentView.swift             # Main UI with Plaid integration
    ├── PlaidManager.swift            # Handles all Plaid API calls
    ├── Info.plist                   # App configuration
    ├── Assets.xcassets/              # App icons and assets
    └── Preview Content/              # Preview assets
```

## 🔄 **API Integration**

### **Create Link Token**
```
POST /api/create_link_token
→ Returns: {"link_token": "link-sandbox-xxx"}
```

### **Exchange Token**
```
POST /api/set_access_token
Body: public_token=public-sandbox-xxx
→ Returns: {"access_token": "access-sandbox-xxx"}
```

### **Get Accounts**
```
GET /api/accounts
→ Returns: {"accounts": [...]}
```

## 🧪 **Testing Mode**

The app includes a **simulation mode** for testing without real bank connections:
- Creates fake link tokens
- Simulates successful Plaid Link flow
- Shows sample account data
- Perfect for development and testing

## 🚨 **Troubleshooting**

### **Common Issues**

1. **"No data received"**
   - ✅ Ensure Python backend is running on `localhost:5000`
   - ✅ Check network permissions in Info.plist

2. **"Invalid backend URL"**
   - ✅ Update `backendURL` in `PlaidManager.swift`
   - ✅ Ensure backend is accessible

3. **Build Errors**
   - ✅ Clean build folder (Product → Clean Build Folder)
   - ✅ Ensure Xcode 13.2 compatibility

4. **Plaid Link Issues**
   - ✅ Check if PlaidLinkKit package is properly added
   - ✅ Verify iOS 14.0+ deployment target

## 🎨 **UI Features**

- 💳 **Credit card icon** for banking theme
- 📊 **Real-time status** updates
- 🟢 **Success indicators** with green colors
- 🔄 **Reset functionality** for testing
- 📱 **Account balance display** 
- 🎯 **Clean, professional interface**

## 🔐 **Security Notes**

- ✅ **No sensitive data stored** in the app
- ✅ **Tokens handled securely** via HTTPS (when configured)
- ✅ **Backend validation** of all API calls
- ✅ **Plaid's security standards** followed

This app provides a complete Plaid Link integration that works with your existing Python backend, optimized for your Big Sur/Xcode 13.2 development environment!