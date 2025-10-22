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
        
        // Set the title for the navigation bar
        self.title = "Flow Rules"
        
        // Set the tab bar item
        self.tabBarItem = UITabBarItem(title: "Rules", image: UIImage(systemName: "list.bullet.rectangle"), tag: 1)
        
        setupBasicUI()
    }
    
    private func setupBasicUI() {
        // Add subtitle label
        let subtitleLabel = UILabel()
        subtitleLabel.text = "Automate your money transfers"
        subtitleLabel.font = UIFont.systemFont(ofSize: 16)
        subtitleLabel.textColor = .systemGray
        subtitleLabel.textAlignment = .center
        subtitleLabel.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(subtitleLabel)
        
        NSLayoutConstraint.activate([
            subtitleLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16),
            subtitleLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            subtitleLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20)
        ])
    }
}