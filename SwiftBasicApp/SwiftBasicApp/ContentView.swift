import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundStyle(.tint)
            Text("Hello, World!")
                .font(.title)
                .padding()
            Text("Welcome to SwiftBasicApp")
                .font(.headline)
                .foregroundColor(.blue)
        }
        .padding()
    }
}

#Preview {
    ContentView()
}