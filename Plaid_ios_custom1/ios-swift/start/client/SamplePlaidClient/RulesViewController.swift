//
//  RulesViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import UIKit

class RulesViewController: UIViewController {
    
    @IBOutlet weak var rulesTableView: UITableView!
    
    private var rules: [FlowRule] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        print("🚀 RulesViewController viewDidLoad - SUCCESS!")
        
        // Set the title for the navigation bar
        self.title = "Flow Rules"
        
        // Add "+" button to navigation bar
        setupNavigationBar()
        
        // Setup table view
        setupTableView()
        
        // Load mock rules for now
        loadMockRules()
        
        print("✅ RulesViewController setup complete")
    }
    
    private func setupNavigationBar() {
        let addButton = UIBarButtonItem(
            barButtonSystemItem: .add,
            target: self,
            action: #selector(addNewRule)
        )
        navigationItem.rightBarButtonItem = addButton
    }
    
    @objc private func addNewRule() {
        print("📝 Add new rule tapped")
        
        // For now, show a simple alert
        let alert = UIAlertController(
            title: "Create New Rule",
            message: "Enter rule details:",
            preferredStyle: .alert
        )
        
        alert.addTextField { textField in
            textField.placeholder = "Rule name"
        }
        
        alert.addTextField { textField in
            textField.placeholder = "Rule description"
        }
        
        let createAction = UIAlertAction(title: "Create", style: .default) { [weak self] _ in
            guard let nameField = alert.textFields?[0],
                  let descField = alert.textFields?[1],
                  let name = nameField.text, !name.isEmpty,
                  let description = descField.text, !description.isEmpty else {
                return
            }
            
            self?.createNewRule(name: name, description: description)
        }
        
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel)
        
        alert.addAction(createAction)
        alert.addAction(cancelAction)
        
        present(alert, animated: true)
    }
    
    private func createNewRule(name: String, description: String) {
        let newRule = FlowRule(
            id: UUID().uuidString,
            name: name,
            description: description,
            isActive: true,
            createdDate: DateFormatter.localizedString(from: Date(), dateStyle: .short, timeStyle: .none),
            triggers: ["manual"],
            actions: ["custom"]
        )
        
        rules.append(newRule)
        
        let indexPath = IndexPath(row: rules.count - 1, section: 0)
        rulesTableView.insertRows(at: [indexPath], with: .automatic)
        
        print("✅ Created new rule: \(name)")
    }
    
    private func setupTableView() {
        rulesTableView.delegate = self
        rulesTableView.dataSource = self
    }
    
    private func loadMockRules() {
        // Create some mock rules for testing
        rules = [
            FlowRule(
                id: "1",
                name: "Auto Save",
                description: "Automatically save 10% of incoming transfers",
                isActive: true,
                createdDate: "2025-10-20",
                triggers: ["incoming_transfer"],
                actions: ["save_percentage"]
            ),
            FlowRule(
                id: "2", 
                name: "Bill Payment",
                description: "Pay bills when balance exceeds $1000",
                isActive: false,
                createdDate: "2025-10-19", 
                triggers: ["balance_threshold"],
                actions: ["pay_bills"]
            ),
            FlowRule(
                id: "3",
                name: "Investment Transfer",
                description: "Move surplus to investment account monthly",
                isActive: true,
                createdDate: "2025-10-18",
                triggers: ["monthly_schedule"],
                actions: ["transfer_investment"]
            )
        ]
        
        rulesTableView.reloadData()
    }
}

// MARK: - UITableViewDataSource
extension RulesViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return rules.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "RuleCell", for: indexPath)
        let rule = rules[indexPath.row]
        
        cell.textLabel?.text = rule.name
        cell.detailTextLabel?.text = rule.description
        
        // Show status with color
        if rule.isActive {
            cell.accessoryType = .checkmark
            cell.textLabel?.textColor = .systemBlue
        } else {
            cell.accessoryType = .none
            cell.textLabel?.textColor = .systemGray
        }
        
        return cell
    }
}

// MARK: - UITableViewDelegate
extension RulesViewController: UITableViewDelegate {
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        
        let rule = rules[indexPath.row]
        print("Selected rule: \(rule.name)")
        
        // TODO: Show rule details or edit screen
    }
}