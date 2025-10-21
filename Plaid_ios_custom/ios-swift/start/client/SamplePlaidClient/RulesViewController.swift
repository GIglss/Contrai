//
//  RulesViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/21/25.
//

import UIKit

struct MoneyRule {
    let id: String
    let name: String
    let description: String
    let fromAccount: String
    let toAccount: String
    let amount: Double
    let frequency: String
    let isActive: Bool
}

class RulesViewController: UIViewController {
    
    private let tableView = UITableView()
    private let addRuleButton = UIButton(type: .system)
    private let emptyStateView = UIView()
    private let emptyStateLabel = UILabel()
    
    private var rules: [MoneyRule] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViews()
        setupConstraints()
        setupUI()
        setupTableView()
        loadRules()
    }
    
    private func setupViews() {
        view.addSubview(tableView)
        view.addSubview(addRuleButton)
        view.addSubview(emptyStateView)
        emptyStateView.addSubview(emptyStateLabel)
        
        tableView.translatesAutoresizingMaskIntoConstraints = false
        addRuleButton.translatesAutoresizingMaskIntoConstraints = false
        emptyStateView.translatesAutoresizingMaskIntoConstraints = false
        emptyStateLabel.translatesAutoresizingMaskIntoConstraints = false
    }
    
    private func setupConstraints() {
        NSLayoutConstraint.activate([
            // Table View
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.bottomAnchor.constraint(equalTo: addRuleButton.topAnchor, constant: -20),
            
            // Add Rule Button
            addRuleButton.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            addRuleButton.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            addRuleButton.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor, constant: -20),
            addRuleButton.heightAnchor.constraint(equalToConstant: 50),
            
            // Empty State View
            emptyStateView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            emptyStateView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            emptyStateView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 40),
            emptyStateView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -40),
            
            // Empty State Label
            emptyStateLabel.centerXAnchor.constraint(equalTo: emptyStateView.centerXAnchor),
            emptyStateLabel.centerYAnchor.constraint(equalTo: emptyStateView.centerYAnchor),
            emptyStateLabel.leadingAnchor.constraint(equalTo: emptyStateView.leadingAnchor),
            emptyStateLabel.trailingAnchor.constraint(equalTo: emptyStateView.trailingAnchor)
        ])
    }
    
    private func setupUI() {
        title = "Money Rules"
        view.backgroundColor = UIColor.systemGroupedBackground
        
        // Configure add rule button
        addRuleButton.setTitle("+ Add Rule", for: .normal)
        addRuleButton.backgroundColor = UIColor.systemBlue
        addRuleButton.setTitleColor(.white, for: .normal)
        addRuleButton.titleLabel?.font = UIFont.systemFont(ofSize: 16, weight: .semibold)
        addRuleButton.layer.cornerRadius = 12
        
        addRuleButton.addTarget(self, action: #selector(addRuleButtonTapped), for: .touchUpInside)
        
        // Configure empty state
        emptyStateLabel.text = "No rules yet!\nCreate your first money flow rule to get started."
        emptyStateLabel.textAlignment = .center
        emptyStateLabel.numberOfLines = 0
        emptyStateLabel.font = UIFont.systemFont(ofSize: 16, weight: .medium)
        emptyStateLabel.textColor = UIColor.secondaryLabel
    }
    
    private func setupTableView() {
        tableView.delegate = self
        tableView.dataSource = self
        tableView.backgroundColor = UIColor.clear
        tableView.separatorStyle = .none
        tableView.register(RuleTableViewCell.self, forCellReuseIdentifier: "RuleCell")
    }
    
    private func loadRules() {
        // Simulate some sample rules
        rules = [
            MoneyRule(id: "1", name: "Emergency Fund", description: "Save 10% of income automatically", fromAccount: "Chase Checking", toAccount: "Savings Account", amount: 245.00, frequency: "Monthly", isActive: true),
            MoneyRule(id: "2", name: "Credit Card Payment", description: "Pay minimum balance automatically", fromAccount: "Chase Checking", toAccount: "Credit Card", amount: 150.00, frequency: "Monthly", isActive: true),
            MoneyRule(id: "3", name: "Investment Transfer", description: "Invest extra funds", fromAccount: "Savings Account", toAccount: "Investment Account", amount: 500.00, frequency: "Quarterly", isActive: false)
        ]
        
        updateEmptyState()
        tableView.reloadData()
    }
    
    private func updateEmptyState() {
        emptyStateView.isHidden = !rules.isEmpty
        tableView.isHidden = rules.isEmpty
    }
    
    @objc private func addRuleButtonTapped() {
        presentAddRuleViewController()
    }
    
    private func presentAddRuleViewController() {
        let alertController = UIAlertController(title: "Add New Rule", message: "Create a new money flow rule", preferredStyle: .alert)
        
        alertController.addTextField { textField in
            textField.placeholder = "Rule Name"
        }
        
        alertController.addTextField { textField in
            textField.placeholder = "Amount ($)"
            textField.keyboardType = .decimalPad
        }
        
        let addAction = UIAlertAction(title: "Add Rule", style: .default) { _ in
            guard let nameField = alertController.textFields?[0],
                  let amountField = alertController.textFields?[1],
                  let name = nameField.text, !name.isEmpty,
                  let amountText = amountField.text, let amount = Double(amountText) else {
                return
            }
            
            let newRule = MoneyRule(
                id: UUID().uuidString,
                name: name,
                description: "Auto-generated rule",
                fromAccount: "Chase Checking",
                toAccount: "Savings Account",
                amount: amount,
                frequency: "Monthly",
                isActive: true
            )
            
            self.rules.append(newRule)
            self.updateEmptyState()
            self.tableView.reloadData()
        }
        
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel)
        
        alertController.addAction(addAction)
        alertController.addAction(cancelAction)
        
        present(alertController, animated: true)
    }
}

