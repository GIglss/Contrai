//
//  UserStatus.swift
//  SamplePlaidClient
//
//  Created by Dave Troupe on 8/30/23.
//

import Foundation

enum UserConnectionStatus: String, Codable {
    case connected
    case disconnected
}

struct UserStatusResponse: Codable {
    let userStatus: UserConnectionStatus
    let userId: String
}

 struct LinkTokenCreateResponse: Codable {
    let linkToken: String
    let expiration: String
}
 
struct SwapPublicTokenResponse: Codable {
    let success: Bool
}

struct SimpleAuthResponse: Codable{
    let accountName: String
    let accountMask: String
    let routingNumber: String
}

// New response models for enhanced account data
struct AccountBalance: Codable {
    let available: Double?
    let current: Double?
    let limit: Double?
    let iso_currency_code: String?
}

struct PlaidAccount: Codable {
    let account_id: String
    let name: String
    let official_name: String?
    let type: String
    let subtype: String?
    let mask: String?
    let balances: AccountBalance?
}

struct AccountsResponse: Codable {
    let accounts: [PlaidAccount]
    let request_id: String
}

struct BalanceResponse: Codable {
    let accounts: [PlaidAccount]
    let request_id: String
}
 
