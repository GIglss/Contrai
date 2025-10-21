//
//  DashboardViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/21/25.
//

import UIKit

struct Account {
    let id: String
    let name: String
    let balance: Double
    let type: String
    let mask: String
}

class DashboardViewController: UIViewController {
    
    private let scrollView = UIScrollView()
    private let contentView = UIView()
    private let headerView = UIView()
    private let totalBalanceLabel = UILabel()
    private let totalBalanceValueLabel = UILabel()
    private let tableView = UITableView()
    private let addAccountButton = UIButton(type: .system)
    
    private var accounts: [Account] = []
    private let communicator = ServerCommunicator()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViews()
        setupConstraints()
        setupUI()
        setupTableView()
        loadAccounts()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        loadAccounts()
    }
    
    private func setupViews() {
        view.addSubview(scrollView)
        scrollView.addSubview(contentView)
        contentView.addSubview(headerView)
        headerView.addSubview(totalBalanceLabel)
        headerView.addSubview(totalBalanceValueLabel)
        contentView.addSubview(tableView)
        contentView.addSubview(addAccountButton)
        
        scrollView.translatesAutoresizingMaskIntoConstraints = false
        contentView.translatesAutoresizingMaskIntoConstraints = false
        headerView.translatesAutoresizingMaskIntoConstraints = false
        totalBalanceLabel.translatesAutoresizingMaskIntoConstraints = false
        totalBalanceValueLabel.translatesAutoresizingMaskIntoConstraints = false
        tableView.translatesAutoresizingMaskIntoConstraints = false
        addAccountButton.translatesAutoresizingMaskIntoConstraints = false
    }
    
    private func setupConstraints() {
        NSLayoutConstraint.activate([
            // ScrollView
            scrollView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            scrollView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            
            // Content View
            contentView.topAnchor.constraint(equalTo: scrollView.topAnchor),
            contentView.leadingAnchor.constraint(equalTo: scrollView.leadingAnchor),
            contentView.trailingAnchor.constraint(equalTo: scrollView.trailingAnchor),
            contentView.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor),
            contentView.widthAnchor.constraint(equalTo: scrollView.widthAnchor),
            
            // Header View
            headerView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 20),
            headerView.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 20),
            headerView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -20),
            headerView.heightAnchor.constraint(equalToConstant: 100),
            
            // Total Balance Label
            totalBalanceLabel.topAnchor.constraint(equalTo: headerView.topAnchor, constant: 20),
            totalBalanceLabel.centerXAnchor.constraint(equalTo: headerView.centerXAnchor),
            
            // Total Balance Value Label
            totalBalanceValueLabel.topAnchor.constraint(equalTo: totalBalanceLabel.bottomAnchor, constant: 8),
            totalBalanceValueLabel.centerXAnchor.constraint(equalTo: headerView.centerXAnchor),
            
            // Table View
            tableView.topAnchor.constraint(equalTo: headerView.bottomAnchor, constant: 20),
            tableView.leadingAnchor.constraint(equalTo: contentView.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor),
            tableView.heightAnchor.constraint(equalToConstant: 300),
            
            // Add Account Button
            addAccountButton.topAnchor.constraint(equalTo: tableView.bottomAnchor, constant: 20),
            addAccountButton.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 20),
            addAccountButton.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -20),
            addAccountButton.heightAnchor.constraint(equalToConstant: 50),
            addAccountButton.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -20)
        ])
    }
    
    private func setupUI() {
        title = "Dashboard"
        view.backgroundColor = UIColor.systemGroupedBackground
        
        // Configure header view
        headerView.backgroundColor = UIColor.systemBackground
        headerView.layer.cornerRadius = 16
        headerView.layer.shadowColor = UIColor.black.cgColor
        headerView.layer.shadowOffset = CGSize(width: 0, height: 2)
        headerView.layer.shadowOpacity = 0.1
        headerView.layer.shadowRadius = 4
        
        // Configure total balance labels
        totalBalanceLabel.text = "Total Balance"
        totalBalanceLabel.font = UIFont.systemFont(ofSize: 16, weight: .medium)
        totalBalanceLabel.textColor = UIColor.secondaryLabel
        
        totalBalanceValueLabel.font = UIFont.systemFont(ofSize: 32, weight: .bold)
        totalBalanceValueLabel.textColor = UIColor.label
        
        // Configure add account button
        addAccountButton.setTitle("+ Add Account", for: .normal)
        addAccountButton.backgroundColor = UIColor.systemBlue
        addAccountButton.setTitleColor(.white, for: .normal)
        addAccountButton.titleLabel?.font = UIFont.systemFont(ofSize: 16, weight: .semibold)
        addAccountButton.layer.cornerRadius = 12
        
        addAccountButton.addTarget(self, action: #selector(addAccountButtonTapped), for: .touchUpInside)
    }
    
    private func setupTableView() {
        tableView.delegate = self
        tableView.dataSource = self
        tableView.backgroundColor = UIColor.clear
        tableView.separatorStyle = .none
        tableView.register(AccountTableViewCell.self, forCellReuseIdentifier: "AccountCell")
        tableView.isScrollEnabled = false
    }
    
    private func loadAccounts() {
        // Simulate loading accounts from Plaid
        // In a real app, this would make an API call
        accounts = [
            Account(id: "1", name: "Chase Checking", balance: 2450.75, type: "checking", mask: "0000"),
            Account(id: "2", name: "Savings Account", balance: 8920.30, type: "savings", mask: "1234"),
            Account(id: "3", name: "Credit Card", balance: -1200.50, type: "credit", mask: "5678")
        ]
        
        updateTotalBalance()
        tableView.reloadData()
        
        // Update table view height based on content
        let contentHeight = CGFloat(accounts.count) * 80
        tableView.constraints.first { $0.firstAttribute == .height }?.constant = contentHeight
    }
    
    private func updateTotalBalance() {
        let total = accounts.reduce(0) { $0 + $1.balance }
        totalBalanceValueLabel.text = String(format: "$%.2f", total)
        totalBalanceValueLabel.textColor = total >= 0 ? UIColor.systemGreen : UIColor.systemRed
    }
    
    @objc private func addAccountButtonTapped() {
        let plaidVC = PlaidLinkViewController()
        navigationController?.pushViewController(plaidVC, animated: true)
    }
}

