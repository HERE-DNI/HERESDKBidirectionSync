---
title: "ChargingStation Structure Reference"
slug: "sdk-for-ios-navigate-structs-chargingstation"
---

# ChargingStation

<div class="declaration">

<div class="language">

``` highlight
public struct ChargingStation : Hashable
```

</div>

</div>

Data for an electric vehicle charging station.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk15ChargingStationV2idSSSgvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-chargingstation#/s:7heresdk15ChargingStationV2idSSSgvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of this charging station. It can only be null when custom charging stations from non-HERE datasets have been injected on the HERE platform. By default, with HERE datasets it is guranteed to be not null.

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

  ` `<span id="/s:7heresdk15ChargingStationV4nameSSSgvp"></span>` `<span id="//apple_ref/swift/Property/name" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-chargingstation#/s:7heresdk15ChargingStationV4nameSSSgvp" class="token"><code>name</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Human readable name of this charging station. It can be null when there is no name associated with the station.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15ChargingStationV19connectorAttributesAA0b9ConnectorE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/connectorAttributes" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-chargingstation#/s:7heresdk15ChargingStationV19connectorAttributesAA0b9ConnectorE0VSgvp" class="token"><code>connectorAttributes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Details of the connector suggested to be used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectorAttributes: ChargingConnectorAttributes?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15ChargingStationV5brandAA6NameIDVSgvp"></span>` `<span id="//apple_ref/swift/Property/brand" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-chargingstation#/s:7heresdk15ChargingStationV5brandAA6NameIDVSgvp" class="token"><code>brand</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charging station brand. <a href="sdk-for-ios-navigate-structs-nameid#/s:7heresdk6NameIDV4nameSSSgvp">`NameID.name`</a> reflect to charging station brand name. <a href="sdk-for-ios-navigate-structs-nameid#/s:7heresdk6NameIDV2idSSSgvp">`NameID.id`</a> reflect to charging station brand unique ID.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var brand: NameID?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15ChargingStationV19chargePointOperatorAA6NameIDVSgvp"></span>` `<span id="//apple_ref/swift/Property/chargePointOperator" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-chargingstation#/s:7heresdk15ChargingStationV19chargePointOperatorAA6NameIDVSgvp" class="token"><code>chargePointOperator</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charging station charge-point-operator. <a href="sdk-for-ios-navigate-structs-nameid#/s:7heresdk6NameIDV4nameSSSgvp">`NameID.name`</a> reflect to charge-point-operator name. <a href="sdk-for-ios-navigate-structs-nameid#/s:7heresdk6NameIDV2idSSSgvp">`NameID.id`</a> reflect to charge-point-operator ID.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargePointOperator: NameID?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15ChargingStationV33matchingEMobilityServiceProvidersSayAA6NameIDVGvp"></span>` `<span id="//apple_ref/swift/Property/matchingEMobilityServiceProviders" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-chargingstation#/s:7heresdk15ChargingStationV33matchingEMobilityServiceProvidersSayAA6NameIDVGvp" class="token"><code>matchingEMobilityServiceProviders</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of matched E-Mobility Service Providers. Populated only when <a href="sdk-for-ios-navigate-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp">`ElectricVehicleOptions.evMobilityServiceProviderPreferences`</a> was set. This list reflects the subset of E-Mobility Service Providers supported by the charging station, from the list specified in the request parameter <a href="sdk-for-ios-navigate-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp">`ElectricVehicleOptions.evMobilityServiceProviderPreferences`</a>. <a href="sdk-for-ios-navigate-structs-nameid#/s:7heresdk6NameIDV4nameSSSgvp">`NameID.name`</a> in each list item reflect to E-Mobility Service Provider name. <a href="sdk-for-ios-navigate-structs-nameid#/s:7heresdk6NameIDV2idSSSgvp">`NameID.id`</a> in each list item reflect to E-Mobility Service Provider id.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var matchingEMobilityServiceProviders: [NameID]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: name: connectorAttributes: brand: chargePointOperator: matchingEMobilityServiceProviders: )

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
  public init ( id : String ? = nil , name : String ? = nil , connectorAttributes : ChargingConnectorAttributes ? = nil , brand : NameID ? = nil , chargePointOperator : NameID ? = nil , matchingEMobilityServiceProviders : [ NameID ] = [])
  ```

  </pre>

  </div>

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

