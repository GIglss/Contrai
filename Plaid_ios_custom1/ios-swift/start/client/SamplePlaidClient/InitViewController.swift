//
//  ViewController.swift
//  SamplePlaidClient
//
//  Created by Todd Kerpelman on 8/17/23.
//

import UIKit

class InitViewController: UIViewController {
    
    @IBOutlet var userLabel: UILabel!
    @IBOutlet var statusLabel: UILabel!
    @IBOutlet var simpleCallResults: UILabel!
    
    
    @IBOutlet var connectToPlaid: UIButton!
    @IBOutlet var simpleCallButton: UIButton!
    @IBOutlet var getAccountsButton: UIButton!
    @IBOutlet var getBalanceButton: UIButton!
    let communicator = ServerCommunicator()

    @IBAction func makeSimpleCallWasPressed(_ sender: Any) {
        // Ask our server to make a call to the Plaid API on behalf of our user
        self.communicator.callMyServer(path: "/server/simple_auth", httpMethod: .get) { (result: Result<SimpleAuthResponse, ServerCommunicator.Error>) in
                    switch result {
                    case .success(let response):
                        self.simpleCallResults.text = "I retrieved routing number \(response.routingNumber) for \(response.accountName) (xxxxxxxxx\(response.accountMask))"
                    case .failure(let error):
                        print("Got an error \(error)")
                    }
                }
    }
    
    @IBAction func getAccountsWasPressed(_ sender: Any) {
        // Test our new get_accounts endpoint
        self.communicator.callMyServer(path: "/server/get_accounts", httpMethod: .get) { (result: Result<AccountsResponse, ServerCommunicator.Error>) in
                    switch result {
                    case .success(let response):
                        let accountCount = response.accounts.count
                        let firstAccount = response.accounts.first
                        self.simpleCallResults.text = "Found \(accountCount) accounts. First: \(firstAccount?.name ?? "Unknown") (\(firstAccount?.type ?? "Unknown"))"
                        
                        // Print detailed info to console for debugging
                        print("=== ACCOUNTS RESPONSE ===")
                        for account in response.accounts {
                            print("Account: \(account.name) | Type: \(account.type) | Subtype: \(account.subtype ?? "N/A") | ID: \(account.account_id)")
                        }
                    case .failure(let error):
                        print("Got an error fetching accounts: \(error)")
                        self.simpleCallResults.text = "Error fetching accounts"
                    }
                }
    }
    
    @IBAction func getBalanceWasPressed(_ sender: Any) {
        // Test our new get_balance endpoint
        self.communicator.callMyServer(path: "/server/get_balance", httpMethod: .get) { (result: Result<BalanceResponse, ServerCommunicator.Error>) in
                    switch result {
                    case .success(let response):
                        let accountCount = response.accounts.count
                        let totalBalance = response.accounts.compactMap { $0.balances?.current }.reduce(0, +)
                        self.simpleCallResults.text = "Found \(accountCount) accounts with total balance: $\(String(format: "%.2f", totalBalance))"
                        
                        // Print detailed balance info to console for debugging
                        print("=== BALANCE RESPONSE ===")
                        for account in response.accounts {
                            let current = account.balances?.current ?? 0
                            let available = account.balances?.available ?? 0
                            print("Account: \(account.name) | Current: $\(current) | Available: $\(available)")
                        }
                    case .failure(let error):
                        print("Got an error fetching balances: \(error)")
                        self.simpleCallResults.text = "Error fetching balances"
                    }
                }
    }
    
    private func determineUserStatus() {
        self.communicator.callMyServer(path: "/server/get_user_info", httpMethod: .get) {
            (result: Result<UserStatusResponse, ServerCommunicator.Error>) in
            
            switch result {
            case .success(let serverResponse):
                self.userLabel.text = "Hello user \(serverResponse.userId)!"
                switch serverResponse.userStatus {
                case .connected:
                    self.statusLabel.text = "You are connected to your bank via Plaid. Make a call!"
                    self.connectToPlaid.setTitle("Make a new connection", for: .normal)
                    self.simpleCallButton.isEnabled = true
                    self.getAccountsButton.isEnabled = true
                    self.getBalanceButton.isEnabled = true
                case .disconnected:
                    self.statusLabel.text = "You should connect to a bank"
                    self.connectToPlaid.setTitle("Connect", for: .normal)
                    self.simpleCallButton.isEnabled = false
                    self.getAccountsButton.isEnabled = false
                    self.getBalanceButton.isEnabled = false
                }
                self.connectToPlaid.isEnabled = true;
            case .failure(let error):
                print(error)
            }
        }
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        // We'll refresh this every time our view appears
        determineUserStatus()
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set the title for the navigation bar
        self.title = "Accounts"
        
        // Set the tab bar item
        self.tabBarItem = UITabBarItem(title: "Accounts", image: UIImage(systemName: "creditcard"), tag: 0)
    }
}