// MARK: - UITableViewDataSource
extension DashboardViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return accounts.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "AccountCell", for: indexPath) as! AccountTableViewCell
        let account = accounts[indexPath.row]
        cell.configure(with: account)
        return cell
    }
}

// MARK: - UITableViewDelegate
extension DashboardViewController: UITableViewDelegate {
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 80
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        // Handle account selection if needed
    }
}

// MARK: - Custom Account Cell
class AccountTableViewCell: UITableViewCell {
    
    private let containerView = UIView()
    private let accountNameLabel = UILabel()
    private let accountTypeLabel = UILabel()
    private let balanceLabel = UILabel()
    private let maskLabel = UILabel()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setupUI()
    }
    
    private func setupUI() {
        backgroundColor = UIColor.clear
        selectionStyle = .none
        
        // Container view
        containerView.backgroundColor = UIColor.systemBackground
        containerView.layer.cornerRadius = 12
        containerView.layer.shadowColor = UIColor.black.cgColor
        containerView.layer.shadowOffset = CGSize(width: 0, height: 1)
        containerView.layer.shadowOpacity = 0.1
        containerView.layer.shadowRadius = 3
        
        contentView.addSubview(containerView)
        containerView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            containerView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 4),
            containerView.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 16),
            containerView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -16),
            containerView.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -4)
        ])
        
        // Account name label
        accountNameLabel.font = UIFont.systemFont(ofSize: 16, weight: .semibold)
        accountNameLabel.textColor = UIColor.label
        
        // Account type label
        accountTypeLabel.font = UIFont.systemFont(ofSize: 14, weight: .medium)
        accountTypeLabel.textColor = UIColor.secondaryLabel
        
        // Balance label
        balanceLabel.font = UIFont.systemFont(ofSize: 18, weight: .bold)
        balanceLabel.textAlignment = .right
        
        // Mask label
        maskLabel.font = UIFont.systemFont(ofSize: 12, weight: .medium)
        maskLabel.textColor = UIColor.tertiaryLabel
        maskLabel.textAlignment = .right
        
        [accountNameLabel, accountTypeLabel, balanceLabel, maskLabel].forEach {
            containerView.addSubview($0)
            $0.translatesAutoresizingMaskIntoConstraints = false
        }
        
        NSLayoutConstraint.activate([
            accountNameLabel.topAnchor.constraint(equalTo: containerView.topAnchor, constant: 12),
            accountNameLabel.leadingAnchor.constraint(equalTo: containerView.leadingAnchor, constant: 16),
            accountNameLabel.trailingAnchor.constraint(lessThanOrEqualTo: balanceLabel.leadingAnchor, constant: -8),
            
            accountTypeLabel.topAnchor.constraint(equalTo: accountNameLabel.bottomAnchor, constant: 2),
            accountTypeLabel.leadingAnchor.constraint(equalTo: containerView.leadingAnchor, constant: 16),
            accountTypeLabel.bottomAnchor.constraint(equalTo: containerView.bottomAnchor, constant: -12),
            
            balanceLabel.topAnchor.constraint(equalTo: containerView.topAnchor, constant: 12),
            balanceLabel.trailingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: -16),
            
            maskLabel.topAnchor.constraint(equalTo: balanceLabel.bottomAnchor, constant: 2),
            maskLabel.trailingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: -16),
            maskLabel.bottomAnchor.constraint(equalTo: containerView.bottomAnchor, constant: -12)
        ])
    }
    
    func configure(with account: Account) {
        accountNameLabel.text = account.name
        accountTypeLabel.text = account.type.capitalized
        balanceLabel.text = String(format: "$%.2f", account.balance)
        maskLabel.text = "••••\(account.mask)"
        
        balanceLabel.textColor = account.balance >= 0 ? UIColor.systemGreen : UIColor.systemRed
    }
}