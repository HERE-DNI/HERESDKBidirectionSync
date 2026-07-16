---
title: "EVChargingOperator Structure Reference"
slug: "sdk-for-ios-navigate-structs-evchargingoperator"
---

# EVChargingOperator

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingOperator : Hashable
```

</div>

</div>

Represents name and optionally other details about operator, suboperator, or e-Mobility service provider. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV4nameSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-name" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingoperator#sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV4nameSSvp" class="token"><code>name</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of the company.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV9partnerIDSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-partnerID" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingoperator#sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV9partnerIDSSvp" class="token"><code>partnerID</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A unique ID for the company.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var partnerID: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV7websiteSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-website" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingoperator#sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV7websiteSSSgvp" class="token"><code>website</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Link to the company’s website, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var website: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV4logoAA9BrandLogoVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-logo" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingoperator#sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV4logoAA9BrandLogoVSgvp" class="token"><code>logo</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Image link to the company’s logo, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var logo: BrandLogo?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-brandlogo">BrandLogo</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV12eMobilityIDsSaySSGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-eMobilityIDs" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingoperator#sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV12eMobilityIDsSaySSGvp" class="token"><code>eMobilityIDs</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  e-Mobility IDs for the company. This list may be empty where map coverage is limited or incomplete.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var eMobilityIDs: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV4name9partnerID7website4logo12eMobilityIDsACSS_S2SSgAA9BrandLogoVSgSaySSGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-name-partnerID-website-logo-eMobilityIDs" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingoperator#sdk-for-ios-navigate-s-7heresdk18EVChargingOperatorV4name9partnerID7website4logo12eMobilityIDsACSS_S2SSgAA9BrandLogoVSgSaySSGtcfc" class="token"><code>init(name:</code><wbr></wbr><code>partnerID:</code><wbr></wbr><code>website:</code><wbr></wbr><code>logo:</code><wbr></wbr><code>eMobilityIDs:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(name: String = "", partnerID: String = "", website: String? = nil, logo: BrandLogo? = nil, eMobilityIDs: [String] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-brandlogo">BrandLogo</a>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

