---
title: "EVChargingConnector Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingconnector"
---

# EVChargingConnector

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingConnector : Hashable
```

</div>

</div>

Represents a connector at the charging point. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV2idSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV2idSSvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of the connector within the EVSE.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV13connectorTypeSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-connectorType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV13connectorTypeSSvp" class="token"><code>connectorType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Standardized type of the connector. Should be one of the constants defined in <a href="sdk-for-ios-explore-structs-evchargingconnectortype">`EVChargingConnectorType`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorType: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV6formatAA0bC6FormatOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-format" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV6formatAA0bC6FormatOvp" class="token"><code>format</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Format of the connector, whether it is a socket or a cable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var format: EVChargingConnectorFormat
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-evchargingconnectorformat">EVChargingConnectorFormat</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV9powerTypeAA05PowerE0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-powerType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV9powerTypeAA05PowerE0Ovp" class="token"><code>powerType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of electrical power used by the connector.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var powerType: PowerType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-powertype">PowerType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV17maxVoltageInVoltss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maxVoltageInVolts" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV17maxVoltageInVoltss5Int32Vvp" class="token"><code>maxVoltageInVolts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max voltage (in volts) of the connector.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxVoltageInVolts: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV19maxCurrentInAmperess5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maxCurrentInAmperes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV19maxCurrentInAmperess5Int32Vvp" class="token"><code>maxCurrentInAmperes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max current (in amperes) of the connector.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxCurrentInAmperes: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV15maxPowerInWattss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maxPowerInWatts" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV15maxPowerInWattss5Int32VSgvp" class="token"><code>maxPowerInWatts</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max power (in watts) of the connector, if available. This should be set when the maximum electric power is lower than the calculated value from voltage and amperage.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxPowerInWatts: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV21termsAndConditionsUrlSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-termsAndConditionsUrl" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV21termsAndConditionsUrlSSSgvp" class="token"><code>termsAndConditionsUrl</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  URL to the operator’s terms and conditions, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var termsAndConditionsUrl: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV13tariffIndexesSays5Int32VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tariffIndexes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV13tariffIndexesSays5Int32VGvp" class="token"><code>tariffIndexes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tariffs for the connector, presented by indexes to the charging station’s tariffs-list. Available only if `EVChargingLocationFeature.TARIFFS` is included in `EVSearchOptions.additional_features`, otherwise empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tariffIndexes: [Int32]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV2id13connectorType6format05powerF017maxVoltageInVolts0i7CurrentK7Amperes0i5PowerK5Watts21termsAndConditionsUrl13tariffIndexesACSS_SSAA0bC6FormatOAA0oF0Os5Int32VA2RSgSSSgSayARGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-id-connectorType-format-powerType-maxVoltageInVolts-maxCurrentInAmperes-maxPowerInWatts-termsAndConditionsUrl-tariffIndexes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingconnector#sdk-for-ios-explore-s-7heresdk19EVChargingConnectorV2id13connectorType6format05powerF017maxVoltageInVolts0i7CurrentK7Amperes0i5PowerK5Watts21termsAndConditionsUrl13tariffIndexesACSS_SSAA0bC6FormatOAA0oF0Os5Int32VA2RSgSSSgSayARGtcfc" class="token"><code>init(id:</code><wbr></wbr><code>connectorType:</code><wbr></wbr><code>format:</code><wbr></wbr><code>powerType:</code><wbr></wbr><code>maxVoltageInVolts:</code><wbr></wbr><code>maxCurrentInAmperes:</code><wbr></wbr><code>maxPowerInWatts:</code><wbr></wbr><code>termsAndConditionsUrl:</code><wbr></wbr><code>tariffIndexes:</code><wbr></wbr><code>)</code></a> 

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
  public init(id: String = "", connectorType: String = "", format: EVChargingConnectorFormat = EVChargingConnectorFormat.socket, powerType: PowerType = PowerType.ac1phase, maxVoltageInVolts: Int32 = 0, maxCurrentInAmperes: Int32 = 0, maxPowerInWatts: Int32? = nil, termsAndConditionsUrl: String? = nil, tariffIndexes: [Int32] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-evchargingconnectorformat">EVChargingConnectorFormat</a>
  - <a href="sdk-for-ios-explore-enums-powertype">PowerType</a>

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

