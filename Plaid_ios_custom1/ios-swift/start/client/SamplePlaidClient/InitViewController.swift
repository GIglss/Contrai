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
    @IBOutlet var connectToPlaid: UIButton!
    @IBOutlet var accountsStackView: UIStackView!
    @IBOutlet var scrollView: UIScrollView!
    
    let communicator = ServerCommunicator()
    
    private var accounts: [PlaidAccount] = []

    private func loadAccountsData() {
        // Load account data with balances when user is connected
        self.communicator.callMyServer(path: "/server/get_balance", httpMethod: .get) { (result: Result<BalanceResponse, ServerCommunicator.Error>) in
            switch result {
            case .success(let response):
                self.accounts = response.accounts
                self.displayAccountCards()
            case .failure(let error):
                print("Error loading accounts: \(error)")
                self.showErrorMessage("Failed to load accounts")
            }
        }
    }
    
    private func displayAccountCards() {
        // Clear existing cards
        accountsStackView.arrangedSubviews.forEach { $0.removeFromSuperview() }
        
        // Create a card for each account
        for account in accounts {
            let accountCard = createAccountCard(for: account)
            accountsStackView.addArrangedSubview(accountCard)
        }
        
        // Show accounts container
        scrollView.isHidden = false
    }
    
    private func createAccountCard(for account: PlaidAccount) -> UIView {
        let cardView = UIView()
        cardView.backgroundColor = UIColor.systemBackground
        cardView.layer.cornerRadius = 12
        cardView.layer.shadowColor = UIColor.black.cgColor
        cardView.layer.shadowOffset = CGSize(width: 0, height: 2)
        cardView.layer.shadowRadius = 4
        cardView.layer.shadowOpacity = 0.1
        cardView.layer.borderWidth = 1
        cardView.layer.borderColor = UIColor.systemGray5.cgColor
        
        // Account name label
        let nameLabel = UILabel()
        nameLabel.text = account.name
        nameLabel.font = UIFont.systemFont(ofSize: 18, weight: .semibold)
        nameLabel.textColor = UIColor.label
        
        // Account type label
        let typeLabel = UILabel()
        let accountType = "\(account.type.capitalized)"
        let accountSubtype = account.subtype?.capitalized ?? ""
        typeLabel.text = accountSubtype.isEmpty ? accountType : "\(accountType) • \(accountSubtype)"
        typeLabel.font = UIFont.systemFont(ofSize: 14, weight: .medium)
        typeLabel.textColor = UIColor.systemBlue
        
        // Account mask label
        let maskLabel = UILabel()
        maskLabel.text = "••••\(account.mask ?? "****")"
        maskLabel.font = UIFont.systemFont(ofSize: 14, weight: .regular)
        maskLabel.textColor = UIColor.secondaryLabel
        
        // Balance label
        let balanceLabel = UILabel()
        if let balance = account.balances?.current {
            let formatter = NumberFormatter()
            formatter.numberStyle = .currency
            formatter.currencyCode = account.balances?.iso_currency_code ?? "USD"
            balanceLabel.text = formatter.string(from: NSNumber(value: balance)) ?? "$0.00"
        } else {
            balanceLabel.text = "Balance unavailable"
        }
        balanceLabel.font = UIFont.systemFont(ofSize: 20, weight: .bold)
        balanceLabel.textColor = UIColor.label
        balanceLabel.textAlignment = .right
        
        // Available balance (if different from current)
        let availableLabel = UILabel()
        if let available = account.balances?.available,
           let current = account.balances?.current,
           available != current {
            let formatter = NumberFormatter()
            formatter.numberStyle = .currency
            formatter.currencyCode = account.balances?.iso_currency_code ?? "USD"
            availableLabel.text = "Available: \(formatter.string(from: NSNumber(value: available)) ?? "$0.00")"
            availableLabel.font = UIFont.systemFont(ofSize: 12, weight: .regular)
            availableLabel.textColor = UIColor.secondaryLabel
            availableLabel.textAlignment = .right
        }
        
        // Setup auto layout
        [nameLabel, typeLabel, maskLabel, balanceLabel, availableLabel].forEach {
            $0.translatesAutoresizingMaskIntoConstraints = false
            cardView.addSubview($0)
        }
        
        NSLayoutConstraint.activate([
            // Card height
            cardView.heightAnchor.constraint(greaterThanOrEqualToConstant: 80),
            
            // Name label - top left
            nameLabel.topAnchor.constraint(equalTo: cardView.topAnchor, constant: 16),
            nameLabel.leadingAnchor.constraint(equalTo: cardView.leadingAnchor, constant: 16),
            nameLabel.trailingAnchor.constraint(lessThanOrEqualTo: balanceLabel.leadingAnchor, constant: -8),
            
            // Type label - below name
            typeLabel.topAnchor.constraint(equalTo: nameLabel.bottomAnchor, constant: 4),
            typeLabel.leadingAnchor.constraint(equalTo: cardView.leadingAnchor, constant: 16),
            
            // Mask label - below type
            maskLabel.topAnchor.constraint(equalTo: typeLabel.bottomAnchor, constant: 4),
            maskLabel.leadingAnchor.constraint(equalTo: cardView.leadingAnchor, constant: 16),
            maskLabel.bottomAnchor.constraint(equalTo: cardView.bottomAnchor, constant: -16),
            
            // Balance label - top right
            balanceLabel.topAnchor.constraint(equalTo: cardView.topAnchor, constant: 16),
            balanceLabel.trailingAnchor.constraint(equalTo: cardView.trailingAnchor, constant: -16),
            
            // Available label - below balance (if visible)
            availableLabel.topAnchor.constraint(equalTo: balanceLabel.bottomAnchor, constant: 4),
            availableLabel.trailingAnchor.constraint(equalTo: cardView.trailingAnchor, constant: -16),
        ])
        
        return cardView
    }
    
    private func showErrorMessage(_ message: String) {
        statusLabel.text = message
        scrollView.isHidden = true
    }
    
    private func determineUserStatus() {
        self.communicator.callMyServer(path: "/server/get_user_info", httpMethod: .get) {
            (result: Result<UserStatusResponse, ServerCommunicator.Error>) in
            
            switch result {
            case .success(let serverResponse):
                self.userLabel.text = "Hello user \(serverResponse.userId)!"
                switch serverResponse.userStatus {
                case .connected:
                    self.statusLabel.text = "Your connected accounts:"
                    self.connectToPlaid.setTitle("Add another bank", for: .normal)
                    self.connectToPlaid.isEnabled = true
                    // Load and display account cards
                    self.loadAccountsData()
                case .disconnected:
                    self.statusLabel.text = "Connect your bank to get started"
                    self.connectToPlaid.setTitle("Connect to bank", for: .normal)
                    self.connectToPlaid.isEnabled = true
                    self.scrollView.isHidden = true
                }
            case .failure(let error):
                print(error)
                self.showErrorMessage("Failed to load user status")
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
        
        print("🏦 InitViewController (Accounts) loaded - console is working!")
        
        // Set the title for the navigation bar
        self.title = "Accounts"
        
        // Set the tab bar item
        self.tabBarItem = UITabBarItem(title: "Accounts", image: UIImage(systemName: "creditcard"), tag: 0)
    }
}
