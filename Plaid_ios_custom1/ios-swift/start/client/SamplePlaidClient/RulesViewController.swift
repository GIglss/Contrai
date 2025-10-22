//
//  RulesViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import UIKit

class RulesViewController: UIViewController {
    
    @IBOutlet var rulesLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set the title for the navigation bar
        self.title = "Rules"
        
        // Set the tab bar item
        self.tabBarItem = UITabBarItem(title: "Rules", image: UIImage(systemName: "list.bullet.rectangle"), tag: 1)
    }
}