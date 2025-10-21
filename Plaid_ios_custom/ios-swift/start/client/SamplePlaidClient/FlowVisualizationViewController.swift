//
//  FlowVisualizationViewController.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/21/25.
//

import UIKit

struct FlowConnection {
    let fromAccount: String
    let toAccount: String
    let amount: Double
    let isActive: Bool
}

class FlowVisualizationViewController: UIViewController {
    
    private let scrollView = UIScrollView()
    private let contentView = UIView()
    private let refreshButton = UIButton(type: .system)
    
    private var accountViews: [String: UIView] = [:]
    private var flowConnections: [FlowConnection] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupViews()
        setupConstraints()
        setupUI()
        createFlowVisualization()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        updateFlowVisualization()
    }
    
    private func setupViews() {
        view.addSubview(scrollView)
        scrollView.addSubview(contentView)
        view.addSubview(refreshButton)
        
        scrollView.translatesAutoresizingMaskIntoConstraints = false
        contentView.translatesAutoresizingMaskIntoConstraints = false
        refreshButton.translatesAutoresizingMaskIntoConstraints = false
    }
    
    private func setupConstraints() {
        NSLayoutConstraint.activate([
            // Refresh Button
            refreshButton.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 10),
            refreshButton.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            refreshButton.widthAnchor.constraint(equalToConstant: 80),
            refreshButton.heightAnchor.constraint(equalToConstant: 35),
            
            // ScrollView
            scrollView.topAnchor.constraint(equalTo: refreshButton.bottomAnchor, constant: 10),
            scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            scrollView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            
            // Content View
            contentView.topAnchor.constraint(equalTo: scrollView.topAnchor),
            contentView.leadingAnchor.constraint(equalTo: scrollView.leadingAnchor),
            contentView.trailingAnchor.constraint(equalTo: scrollView.trailingAnchor),
            contentView.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor),
            contentView.widthAnchor.constraint(equalToConstant: 400),
            contentView.heightAnchor.constraint(equalToConstant: 400)
        ])
    }
    
    private func setupUI() {
        title = "Money Flows"
        view.backgroundColor = UIColor.systemGroupedBackground
        
        // Configure refresh button
        refreshButton.setTitle("Refresh", for: .normal)
        refreshButton.backgroundColor = UIColor.systemBlue
        refreshButton.setTitleColor(.white, for: .normal)
        refreshButton.titleLabel?.font = UIFont.systemFont(ofSize: 14, weight: .semibold)
        refreshButton.layer.cornerRadius = 6
        
        refreshButton.addTarget(self, action: #selector(refreshButtonTapped), for: .touchUpInside)
        
        scrollView.backgroundColor = UIColor.clear
        contentView.backgroundColor = UIColor.clear
    }
    
    private func createFlowVisualization() {
        // Sample flow data
        flowConnections = [
            FlowConnection(fromAccount: "Chase Checking", toAccount: "Savings Account", amount: 245.00, isActive: true),
            FlowConnection(fromAccount: "Chase Checking", toAccount: "Credit Card", amount: 150.00, isActive: true),
            FlowConnection(fromAccount: "Savings Account", toAccount: "Investment Account", amount: 500.00, isActive: false)
        ]
        
        // Clear existing views
        contentView.subviews.forEach { $0.removeFromSuperview() }
        accountViews.removeAll()
        
        // Create account nodes
        createAccountNodes()
        
        // Draw flow connections
        drawFlowConnections()
    }
    
    private func createAccountNodes() {
        let accounts = ["Chase Checking", "Savings Account", "Credit Card", "Investment Account"]
        let colors: [UIColor] = [.systemBlue, .systemGreen, .systemRed, .systemPurple]
        
        for (index, account) in accounts.enumerated() {
            let accountView = createAccountView(name: account, color: colors[index % colors.count])
            contentView.addSubview(accountView)
            accountViews[account] = accountView
            
            // Position accounts in a circular layout
            let centerX: CGFloat = 200
            let centerY: CGFloat = 200
            let radius: CGFloat = 120
            let angle = (2 * CGFloat.pi / CGFloat(accounts.count)) * CGFloat(index)
            
            let x = centerX + radius * cos(angle) - 40
            let y = centerY + radius * sin(angle) - 40
            
            accountView.frame = CGRect(x: x, y: y, width: 80, height: 80)
        }
        
        // Set content size for scroll view
        scrollView.contentSize = CGSize(width: 400, height: 400)
    }
    
    private func createAccountView(name: String, color: UIColor) -> UIView {
        let view = UIView()
        view.backgroundColor = color.withAlphaComponent(0.8)
        view.layer.cornerRadius = 40
        view.layer.shadowColor = UIColor.black.cgColor
        view.layer.shadowOffset = CGSize(width: 0, height: 2)
        view.layer.shadowOpacity = 0.3
        view.layer.shadowRadius = 4
        
        let label = UILabel()
        label.text = name.components(separatedBy: " ").first ?? name
        label.textAlignment = .center
        label.font = UIFont.systemFont(ofSize: 12, weight: .bold)
        label.textColor = .white
        label.numberOfLines = 2
        label.adjustsFontSizeToFitWidth = true
        
        view.addSubview(label)
        label.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            label.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            label.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            label.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 4),
            label.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -4)
        ])
        
        return view
    }
    
    private func drawFlowConnections() {
        for connection in flowConnections {
            guard let fromView = accountViews[connection.fromAccount],
                  let toView = accountViews[connection.toAccount] else { continue }
            
            let arrowLayer = createArrowLayer(from: fromView, to: toView, connection: connection)
            contentView.layer.addSublayer(arrowLayer)
        }
    }
    
    private func createArrowLayer(from fromView: UIView, to toView: UIView, connection: FlowConnection) -> CAShapeLayer {
        let fromCenter = CGPoint(x: fromView.center.x, y: fromView.center.y)
        let toCenter = CGPoint(x: toView.center.x, y: toView.center.y)
        
        // Calculate arrow path
        let path = UIBezierPath()
        path.move(to: fromCenter)
        path.addLine(to: toCenter)
        
        // Create arrow head
        let angle = atan2(toCenter.y - fromCenter.y, toCenter.x - fromCenter.x)
        let arrowLength: CGFloat = 15
        let arrowAngle: CGFloat = CGFloat.pi / 6
        
        let arrowEnd1 = CGPoint(
            x: toCenter.x - arrowLength * cos(angle - arrowAngle),
            y: toCenter.y - arrowLength * sin(angle - arrowAngle)
        )
        let arrowEnd2 = CGPoint(
            x: toCenter.x - arrowLength * cos(angle + arrowAngle),
            y: toCenter.y - arrowLength * sin(angle + arrowAngle)
        )
        
        path.move(to: toCenter)
        path.addLine(to: arrowEnd1)
        path.move(to: toCenter)
        path.addLine(to: arrowEnd2)
        
        // Create layer
        let shapeLayer = CAShapeLayer()
        shapeLayer.path = path.cgPath
        shapeLayer.strokeColor = connection.isActive ? UIColor.systemGreen.cgColor : UIColor.systemGray.cgColor
        shapeLayer.lineWidth = connection.isActive ? 3.0 : 1.5
        shapeLayer.lineCap = .round
        shapeLayer.lineJoin = .round
        
        if connection.isActive {
            // Add pulsing animation
            let animation = CABasicAnimation(keyPath: "opacity")
            animation.fromValue = 0.4
            animation.toValue = 1.0
            animation.duration = 1.0
            animation.repeatCount = .infinity
            animation.autoreverses = true
            shapeLayer.add(animation, forKey: "pulse")
        }
        
        // Add amount label
        let midPoint = CGPoint(
            x: (fromCenter.x + toCenter.x) / 2,
            y: (fromCenter.y + toCenter.y) / 2
        )
        
        let amountLabel = CATextLayer()
        amountLabel.string = String(format: "$%.0f", connection.amount)
        amountLabel.fontSize = 12
        amountLabel.foregroundColor = UIColor.label.cgColor
        amountLabel.backgroundColor = UIColor.systemBackground.cgColor
        amountLabel.cornerRadius = 8
        amountLabel.frame = CGRect(x: midPoint.x - 25, y: midPoint.y - 10, width: 50, height: 20)
        amountLabel.alignmentMode = .center
        
        contentView.layer.addSublayer(amountLabel)
        
        return shapeLayer
    }
    
    private func updateFlowVisualization() {
        // Remove existing flow layers
        contentView.layer.sublayers?.forEach { layer in
            if layer is CAShapeLayer || layer is CATextLayer {
                layer.removeFromSuperlayer()
            }
        }
        
        // Redraw connections
        drawFlowConnections()
    }
    
    @objc private func refreshButtonTapped() {
        // Animate refresh
        UIView.animate(withDuration: 0.3, animations: {
            self.contentView.transform = CGAffineTransform(scaleX: 0.95, y: 0.95)
        }) { _ in
            UIView.animate(withDuration: 0.3) {
                self.contentView.transform = CGAffineTransform.identity
            }
        }
        
        updateFlowVisualization()
    }
}