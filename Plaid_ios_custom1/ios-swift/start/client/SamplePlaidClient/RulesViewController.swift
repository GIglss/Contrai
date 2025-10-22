//
//  RulesViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import UIKit

class RulesViewController: UIViewController {
     
    //@IBOutlet weak var rulesLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        print("🚀 RulesViewController viewDidLoad called")
        
        // Set the title for the navigation bar
        self.title = "Flow Rules"
        
        // Set the tab bar item
        self.tabBarItem = UITabBarItem(title: "Rules", image: UIImage(systemName: "list.bullet.rectangle"), tag: 1)
        
        setupBasicUI()
        
        print("🏁 RulesViewController viewDidLoad finished")
    }
    
    private func setupBasicUI() {
        print("🎨 Setting up basic UI for Rules")
        
        // Add subtitle label
        let subtitleLabel = UILabel()
        subtitleLabel.text = "Automate your money transfers"
        subtitleLabel.font = UIFont.systemFont(ofSize: 16)
        subtitleLabel.textColor = .systemGray
        subtitleLabel.textAlignment = .center
        subtitleLabel.backgroundColor = .systemYellow // Temporary to make it visible
        subtitleLabel.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(subtitleLabel)
        
        // Add a temporary test label to make sure our code is running
        let testLabel = UILabel()
        testLabel.text = "TEST: Rules View Loaded"
        testLabel.font = UIFont.systemFont(ofSize: 20, weight: .bold)
        testLabel.textColor = .systemBlue
        testLabel.textAlignment = .center
        testLabel.backgroundColor = .systemGray6
        testLabel.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(testLabel)
        
        NSLayoutConstraint.activate([
            // Subtitle
            subtitleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16),
            subtitleLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            subtitleLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            subtitleLabel.heightAnchor.constraint(equalToConstant: 40),
            
            // Test label
            testLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            testLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            testLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            testLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            testLabel.heightAnchor.constraint(equalToConstant: 50)
        ])
        
        print("✅ Basic UI setup complete")
    }
}