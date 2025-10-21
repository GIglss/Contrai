//
//  MainTabBarController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/21/25.
//

import UIKit

class MainTabBarController: UITabBarController {
    
    private var chatToggleButton: UIButton!
    private var isChatVisible = false
    private var chatViewController: ChatViewController?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViewControllers()
        setupChatToggle()
        customizeTabBarAppearance()
    }
    
    private func setupViewControllers() {
        // Dashboard
        let dashboardVC = DashboardViewController()
        dashboardVC.tabBarItem = UITabBarItem(title: "Dashboard", image: UIImage(systemName: "house"), tag: 0)
        let dashboardNav = UINavigationController(rootViewController: dashboardVC)
        
        // Rules
        let rulesVC = RulesViewController()
        rulesVC.tabBarItem = UITabBarItem(title: "Rules", image: UIImage(systemName: "gear"), tag: 1)
        let rulesNav = UINavigationController(rootViewController: rulesVC)
        
        // Flow Visualization
        let flowVC = FlowVisualizationViewController()
        flowVC.tabBarItem = UITabBarItem(title: "Flows", image: UIImage(systemName: "arrow.triangle.branch"), tag: 2)
        let flowNav = UINavigationController(rootViewController: flowVC)
        
        // Settings (Add Account)
        let settingsVC = PlaidLinkViewController()
        settingsVC.title = "Add Account"
        settingsVC.tabBarItem = UITabBarItem(title: "Settings", image: UIImage(systemName: "plus.circle"), tag: 3)
        let settingsNav = UINavigationController(rootViewController: settingsVC)
        
        viewControllers = [dashboardNav, rulesNav, flowNav, settingsNav]
    }
    
    private func setupChatToggle() {
        chatToggleButton = UIButton(type: .custom)
        chatToggleButton.setImage(UIImage(systemName: "message.circle.fill"), for: .normal)
        chatToggleButton.backgroundColor = UIColor.systemBlue
        chatToggleButton.tintColor = .white
        chatToggleButton.layer.cornerRadius = 25
        chatToggleButton.layer.shadowColor = UIColor.black.cgColor
        chatToggleButton.layer.shadowOffset = CGSize(width: 0, height: 2)
        chatToggleButton.layer.shadowOpacity = 0.3
        chatToggleButton.layer.shadowRadius = 4
        
        chatToggleButton.addTarget(self, action: #selector(chatToggleButtonTapped), for: .touchUpInside)
        
        view.addSubview(chatToggleButton)
        chatToggleButton.translatesAutoresizingMaskIntoConstraints = false
        
        NSLayoutConstraint.activate([
            chatToggleButton.widthAnchor.constraint(equalToConstant: 50),
            chatToggleButton.heightAnchor.constraint(equalToConstant: 50),
            chatToggleButton.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -20),
            chatToggleButton.bottomAnchor.constraint(equalTo: tabBar.topAnchor, constant: -20)
        ])
    }
    
    private func customizeTabBarAppearance() {
        tabBar.backgroundColor = UIColor.systemBackground
        tabBar.tintColor = UIColor.systemBlue
        tabBar.unselectedItemTintColor = UIColor.systemGray
        
        if #available(iOS 15.0, *) {
            let appearance = UITabBarAppearance()
            appearance.configureWithOpaqueBackground()
            appearance.backgroundColor = UIColor.systemBackground
            
            tabBar.standardAppearance = appearance
            tabBar.scrollEdgeAppearance = appearance
        }
    }
    
    @objc private func chatToggleButtonTapped() {
        if isChatVisible {
            dismissChat()
        } else {
            presentChat()
        }
    }
    
    private func presentChat() {
        if chatViewController == nil {
            chatViewController = ChatViewController()
        }
        
        guard let chatVC = chatViewController else { return }
        
        let navController = UINavigationController(rootViewController: chatVC)
        navController.modalPresentationStyle = .pageSheet
        
        if #available(iOS 15.0, *) {
            if let sheet = navController.sheetPresentationController {
                sheet.detents = [.medium(), .large()]
                sheet.prefersGrabberVisible = true
            }
        }
        
        // Add close button to chat
        chatVC.navigationItem.rightBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .done,
            target: self,
            action: #selector(dismissChat)
        )
        
        present(navController, animated: true) {
            self.isChatVisible = true
            self.updateChatToggleButton()
        }
    }
    
    @objc private func dismissChat() {
        dismiss(animated: true) {
            self.isChatVisible = false
            self.updateChatToggleButton()
        }
    }
    
    private func updateChatToggleButton() {
        let imageName = isChatVisible ? "xmark.circle.fill" : "message.circle.fill"
        chatToggleButton.setImage(UIImage(systemName: imageName), for: .normal)
        
        UIView.animate(withDuration: 0.3) {
            self.chatToggleButton.transform = self.isChatVisible ? 
                CGAffineTransform(rotationAngle: .pi) : CGAffineTransform.identity
        }
    }
}