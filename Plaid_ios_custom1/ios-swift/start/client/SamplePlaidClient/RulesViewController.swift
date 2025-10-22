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
        
        // Setup table view
        setupTableView()
        
        // Load mock rules for now
        loadMockRules()
        
        print("✅ RulesViewController setup complete")
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