//
//  SimpleRulesViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import UIKit

class SimpleRulesViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        print("📱 SimpleRulesViewController loaded successfully!")
        
        view.backgroundColor = .systemBackground
        self.title = "Flow Rules"
        
        let label = UILabel()
        label.text = "Simple Rules Controller Works!"
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        
        view.addSubview(label)
        
        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }
}