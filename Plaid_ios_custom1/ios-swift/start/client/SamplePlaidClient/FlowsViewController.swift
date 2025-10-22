//
//  FlowsViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import UIKit

class FlowsViewController: UIViewController {
    
    @IBOutlet var flowsLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set the title for the navigation bar
        self.title = "Flows"
        
        // Set the tab bar item
        self.tabBarItem = UITabBarItem(title: "Flows", image: UIImage(systemName: "arrow.triangle.branch"), tag: 2)
    }
}