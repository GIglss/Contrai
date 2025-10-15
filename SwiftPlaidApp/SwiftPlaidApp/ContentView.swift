import SwiftUI

struct ContentView: View {
    @StateObject private var plaidManager = PlaidManager()
    
    var body: some View {
        NavigationView {
            ZStack {
                Color.white
                    .ignoresSafeArea()
                
                VStack(spacing: 30) {
                    // Header
                    VStack(spacing: 10) {
                        Image(systemName: "creditcard.circle.fill")
                            .font(.system(size: 60))
                            .foregroundColor(.blue)
                        
                        Text("Plaid Link Test")
                            .font(.largeTitle)
                            .fontWeight(.bold)
                            .foregroundColor(.black)
                    }
                    
                    // Status Section
                    VStack(spacing: 15) {
                        Text("Status")
                            .font(.headline)
                            .foregroundColor(.gray)
                        
                        Text(plaidManager.statusMessage)
                            .font(.body)
                            .multilineTextAlignment(.center)
                            .foregroundColor(plaidManager.isLinked ? .green : .black)
                            .padding()
                            .background(Color.gray.opacity(0.1))
                            .cornerRadius(10)
                    }
                    
                    // Connection Button
                    if !plaidManager.isLinked {
                        Button(action: {
                            plaidManager.createLinkToken()
                        }) {
                            HStack {
                                Image(systemName: "link.circle.fill")
                                Text("Connect Bank Account")
                            }
                            .font(.headline)
                            .foregroundColor(.white)
                            .padding()
                            .background(Color.blue)
                            .cornerRadius(10)
                        }
                    } else {
                        // Success Actions
                        VStack(spacing: 15) {
                            Button(action: {
                                // Could navigate to account details
                            }) {
                                HStack {
                                    Image(systemName: "list.bullet.rectangle")
                                    Text("View Account Details")
                                }
                                .font(.headline)
                                .foregroundColor(.white)
                                .padding()
                                .background(Color.green)
                                .cornerRadius(10)
                            }
                            
                            Button(action: {
                                plaidManager.resetConnection()
                            }) {
                                HStack {
                                    Image(systemName: "arrow.counterclockwise")
                                    Text("Reset Connection")
                                }
                                .font(.subheadline)
                                .foregroundColor(.red)
                                .padding()
                                .background(Color.red.opacity(0.1))
                                .cornerRadius(10)
                            }
                        }
                    }
                    
                    // Account Data Display
                    if plaidManager.isLinked, let accountData = plaidManager.accountData {
                        AccountDataView(accountData: accountData)
                    }
                    
                    Spacer()
                    
                    // Backend Info
                    VStack(spacing: 5) {
                        Text("Backend: Python Flask")
                            .font(.caption)
                            .foregroundColor(.gray)
                        Text("SDK: Plaid Link iOS")
                            .font(.caption)
                            .foregroundColor(.gray)
                    }
                }
                .padding(20)
            }
            .navigationTitle("")
            .navigationBarHidden(true)
        }
    }
}

struct AccountDataView: View {
    let accountData: [String: Any]
    
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text("Connected Accounts")
                .font(.headline)
                .foregroundColor(.black)
            
            if let accounts = accountData["accounts"] as? [[String: Any]] {
                ForEach(Array(accounts.enumerated()), id: \.offset) { index, account in
                    HStack {
                        VStack(alignment: .leading, spacing: 5) {
                            Text(account["name"] as? String ?? "Unknown Account")
                                .font(.subheadline)
                                .fontWeight(.medium)
                            
                            Text(account["subtype"] as? String ?? "Unknown Type")
                                .font(.caption)
                                .foregroundColor(.gray)
                        }
                        
                        Spacer()
                        
                        if let balance = account["balance"] as? [String: Any],
                           let current = balance["current"] as? Double {
                            Text("$\(current, specifier: "%.2f")")
                                .font(.subheadline)
                                .fontWeight(.bold)
                                .foregroundColor(.green)
                        }
                    }
                    .padding()
                    .background(Color.green.opacity(0.1))
                    .cornerRadius(8)
                }
            }
        }
        .padding()
        .background(Color.gray.opacity(0.05))
        .cornerRadius(10)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}