// MARK: - UITableViewDataSource
extension RulesViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return rules.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "RuleCell", for: indexPath) as! RuleTableViewCell
        let rule = rules[indexPath.row]
        cell.configure(with: rule)
        cell.delegate = self
        return cell
    }
}

// MARK: - UITableViewDelegate
extension RulesViewController: UITableViewDelegate {
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 100
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
    }
}

// MARK: - RuleTableViewCellDelegate
extension RulesViewController: RuleTableViewCellDelegate {
    func didToggleRule(_ rule: MoneyRule, isActive: Bool) {
        if let index = rules.firstIndex(where: { $0.id == rule.id }) {
            rules[index] = MoneyRule(
                id: rule.id,
                name: rule.name,
                description: rule.description,
                fromAccount: rule.fromAccount,
                toAccount: rule.toAccount,
                amount: rule.amount,
                frequency: rule.frequency,
                isActive: isActive
            )
        }
    }
}

// MARK: - Custom Rule Cell
protocol RuleTableViewCellDelegate: AnyObject {
    func didToggleRule(_ rule: MoneyRule, isActive: Bool)
}

class RuleTableViewCell: UITableViewCell {
    
    weak var delegate: RuleTableViewCellDelegate?
    private var currentRule: MoneyRule?
    
    private let containerView = UIView()
    private let ruleNameLabel = UILabel()
    private let descriptionLabel = UILabel()
    private let amountLabel = UILabel()
    private let frequencyLabel = UILabel()
    private let activeSwitch = UISwitch()
    private let flowArrowLabel = UILabel()
    
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
        
        // Configure labels
        ruleNameLabel.font = UIFont.systemFont(ofSize: 16, weight: .semibold)
        ruleNameLabel.textColor = UIColor.label
        
        descriptionLabel.font = UIFont.systemFont(ofSize: 14, weight: .medium)
        descriptionLabel.textColor = UIColor.secondaryLabel
        descriptionLabel.numberOfLines = 2
        
        amountLabel.font = UIFont.systemFont(ofSize: 18, weight: .bold)
        amountLabel.textColor = UIColor.systemGreen
        
        frequencyLabel.font = UIFont.systemFont(ofSize: 12, weight: .medium)
        frequencyLabel.textColor = UIColor.tertiaryLabel
        
        flowArrowLabel.text = "→"
        flowArrowLabel.font = UIFont.systemFont(ofSize: 16, weight: .bold)
        flowArrowLabel.textColor = UIColor.systemBlue
        
        activeSwitch.onTintColor = UIColor.systemGreen
        activeSwitch.addTarget(self, action: #selector(switchValueChanged), for: .valueChanged)
        
        [ruleNameLabel, descriptionLabel, amountLabel, frequencyLabel, flowArrowLabel, activeSwitch].forEach {
            containerView.addSubview($0)
            $0.translatesAutoresizingMaskIntoConstraints = false
        }
        
        NSLayoutConstraint.activate([
            ruleNameLabel.topAnchor.constraint(equalTo: containerView.topAnchor, constant: 12),
            ruleNameLabel.leadingAnchor.constraint(equalTo: containerView.leadingAnchor, constant: 16),
            ruleNameLabel.trailingAnchor.constraint(lessThanOrEqualTo: activeSwitch.leadingAnchor, constant: -8),
            
            descriptionLabel.topAnchor.constraint(equalTo: ruleNameLabel.bottomAnchor, constant: 4),
            descriptionLabel.leadingAnchor.constraint(equalTo: containerView.leadingAnchor, constant: 16),
            descriptionLabel.trailingAnchor.constraint(lessThanOrEqualTo: amountLabel.leadingAnchor, constant: -8),
            
            amountLabel.centerYAnchor.constraint(equalTo: containerView.centerYAnchor),
            amountLabel.trailingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: -16),
            
            frequencyLabel.topAnchor.constraint(equalTo: amountLabel.bottomAnchor, constant: 2),
            frequencyLabel.trailingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: -16),
            
            activeSwitch.topAnchor.constraint(equalTo: containerView.topAnchor, constant: 12),
            activeSwitch.trailingAnchor.constraint(equalTo: containerView.trailingAnchor, constant: -16)
        ])
    }
    
    @objc private func switchValueChanged() {
        guard let rule = currentRule else { return }
        delegate?.didToggleRule(rule, isActive: activeSwitch.isOn)
        
        UIView.animate(withDuration: 0.3) {
            self.containerView.alpha = self.activeSwitch.isOn ? 1.0 : 0.6
        }
    }
    
    func configure(with rule: MoneyRule) {
        currentRule = rule
        ruleNameLabel.text = rule.name
        descriptionLabel.text = rule.description
        amountLabel.text = String(format: "$%.2f", rule.amount)
        frequencyLabel.text = rule.frequency
        activeSwitch.isOn = rule.isActive
        
        containerView.alpha = rule.isActive ? 1.0 : 0.6
    }
}