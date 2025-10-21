//
//  ChatViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/21/25.
//

import UIKit

struct ChatMessage {
    let id: String
    let text: String
    let isFromUser: Bool
    let timestamp: Date
}

class ChatViewController: UIViewController {
    
    private let tableView = UITableView()
    private let messageInputView = UIView()
    private let messageTextField = UITextField()
    private let sendButton = UIButton(type: .system)
    private var inputViewBottomConstraint: NSLayoutConstraint!
    
    private var messages: [ChatMessage] = []
    private let assistantResponses = [
        "I can help you manage your money flows and rules!",
        "Would you like me to explain how your current rules work?",
        "I notice you have a savings rule set up. That's great for building an emergency fund!",
        "Consider setting up automatic payments for your credit card to avoid late fees.",
        "Your money flow visualization shows healthy saving patterns.",
        "I can help you optimize your money rules for better financial outcomes."
    ]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViews()
        setupConstraints()
        setupUI()
        setupTableView()
        setupKeyboardObservers()
        loadInitialMessages()
    }
    
    deinit {
        NotificationCenter.default.removeObserver(self)
    }
    
    private func setupViews() {
        view.addSubview(tableView)
        view.addSubview(messageInputView)
        messageInputView.addSubview(messageTextField)
        messageInputView.addSubview(sendButton)
        
        tableView.translatesAutoresizingMaskIntoConstraints = false
        messageInputView.translatesAutoresizingMaskIntoConstraints = false
        messageTextField.translatesAutoresizingMaskIntoConstraints = false
        sendButton.translatesAutoresizingMaskIntoConstraints = false
    }
    
    private func setupConstraints() {
        inputViewBottomConstraint = messageInputView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor)
        
        NSLayoutConstraint.activate([
            // Table View
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.bottomAnchor.constraint(equalTo: messageInputView.topAnchor),
            
            // Message Input View
            messageInputView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            messageInputView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            messageInputView.heightAnchor.constraint(equalToConstant: 80),
            inputViewBottomConstraint,
            
            // Message Text Field
            messageTextField.leadingAnchor.constraint(equalTo: messageInputView.leadingAnchor, constant: 16),
            messageTextField.centerYAnchor.constraint(equalTo: messageInputView.centerYAnchor),
            messageTextField.trailingAnchor.constraint(equalTo: sendButton.leadingAnchor, constant: -12),
            messageTextField.heightAnchor.constraint(equalToConstant: 40),
            
            // Send Button
            sendButton.trailingAnchor.constraint(equalTo: messageInputView.trailingAnchor, constant: -16),
            sendButton.centerYAnchor.constraint(equalTo: messageInputView.centerYAnchor),
            sendButton.widthAnchor.constraint(equalToConstant: 60),
            sendButton.heightAnchor.constraint(equalToConstant: 40)
        ])
    }
    
    private func setupUI() {
        title = "Financial Assistant"
        view.backgroundColor = UIColor.systemGroupedBackground
        
        // Configure input view
        messageInputView.backgroundColor = UIColor.systemBackground
        messageInputView.layer.borderColor = UIColor.separator.cgColor
        messageInputView.layer.borderWidth = 0.5
        
        // Configure text field
        messageTextField.placeholder = "Ask about your finances..."
        messageTextField.borderStyle = .roundedRect
        messageTextField.delegate = self
        
        // Configure send button
        sendButton.setTitle("Send", for: .normal)
        sendButton.backgroundColor = UIColor.systemBlue
        sendButton.setTitleColor(.white, for: .normal)
        sendButton.titleLabel?.font = UIFont.systemFont(ofSize: 16, weight: .semibold)
        sendButton.layer.cornerRadius = 8
        sendButton.isEnabled = false
        
        sendButton.addTarget(self, action: #selector(sendButtonTapped), for: .touchUpInside)
    }
    
    private func setupTableView() {
        tableView.delegate = self
        tableView.dataSource = self
        tableView.backgroundColor = UIColor.clear
        tableView.separatorStyle = .none
        tableView.register(ChatMessageTableViewCell.self, forCellReuseIdentifier: "ChatMessageCell")
        tableView.contentInset = UIEdgeInsets(top: 16, left: 0, bottom: 16, right: 0)
    }
    
    private func setupKeyboardObservers() {
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(keyboardWillShow),
            name: UIResponder.keyboardWillShowNotification,
            object: nil
        )
        
        NotificationCenter.default.addObserver(
            self,
            selector: #selector(keyboardWillHide),
            name: UIResponder.keyboardWillHideNotification,
            object: nil
        )
    }
    
    private func loadInitialMessages() {
        let welcomeMessage = ChatMessage(
            id: UUID().uuidString,
            text: "Hello! I'm your financial assistant. I can help you understand your money flows, manage rules, and answer questions about your accounts. How can I help you today?",
            isFromUser: false,
            timestamp: Date()
        )
        
        messages.append(welcomeMessage)
        tableView.reloadData()
    }
    
    @objc private func keyboardWillShow(notification: NSNotification) {
        guard let keyboardFrame = notification.userInfo?[UIResponder.keyboardFrameEndUserInfoKey] as? CGRect else { return }
        
        inputViewBottomConstraint.constant = -keyboardFrame.height + view.safeAreaInsets.bottom
        
        UIView.animate(withDuration: 0.3) {
            self.view.layoutIfNeeded()
        }
    }
    
    @objc private func keyboardWillHide(notification: NSNotification) {
        inputViewBottomConstraint.constant = 0
        
        UIView.animate(withDuration: 0.3) {
            self.view.layoutIfNeeded()
        }
    }
    
    @objc private func sendButtonTapped() {
        sendMessage()
    }
    
    private func sendMessage() {
        guard let messageText = messageTextField.text, !messageText.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty else {
            return
        }
        
        // Add user message
        let userMessage = ChatMessage(
            id: UUID().uuidString,
            text: messageText,
            isFromUser: true,
            timestamp: Date()
        )
        
        messages.append(userMessage)
        messageTextField.text = ""
        sendButton.isEnabled = false
        
        // Reload table and scroll to bottom
        tableView.reloadData()
        scrollToBottom()
        
        // Simulate assistant response after a delay
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
            self.addAssistantResponse()
        }
    }
    
    private func addAssistantResponse() {
        let randomResponse = assistantResponses.randomElement() ?? "I'm here to help!"
        
        let assistantMessage = ChatMessage(
            id: UUID().uuidString,
            text: randomResponse,
            isFromUser: false,
            timestamp: Date()
        )
        
        messages.append(assistantMessage)
        tableView.reloadData()
        scrollToBottom()
    }
    
    private func scrollToBottom() {
        guard !messages.isEmpty else { return }
        
        let indexPath = IndexPath(row: messages.count - 1, section: 0)
        tableView.scrollToRow(at: indexPath, at: .bottom, animated: true)
    }
}

