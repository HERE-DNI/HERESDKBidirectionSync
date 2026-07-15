---
title: "EVChargingStation Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingstation"
---

# EVChargingStation

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingStation : Hashable
```

</div>

</div>

Group of connectors for electric vehicles (EVs), defined by a common charging connector type and maximum power level.

Use <a href="sdk-for-ios-explore-classes-placecategory#/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ">`PlaceCategory.businessAndServicesEvChargingStation`</a> to find stations. In the <a href="sdk-for-ios-explore-structs-details">`Details`</a> of a <a href="sdk-for-ios-explore-classes-place">`Place`</a> result you can find the list of found pools containing stations, if any.

For offline EV rich attributes, enable <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a> in <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV12supplierNameSSSgvp"></span>` `<span id="//apple_ref/swift/Property/supplierName" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV12supplierNameSSSgvp" class="token"><code>supplierName</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EV charging station operator. This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online search using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it can be null if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var supplierName: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV17connectorTypeNameSSSgvp"></span>` `<span id="//apple_ref/swift/Property/connectorTypeName" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV17connectorTypeNameSSSgvp" class="token"><code>connectorTypeName</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of the connector type. For more information on the current connector types, see <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html> May include customer-facing names. In such cases, a ‘customer names’ label is present. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorTypeName: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV15connectorTypeIdSSSgvp"></span>` `<span id="//apple_ref/swift/Property/connectorTypeId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV15connectorTypeIdSSSgvp" class="token"><code>connectorTypeId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  ID of the connector type. For more information on the current connector types, see <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html> This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online searches using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it may be `nil` if the data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorTypeId: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV17powerFeedTypeNameSSSgvp"></span>` `<span id="//apple_ref/swift/Property/powerFeedTypeName" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV17powerFeedTypeNameSSSgvp" class="token"><code>powerFeedTypeName</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of the power feed type, as defined by the <https://en.wikipedia.org/wiki/SAE_J1772#Charging> standard. Provides the customer information on the charge level of the specific Connector Type. Also, can describe level that is used in North America and Australia. In that case label ‘North America (Australia)’ is present. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var powerFeedTypeName: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV15powerFeedTypeIdSSSgvp"></span>` `<span id="//apple_ref/swift/Property/powerFeedTypeId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV15powerFeedTypeIdSSSgvp" class="token"><code>powerFeedTypeId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  ID of the power feed type, as defined by the <https://en.wikipedia.org/wiki/SAE_J1772#Charging> standard. No data in case of offline search. This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online searches using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it may be `nil` if the data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var powerFeedTypeId: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV19maxPowerInKilowattsSdSgvp"></span>` `<span id="//apple_ref/swift/Property/maxPowerInKilowatts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV19maxPowerInKilowattsSdSgvp" class="token"><code>maxPowerInKilowatts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum charge power of connectors in kW. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxPowerInKilowatts: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV14connectorCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/connectorCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV14connectorCounts5Int32VSgvp" class="token"><code>connectorCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of physical connectors at the charging station. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV23availableConnectorCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/availableConnectorCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV23availableConnectorCounts5Int32VSgvp" class="token"><code>availableConnectorCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of available physical connectors at the charging station. This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online searches using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it may be `nil` if the data is unavailable.

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

  ` `<span id="/s:7heresdk17EVChargingStationV22occupiedConnectorCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/occupiedConnectorCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV22occupiedConnectorCounts5Int32VSgvp" class="token"><code>occupiedConnectorCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of occupied physical connectors at the charging station. This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online searches using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it may be `nil` if the data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var occupiedConnectorCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV26outOfServiceConnectorCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/outOfServiceConnectorCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV26outOfServiceConnectorCounts5Int32VSgvp" class="token"><code>outOfServiceConnectorCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of physical connectors that are out of service at the charging station. This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online searches using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it may be `nil` if the data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var outOfServiceConnectorCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV22reservedConnectorCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/reservedConnectorCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV22reservedConnectorCounts5Int32VSgvp" class="token"><code>reservedConnectorCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of physical connectors that are reserved at the charging station. This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online searches using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it may be `nil` if the data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var reservedConnectorCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV11lastUpdated10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/lastUpdated" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV11lastUpdated10Foundation4DateVSgvp" class="token"><code>lastUpdated</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Last update of the `available_connector_count` and `occupied_connector_count` fields. This field is always `nil` for offline search using the <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a>. For online searches using the <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, it may be `nil` if the data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastUpdated: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV12chargingModeSSSgvp"></span>` `<span id="//apple_ref/swift/Property/chargingMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV12chargingModeSSSgvp" class="token"><code>chargingMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charging mode of the charging station. For more information, see <https://en.wikipedia.org/w/index.php?title=Charging_station&oldid=1013010605#IEC-61851-1_Charging_Modes> standard. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargingMode: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV19voltageRangeInVoltsSSSgvp"></span>` `<span id="//apple_ref/swift/Property/voltageRangeInVolts" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV19voltageRangeInVoltsSSSgvp" class="token"><code>voltageRangeInVolts</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Voltage range of the charge provided by the charging station, in volts. Values are alphanumeric represented by the voltage range followed by ‘V’ and by the current type ‘AC’ or ‘DC’, for example: ‘100-120V AC’. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var voltageRangeInVolts: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV21currentRangeInAmperesSSSgvp"></span>` `<span id="//apple_ref/swift/Property/currentRangeInAmperes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV21currentRangeInAmperesSSSgvp" class="token"><code>currentRangeInAmperes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Current range provided by the charging station, in amperes. Values are alphanumeric represented by the Ampere value followed by an ‘A’, for example ‘12A-80A’. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currentRangeInAmperes: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV10phaseCounts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/phaseCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV10phaseCounts5Int32VSgvp" class="token"><code>phaseCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of phases used by the charging station. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var phaseCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV13hasFixedCableSbSgvp"></span>` `<span id="//apple_ref/swift/Property/hasFixedCable" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV13hasFixedCableSbSgvp" class="token"><code>hasFixedCable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates that the cable is fixed or not fixed for a specific Connector Type on the charge station. This field can be `nil` if data is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hasFixedCable: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17EVChargingStationV17physicalReferenceSSSgvp"></span>` `<span id="//apple_ref/swift/Property/physicalReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingstation#/s:7heresdk17EVChargingStationV17physicalReferenceSSSgvp" class="token"><code>physicalReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Printed on the outside of the EVSE for visual identification. Available only in offline search. This field can be `nil` if data is unavailable.

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

      init(supplierName: connectorTypeName: connectorTypeId: powerFeedTypeName: powerFeedTypeId: maxPowerInKilowatts: connectorCount: availableConnectorCount: occupiedConnectorCount: outOfServiceConnectorCount: reservedConnectorCount: lastUpdated: chargingMode: voltageRangeInVolts: currentRangeInAmperes: phaseCount: hasFixedCable: physicalReference: )

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
  public init ( supplierName : String ? = nil , connectorTypeName : String ? = nil , connectorTypeId : String ? = nil , powerFeedTypeName : String ? = nil , powerFeedTypeId : String ? = nil , maxPowerInKilowatts : Double ? = nil , connectorCount : Int32 ? = nil , availableConnectorCount : Int32 ? = nil , occupiedConnectorCount : Int32 ? = nil , outOfServiceConnectorCount : Int32 ? = nil , reservedConnectorCount : Int32 ? = nil , lastUpdated : Date ? = nil , chargingMode : String ? = nil , voltageRangeInVolts : String ? = nil , currentRangeInAmperes : String ? = nil , phaseCount : Int32 ? = nil , hasFixedCable : Bool ? = nil , physicalReference : String ? = nil )
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

