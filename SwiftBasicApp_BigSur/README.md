# SwiftBasicApp_BigSur

A basic Swift iOS application specifically designed to be compatible with **macOS Big Sur 11.7.10**.

## ✅ Big Sur Compatibility

This app is specifically configured to work with:
- **macOS Big Sur 11.7.10**
- **Xcode 13.2.1** (maximum version supported on Big Sur)
- **iOS 14.0+** deployment target
- **Swift 5.0**

## Key Differences from Modern Swift Apps

### Compatible Settings:
- ✅ Object version 50 (compatible with Xcode 13.2.1)
- ✅ iOS 14.0 deployment target
- ✅ Xcode 9.3 compatibility version
- ✅ Manual Info.plist file
- ✅ Traditional SwiftUI syntax (no #Preview)
- ✅ Standard build settings without modern sandboxing

### Features Included:
- Simple "Hello, World!" interface using SwiftUI
- Globe icon using SF Symbols
- Compatible color and styling
- Standard app icon configuration
- Preview support for Xcode 13.2

## How to Run on Big Sur

### Prerequisites:
1. **macOS Big Sur 11.7.10**
2. **Xcode 13.2.1** (available from Apple Developer Downloads)

### Steps:
1. Open `SwiftBasicApp_BigSur.xcodeproj` in Xcode 13.2.1
2. Select an iOS 14.0+ simulator or device
3. Press Cmd+R to build and run

## Project Structure

```
SwiftBasicApp_BigSur/
├── SwiftBasicApp_BigSur.xcodeproj/     # Xcode project (Big Sur compatible)
└── SwiftBasicApp_BigSur/               # Source code folder
    ├── SwiftBasicApp_BigSurApp.swift   # Main app entry point
    ├── ContentView.swift               # Main UI view (Big Sur compatible)
    ├── Info.plist                     # App configuration (required for Xcode 13.2)
    ├── Assets.xcassets/                # App icons and assets
    └── Preview Content/                # Preview assets
```

## What You'll See

The app displays:
- 🌍 A globe icon (SF Symbol)
- 📱 "Hello, World!" in large text
- 🎯 "Welcome to SwiftBasicApp" in blue
- ℹ️ "Compatible with Big Sur" subtitle

## Version Comparison

| Feature | Original App | Big Sur Version |
|---------|-------------|-----------------|
| Xcode Version | 15.0+ | 13.2.1 |
| iOS Target | 17.0+ | 14.0+ |
| Object Version | 56 | 50 |
| Info.plist | Auto-generated | Manual file |
| Preview Syntax | #Preview | PreviewProvider |
| Build Settings | Modern | Big Sur compatible |

## Troubleshooting

If you encounter issues:

1. **Verify Xcode Version**: Make sure you're using Xcode 13.2.1
2. **Check iOS Target**: Ensure you're targeting iOS 14.0 or later simulators
3. **Clean Build**: Product → Clean Build Folder (Cmd+Shift+K)
4. **Reset Simulator**: Device → Erase All Content and Settings

This version is specifically designed to work with the tools available on macOS Big Sur 11.7.10!