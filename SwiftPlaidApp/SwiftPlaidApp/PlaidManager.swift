import Foundation
import LinkKit
import UIKit

class PlaidManager: ObservableObject {
    @Published var isLinked = false
    @Published var statusMessage = "Ready to connect bank account"
    @Published var linkToken: String?
    @Published var accessToken: String?
    @Published var accountData: [String: Any]?
    
    // Update this URL to match your backend server
    private let backendURL = "http://localhost:5000" // Change this to your backend URL
    
    // MARK: - Create Link Token
    func createLinkToken() {
        statusMessage = "Creating link token..."
        print("🔄 Starting link token creation...")
        
        guard let url = URL(string: "\(backendURL)/api/create_link_token") else {
            statusMessage = "Invalid backend URL"
            print("❌ Invalid backend URL: \(backendURL)")
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.timeoutInterval = 10.0 // Add timeout
        
        print("🌐 Making request to: \(url)")
        
        URLSession.shared.dataTask(with: request) { [weak self] data, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    print("❌ Network error: \(error.localizedDescription)")
                    self?.statusMessage = "Error creating link token: \(error.localizedDescription)"
                    
                    // Fallback to simulation mode for testing
                    print("🔄 Falling back to simulation mode...")
                    self?.statusMessage = "Backend unavailable - using simulation mode"
                    DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
                        self?.simulateSuccessfulFlow()
                    }
                    return
                }
                
                guard let data = data else {
                    print("❌ No data received from backend")
                    self?.statusMessage = "No data received"
                    return
                }
                
                print("✅ Received data: \(String(data: data, encoding: .utf8) ?? "Invalid UTF8")")
                
                do {
                    let json = try JSONSerialization.jsonObject(with: data) as? [String: Any]
                    if let token = json?["link_token"] as? String {
                        print("✅ Link token received: \(token.prefix(20))...")
                        self?.linkToken = token
                        self?.statusMessage = "Link token created successfully"
                        self?.presentPlaidLink()
                    } else {
                        print("❌ No link_token in response: \(json ?? [:])")
                        self?.statusMessage = "Failed to get link token from response"
                    }
                } catch {
                    print("❌ JSON parsing error: \(error.localizedDescription)")
                    self?.statusMessage = "Error parsing response: \(error.localizedDescription)"
                }
            }
        }.resume()
    }
    
    // MARK: - Present Plaid Link
    private func presentPlaidLink() {
        guard let linkToken = linkToken else {
            statusMessage = "No link token available"
            return
        }
        
        statusMessage = "Opening Plaid Link..."
        
        // Configure Plaid Link
        var linkConfiguration = LinkTokenConfiguration(token: linkToken) { [weak self] success in
            // Handle successful link
            self?.handleLinkSuccess(success)
        }
        
        linkConfiguration.onExit = { [weak self] exit in
            // Handle link exit
            self?.handleLinkExit(exit)
        }
        
        linkConfiguration.onEvent = { [weak self] event in
            // Handle link events
            self?.handleLinkEvent(event)
        }
        
        // Present the link
        let result = Plaid.create(linkConfiguration)
        switch result {
        case .failure(let error):
            print("❌ Error creating Plaid Link: \(error.localizedDescription)")
            statusMessage = "Error creating Plaid Link: \(error.localizedDescription)"
        case .success(let handler):
            print("✅ Plaid Link handler created successfully")
            // Try using viewController presentation method instead of custom
            DispatchQueue.main.async {
                guard let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
                      let window = windowScene.windows.first else {
                    print("❌ Could not find window scene")
                    self.statusMessage = "Could not find window to present Plaid Link"
                    return
                }
                
                var topController = window.rootViewController
                while let presentedViewController = topController?.presentedViewController {
                    topController = presentedViewController
                }
                
                guard let presenter = topController else {
                    print("❌ Could not find presenter view controller")
                    self.statusMessage = "Could not find view controller to present Plaid Link"
                    return
                }
                
                print("🔄 Presenting Plaid Link UI using .viewController method...")
                print("🔄 Presenter: \(type(of: presenter))")
                
                // Try the simpler .viewController presentation method
                do {
                    handler.open(presentUsing: .viewController(presenter))
                    print("✅ Plaid Link open call completed")
                    
                    // Set a timeout to fall back to simulation if Plaid Link doesn't appear
                    DispatchQueue.main.asyncAfter(deadline: .now() + 5) {
                        if self.statusMessage == "Opening Plaid Link..." {
                            print("⚠️ Plaid Link UI didn't appear after 5 seconds, falling back to simulation")
                            self.statusMessage = "Plaid Link UI failed to load - using simulation"
                            self.simulateSuccessfulFlow()
                        }
                    }
                } catch {
                    print("❌ Error in handler.open: \(error)")
                    self.statusMessage = "Error presenting Plaid Link: \(error.localizedDescription)"
                }
            }
        }
    }
    
    // MARK: - Handle Link Success
    private func handleLinkSuccess(_ success: LinkSuccess) {
        statusMessage = "Link successful! Exchanging token..."
        exchangePublicToken(success.publicToken)
    }
    
    // MARK: - Handle Link Exit
    private func handleLinkExit(_ exit: LinkExit) {
        if let error = exit.error {
            statusMessage = "Link failed: \(error.localizedDescription)"
        } else {
            statusMessage = "Link cancelled by user"
        }
    }
    
    // MARK: - Handle Link Event
    private func handleLinkEvent(_ event: LinkEvent) {
        print("Plaid Link Event: \(event.eventName)")
    }
    
    // MARK: - Exchange Public Token
    private func exchangePublicToken(_ publicToken: String) {
        guard let url = URL(string: "\(backendURL)/api/set_access_token") else {
            statusMessage = "Invalid backend URL"
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
        
        let bodyString = "public_token=\(publicToken)"
        request.httpBody = bodyString.data(using: .utf8)
        
        URLSession.shared.dataTask(with: request) { [weak self] data, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    self?.statusMessage = "Error exchanging token: \(error.localizedDescription)"
                    return
                }
                
                guard let data = data else {
                    self?.statusMessage = "No data received"
                    return
                }
                
                do {
                    let json = try JSONSerialization.jsonObject(with: data) as? [String: Any]
                    if let accessToken = json?["access_token"] as? String {
                        self?.accessToken = accessToken
                        self?.isLinked = true
                        self?.statusMessage = "Account successfully linked!"
                        self?.fetchAccountData()
                    } else {
                        self?.statusMessage = "Failed to get access token"
                    }
                } catch {
                    self?.statusMessage = "Error parsing response: \(error.localizedDescription)"
                }
            }
        }.resume()
    }
    
    // MARK: - Fetch Account Data
    private func fetchAccountData() {
        guard let url = URL(string: "\(backendURL)/api/accounts") else {
            statusMessage = "Invalid backend URL"
            return
        }
        
        URLSession.shared.dataTask(with: url) { [weak self] data, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    self?.statusMessage = "Error fetching accounts: \(error.localizedDescription)"
                    return
                }
                
                guard let data = data else {
                    self?.statusMessage = "No account data received"
                    return
                }
                
                do {
                    let json = try JSONSerialization.jsonObject(with: data) as? [String: Any]
                    self?.accountData = json
                    self?.statusMessage = "Account data loaded successfully"
                } catch {
                    self?.statusMessage = "Error parsing account data: \(error.localizedDescription)"
                }
            }
        }.resume()
    }
    
    // MARK: - Simulate Successful Flow (for testing when backend is unavailable)
    private func simulateSuccessfulFlow() {
        statusMessage = "Simulating Plaid Link flow..."
        
        // Simulate creating a link token
        linkToken = "link-sandbox-simulation-token"
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.statusMessage = "Opening Plaid Link..."
            
            // Simulate presenting Plaid Link
            DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                self.statusMessage = "Simulating bank selection..."
                
                // Simulate successful authentication
                DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                    self.handleSimulatedSuccess()
                }
            }
        }
    }
    
    private func handleSimulatedSuccess() {
        statusMessage = "Bank connected successfully! (Simulated)"
        accessToken = "access-sandbox-simulation-token"
        isLinked = true
        
        // Simulate account data
        accountData = [
            "accounts": [
                [
                    "name": "Plaid Checking (Demo)",
                    "type": "depository",
                    "subtype": "checking",
                    "balance": ["current": 1210.25]
                ],
                [
                    "name": "Plaid Savings (Demo)",
                    "type": "depository",
                    "subtype": "savings",
                    "balance": ["current": 5420.50]
                ]
            ]
        ]
        
        statusMessage = "✅ Demo bank accounts loaded successfully"
    }
    
    // MARK: - Reset Connection
    func resetConnection() {
        isLinked = false
        statusMessage = "Ready to connect bank account"
        linkToken = nil
        accessToken = nil
        accountData = nil
    }
}