// MARK: - UITextFieldDelegate
extension ChatViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        let newText = (textField.text as NSString?)?.replacingCharacters(in: range, with: string) ?? string
        sendButton.isEnabled = !newText.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
        return true
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        sendMessage()
        return true
    }
}

// MARK: - UITableViewDataSource
extension ChatViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return messages.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ChatMessageCell", for: indexPath) as! ChatMessageTableViewCell
        let message = messages[indexPath.row]
        cell.configure(with: message)
        return cell
    }
}

// MARK: - UITableViewDelegate
extension ChatViewController: UITableViewDelegate {
    func tableView(_ tableView: UITableView, estimatedHeightForRowAt indexPath: IndexPath) -> CGFloat {
        return 60
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return UITableView.automaticDimension
    }
}

// MARK: - Custom Chat Message Cell
class ChatMessageTableViewCell: UITableViewCell {
    
    private let messageContainerView = UIView()
    private let messageLabel = UILabel()
    private let timestampLabel = UILabel()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        setupUI()
    }
    
    private func setupUI() {
        backgroundColor = UIColor.clear
        selectionStyle = .none
        
        // Configure message container
        messageContainerView.layer.cornerRadius = 16
        messageContainerView.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner, .layerMinXMaxYCorner]
        
        // Configure message label
        messageLabel.numberOfLines = 0
        messageLabel.font = UIFont.systemFont(ofSize: 16, weight: .medium)
        
        // Configure timestamp label
        timestampLabel.font = UIFont.systemFont(ofSize: 12, weight: .medium)
        timestampLabel.textColor = UIColor.tertiaryLabel
        
        contentView.addSubview(messageContainerView)
        messageContainerView.addSubview(messageLabel)
        contentView.addSubview(timestampLabel)
        
        messageContainerView.translatesAutoresizingMaskIntoConstraints = false
        messageLabel.translatesAutoresizingMaskIntoConstraints = false
        timestampLabel.translatesAutoresizingMaskIntoConstraints = false
    }
    
    func configure(with message: ChatMessage) {
        messageLabel.text = message.text
        
        let formatter = DateFormatter()
        formatter.timeStyle = .short
        timestampLabel.text = formatter.string(from: message.timestamp)
        
        // Clear existing constraints
        messageContainerView.constraints.forEach { messageContainerView.removeConstraint($0) }
        contentView.constraints.forEach { constraint in
            if constraint.firstItem === messageContainerView || constraint.secondItem === messageContainerView ||
               constraint.firstItem === timestampLabel || constraint.secondItem === timestampLabel {
                contentView.removeConstraint(constraint)
            }
        }
        
        if message.isFromUser {
            // User message (right side)
            messageContainerView.backgroundColor = UIColor.systemBlue
            messageLabel.textColor = UIColor.white
            messageContainerView.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner, .layerMinXMaxYCorner]
            
            NSLayoutConstraint.activate([
                messageContainerView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 8),
                messageContainerView.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -16),
                messageContainerView.leadingAnchor.constraint(greaterThanOrEqualTo: contentView.leadingAnchor, constant: 80),
                messageContainerView.bottomAnchor.constraint(equalTo: timestampLabel.topAnchor, constant: -4),
                
                timestampLabel.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -16),
                timestampLabel.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -8)
            ])
        } else {
            // Assistant message (left side)
            messageContainerView.backgroundColor = UIColor.systemGray5
            messageLabel.textColor = UIColor.label
            messageContainerView.layer.maskedCorners = [.layerMinXMinYCorner, .layerMaxXMinYCorner, .layerMaxXMaxYCorner]
            
            NSLayoutConstraint.activate([
                messageContainerView.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 8),
                messageContainerView.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 16),
                messageContainerView.trailingAnchor.constraint(lessThanOrEqualTo: contentView.trailingAnchor, constant: -80),
                messageContainerView.bottomAnchor.constraint(equalTo: timestampLabel.topAnchor, constant: -4),
                
                timestampLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 16),
                timestampLabel.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -8)
            ])
        }
        
        NSLayoutConstraint.activate([
            messageLabel.topAnchor.constraint(equalTo: messageContainerView.topAnchor, constant: 12),
            messageLabel.leadingAnchor.constraint(equalTo: messageContainerView.leadingAnchor, constant: 16),
            messageLabel.trailingAnchor.constraint(equalTo: messageContainerView.trailingAnchor, constant: -16),
            messageLabel.bottomAnchor.constraint(equalTo: messageContainerView.bottomAnchor, constant: -12)
        ])
    }
}