//
//  PlaidLinkViewController.swift
//  SamplePlaidClients
//
//  Created by Todd Kerpelman on 8/18/23.
//

import UIKit
import LinkKit

class PlaidLinkViewController: UIViewController {
    private let startLinkButton = UIButton(type: .system)
    let communicator = ServerCommunicator()
    var linkToken: String?
    var handler: Handler?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViews()
        setupConstraints()
        setupUI()
        self.startLinkButton.isEnabled = false
        fetchLinkToken()
    }
    
    private func setupViews() {
        view.addSubview(startLinkButton)
        startLinkButton.translatesAutoresizingMaskIntoConstraints = false
    }
    
    private func setupConstraints() {
        NSLayoutConstraint.activate([
            startLinkButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            startLinkButton.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            startLinkButton.leadingAnchor.constraint(greaterThanOrEqualTo: view.leadingAnchor, constant: 50),
            startLinkButton.trailingAnchor.constraint(lessThanOrEqualTo: view.trailingAnchor, constant: -50),
            startLinkButton.heightAnchor.constraint(equalToConstant: 50)
        ])
    }
    
    private func setupUI() {
        view.backgroundColor = UIColor.systemBackground
        
        startLinkButton.setTitle("Connect Bank Account", for: .normal)
        startLinkButton.backgroundColor = UIColor.systemBlue
        startLinkButton.setTitleColor(.white, for: .normal)
        startLinkButton.titleLabel?.font = UIFont.systemFont(ofSize: 18, weight: .semibold)
        startLinkButton.layer.cornerRadius = 12
        
        startLinkButton.addTarget(self, action: #selector(startLinkWasPressed), for: .touchUpInside)
    }
    
    private func createLinkConfiguration(linkToken: String) -> Any? {
        // Create our link configuration object
        // This return type will be a LinkTokenConfiguration object
        var linkTokenConfig = LinkTokenConfiguration(token: linkToken) { success  in
                    print("Link was finished successfully! \(success)")
                    self.exchangePublicTokenForAccessToken(success.publicToken)
                }
                linkTokenConfig.onExit = { linkEvent in
                    print("User exited link early. \(linkEvent)")
                }
                linkTokenConfig.onEvent = { linkExit in
                    print("Hit an event \(linkExit.eventName)")
                }
                return linkTokenConfig
    }
    
    @objc private func startLinkWasPressed() {
        // Handle the button being clicked
        guard let linkToken = linkToken else { return }
        let config = createLinkConfiguration(linkToken: linkToken)
        
        let creationResult = Plaid.create(config as! LinkTokenConfiguration)
        switch creationResult {
        case .success(let handler):
            self.handler = handler
            handler.open(presentUsing: .viewController(self))
        case .failure(let error):
            print("Handler creation error\(error)")
        }
    }
    
    private func exchangePublicTokenForAccessToken(_ publicToken: String) {
        // Exchange our public token for an access token
        self.communicator.callMyServer(path: "/server/swap_public_token", httpMethod: .post, params: ["public_token": publicToken]) { (result: Result<SwapPublicTokenResponse, ServerCommunicator.Error>) in
                    switch result {
                    case .success(let response):
                        if response.success {
                            self.navigationController?.popViewController(animated: true)
                        } else {
                            print ("Got a failed success \(response)")
                        }
                    case .failure(let error):
                        print ("Got an error \(error)")
                    }
                }
    }
    
    
    private func fetchLinkToken() {
        // Fetch a link token from our server
        self.communicator.callMyServer(path: "/server/generate_link_token", httpMethod: .post) { (result: Result<LinkTokenCreateResponse, ServerCommunicator.Error>) in
            switch result {
            case .success(let response):
                self.linkToken = response.linkToken
                self.startLinkButton.isEnabled = true
            case .failure(let error):
                print(error)
            }
        }

    }
}
