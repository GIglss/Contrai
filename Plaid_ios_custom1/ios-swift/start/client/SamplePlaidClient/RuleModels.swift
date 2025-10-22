//
//  RuleModels.swift
//  SamplePlaidClient
//
//  Created by Assistant on 10/22/25.
//

import Foundation

// MARK: - Flow Rule Data Model
struct FlowRule: Codable {
    let id: String
    let name: String
    let description: String
    let isActive: Bool
    let createdDate: String
    let triggers: [String]
    let actions: [String]
    
    enum CodingKeys: String, CodingKey {
        case id, name, description
        case isActive = "is_active"
        case createdDate = "created_date"
        case triggers, actions
    }
}

// MARK: - Create Rule Request
struct CreateRuleRequest: Codable {
    let name: String
    let description: String
    let triggers: [String]
    let actions: [String]
}

// MARK: - Rules Response
struct RulesResponse: Codable {
    let rules: [FlowRule]
    let status: String
}

// MARK: - Update Rule Status Request
struct UpdateRuleStatusRequest: Codable {
    let ruleId: String
    let isActive: Bool
    
    enum CodingKeys: String, CodingKey {
        case ruleId = "rule_id"
        case isActive = "is_active"
    }
}

// MARK: - Generic API Response
struct APIResponse: Codable {
    let status: String
    let message: String?
}