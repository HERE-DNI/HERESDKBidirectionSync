---
title: "EVSEInfo Structure Reference"
slug: "sdk-for-ios-explore-structs-evseinfo"
---

# EVSEInfo

<div class="declaration">

<div class="language">

``` highlight
public struct EVSEInfo : Hashable
```

</div>

</div>

Represents an EVSE at the charging point. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV3uidSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-uid" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV3uidSSvp" class="token"><code>uid</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Uniquely identifies the EVSE within the CPOs platform (and suboperator platforms). For example a database ID or the actual “EVSE ID”. This field can never be changed, modified or renamed. This is the ‘technical’ identification of the EVSE, not to be used as ‘human readable’ identification, use the field <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV2idSSSgvp">`EVSEInfo.id`</a> for that.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var uid: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV2idSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV2idSSSgvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Human-readable globally unique identifier for the EVSE.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV6evseIDSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-evseID" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV6evseIDSSSgvp" class="token"><code>evseID</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier compliant with the EVSE ID from eMI3 standard version V1.0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evseID: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV6statusAA9EVSEStateOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-status" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV6statusAA9EVSEStateOvp" class="token"><code>status</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Status of the EVSE.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var status: EVSEState
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-evsestate">EVSEState</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV11lastUpdated10Foundation4DateVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastUpdated" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV11lastUpdated10Foundation4DateVvp" class="token"><code>lastUpdated</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Timestamp when the status of this EVSE was last updated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastUpdated: Date
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV10connectorsSayAA19EVChargingConnectorVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-connectors" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV10connectorsSayAA19EVChargingConnectorVGvp" class="token"><code>connectors</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of available connectors on the EVSE. An operational EVSE should have at least one connector.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectors: [EVChargingConnector]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evchargingconnector">EVChargingConnector</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV12capabilitiesSayAA14EVSECapabilityOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-capabilities" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV12capabilitiesSayAA14EVSECapabilityOGvp" class="token"><code>capabilities</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Capabilities of the EVSE.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var capabilities: [EVSECapability]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-evsecapability">EVSECapability</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV10floorLevelSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-floorLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV10floorLevelSSSgvp" class="token"><code>floorLevel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Floor level on which the EVSE is located.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var floorLevel: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV17physicalReferenceSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-physicalReference" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV17physicalReferenceSSSgvp" class="token"><code>physicalReference</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A number or string printed on the outside of the EVSE for visual identification.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var physicalReference: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV11coordinatesAA14GeoCoordinatesVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV11coordinatesAA14GeoCoordinatesVSgvp" class="token"><code>coordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the EVSE.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV15paymentSupportsSayAA18EVSEPaymentSupportOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-paymentSupports" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV15paymentSupportsSayAA18EVSEPaymentSupportOGvp" class="token"><code>paymentSupports</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of payment support functionalities on EVSE for ad-hoc customers (without pre-registration).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var paymentSupports: [EVSEPaymentSupport]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-evsepaymentsupport">EVSEPaymentSupport</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8EVSEInfoV3uid2id6evseID6status11lastUpdated10connectors12capabilities10floorLevel17physicalReference11coordinates15paymentSupportsACSS_SSSgAoA9EVSEStateO10Foundation4DateVSayAA19EVChargingConnectorVGSayAA14EVSECapabilityOGA2oA14GeoCoordinatesVSgSayAA18EVSEPaymentSupportOGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-uid-id-evseID-status-lastUpdated-connectors-capabilities-floorLevel-physicalReference-coordinates-paymentSupports" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evseinfo#sdk-for-ios-explore-s-7heresdk8EVSEInfoV3uid2id6evseID6status11lastUpdated10connectors12capabilities10floorLevel17physicalReference11coordinates15paymentSupportsACSS_SSSgAoA9EVSEStateO10Foundation4DateVSayAA19EVChargingConnectorVGSayAA14EVSECapabilityOGA2oA14GeoCoordinatesVSgSayAA18EVSEPaymentSupportOGtcfc" class="token"><code>init(uid:</code><wbr></wbr><code>id:</code><wbr></wbr><code>evseID:</code><wbr></wbr><code>status:</code><wbr></wbr><code>lastUpdated:</code><wbr></wbr><code>connectors:</code><wbr></wbr><code>capabilities:</code><wbr></wbr><code>floorLevel:</code><wbr></wbr><code>physicalReference:</code><wbr></wbr><code>coordinates:</code><wbr></wbr><code>paymentSupports:</code><wbr></wbr><code>)</code></a> 

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
  public init(uid: String = "", id: String? = nil, evseID: String? = nil, status: EVSEState = EVSEState.unknown, lastUpdated: Date = Date(timeIntervalSince1970: 0), connectors: [EVChargingConnector] = [], capabilities: [EVSECapability] = [], floorLevel: String? = nil, physicalReference: String? = nil, coordinates: GeoCoordinates? = nil, paymentSupports: [EVSEPaymentSupport] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-evsestate">EVSEState</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnector">EVChargingConnector</a>
  - <a href="sdk-for-ios-explore-enums-evsecapability">EVSECapability</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-enums-evsepaymentsupport">EVSEPaymentSupport</a>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

