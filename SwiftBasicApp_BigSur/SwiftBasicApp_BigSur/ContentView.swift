import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
                .font(.system(size: 50))
            
            Text("Hello, World!")
                .font(.largeTitle)
                .fontWeight(.bold)
            
            Text("Welcome to SwiftBasicApp")
                .font(.title2)
                .foregroundColor(.blue)
                
            Text("Compatible with Big Sur")
                .font(.caption)
                .foregroundColor(.secondary)
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}