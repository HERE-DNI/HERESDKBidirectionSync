---
title: "EVChargingConnectorGroup Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingconnectorgroup"
---

# EVChargingConnectorGroup

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingConnectorGroup : Hashable
```

</div>

</div>

Represents the connector group at the charging location. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk24EVChargingConnectorGroupV13connectorTypeSSvp"></span>` `<span id="//apple_ref/swift/Property/connectorType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingconnectorgroup#/s:7heresdk24EVChargingConnectorGroupV13connectorTypeSSvp" class="token"><code>connectorType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The standard (type) of the connectors belonging to this group. Should be one of the constants defined in <a href="sdk-for-ios-explore-structs-evchargingconnectortype">`EVChargingConnectorType`</a>.

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

  ` `<span id="/s:7heresdk24EVChargingConnectorGroupV15maxPowerInWattss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/maxPowerInWatts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingconnectorgroup#/s:7heresdk24EVChargingConnectorGroupV15maxPowerInWattss5Int32Vvp" class="token"><code>maxPowerInWatts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum power that can be delivered by the connectors, in watts (W). Connectors without max power are not grouped.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxPowerInWatts: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp"></span>` `<span id="//apple_ref/swift/Property/connectors" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingconnectorgroup#/s:7heresdk24EVChargingConnectorGroupV10connectorsSayAA0bC9ReferenceVGvp" class="token"><code>connectors</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Array of EVSE + connector(s) pairs that belong to the group. Provides access to EVSE statuses and more detailed connector characteristics. Available only if `EVChargingLocationFeature.EVSES` is included in `EVSearchOptions.additional_features`, otherwise empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectors: [EVChargingConnectorReference]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EVChargingConnectorGroupV14connectorCounts5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/connectorCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingconnectorgroup#/s:7heresdk24EVChargingConnectorGroupV14connectorCounts5Int32Vvp" class="token"><code>connectorCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of connectors in the group. If an EVSE has multiple identical connectors they are counted as one as only one is accessible at a time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorCount: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EVChargingConnectorGroupV09availableC5Counts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/availableConnectorCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingconnectorgroup#/s:7heresdk24EVChargingConnectorGroupV09availableC5Counts5Int32VSgvp" class="token"><code>availableConnectorCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of connectors available for use at the time of query. The field is not present if the availability is not known.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var availableConnectorCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp"></span>` `<span id="//apple_ref/swift/Property/tariffIndexes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingconnectorgroup#/s:7heresdk24EVChargingConnectorGroupV13tariffIndexesSays5Int32VGvp" class="token"><code>tariffIndexes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tariffs for the connector group, represented by indexes to the charging station’s tariffs-list. Available only if `EVChargingLocationFeature.TARIFFS` is included in `EVSearchOptions.additional_features`, otherwise empty.

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

      init(connectorType: maxPowerInWatts: connectors: connectorCount: availableConnectorCount: tariffIndexes: )

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
  public init ( connectorType : String = "" , maxPowerInWatts : Int32 = 1 , connectors : [ EVChargingConnectorReference ] = [], connectorCount : Int32 = 1 , availableConnectorCount : Int32 ? = nil , tariffIndexes : [ Int32 ] = [])
  ```

  </pre>

  </div>

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

