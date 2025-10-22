//
//  RulesViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import UIKit

class RulesViewController: UIViewController {
    
    @IBOutlet weak var rulesLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        print("🚀 RulesViewController viewDidLoad - SUCCESS!")
        
        // Set the title for the navigation bar
        self.title = "Flow Rules"
        
        // Update the existing storyboard label
        rulesLabel.text = "Rules Management System"
        rulesLabel.font = UIFont.systemFont(ofSize: 18, weight: .bold)
        rulesLabel.textColor = .systemBlue
        
        print("✅ RulesViewController setup complete")
    }
}