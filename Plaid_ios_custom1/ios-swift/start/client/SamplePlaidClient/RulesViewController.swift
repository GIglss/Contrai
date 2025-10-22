//
//  RulesViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import UIKit

class RulesViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        print("🚀 RulesViewController viewDidLoad - SUCCESS!")
        
        // Set the title for the navigation bar
        self.title = "Flow Rules"
        
        // Set the tab bar item
        self.tabBarItem = UITabBarItem(title: "Rules", image: UIImage(systemName: "list.bullet.rectangle"), tag: 1)
        
        // Add simple test label to make sure it's working
        let testLabel = UILabel()
        testLabel.text = "Custom RulesViewController Working!"
        testLabel.font = UIFont.systemFont(ofSize: 18, weight: .bold)
        testLabel.textColor = .systemBlue
        testLabel.textAlignment = .center
        testLabel.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(testLabel)
        
        NSLayoutConstraint.activate([
            testLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            testLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
        
        print("✅ RulesViewController setup complete")
    }
}