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
        
        guard let url = URL(string: "\(backendURL)/api/create_link_token") else {
            statusMessage = "Invalid backend URL"
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        // request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        // // Send empty JSON body to avoid malformed request
        // let emptyBody = Data("{}"   .utf8)
        // request.httpBody = emptyBody
        
        URLSession.shared.dataTask(with: request) { [weak self] data, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    self?.statusMessage = "Error creating link token: \(error.localizedDescription)"
                    return
                }
                
                guard let data = data else {
                    self?.statusMessage = "No data received"
                    return
                }
                
                do {
                    let json = try JSONSerialization.jsonObject(with: data) as? [String: Any]
                    if let token = json?["link_token"] as? String {
                        self?.linkToken = token
                        self?.statusMessage = "Link token created successfully"
                        self?.presentPlaidLink()
                    } else {
                        self?.statusMessage = "Failed to get link token from response"
                    }
                } catch {
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
            statusMessage = "Error creating Plaid Link: \(error.localizedDescription)"
        case .success(let handler):
            // Present the actual Plaid Link UI
            DispatchQueue.main.async {
                if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
                   let window = windowScene.windows.first,
                   let rootViewController = window.rootViewController {
                    handler.open(presentUsing: rootViewController)
                } else {
                    self?.statusMessage = "Could not find root view controller to present Plaid Link"
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
    
    // MARK: - Reset Connection
    func resetConnection() {
        isLinked = false
        statusMessage = "Ready to connect bank account"
        linkToken = nil
        accessToken = nil
        accountData = nil
    }
}