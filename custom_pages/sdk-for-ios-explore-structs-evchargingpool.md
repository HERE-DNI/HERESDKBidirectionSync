---
title: "EVChargingPool Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingpool"
---

# EVChargingPool

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingPool : Hashable
```

</div>

</div>

A charging pool for electric vehicles is an area equipped with one or more charging stations.

Use <a href="sdk-for-ios-explore-classes-placecategory#/s:7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ">`PlaceCategory.businessAndServicesEvChargingStation`</a> to find stations. In the <a href="sdk-for-ios-explore-structs-details">`Details`</a> of a <a href="sdk-for-ios-explore-classes-place">`Place`</a> result you can find the list of found pools containing stations, if any.

For offline EV rich attributes, also enable <a href="sdk-for-ios-explore-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a> in <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk14EVChargingPoolV16chargingStationsSayAA0B7StationVGvp"></span>` `<span id="//apple_ref/swift/Property/chargingStations" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV16chargingStationsSayAA0B7StationVGvp" class="token"><code>chargingStations</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of charging stations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargingStations: [EVChargingStation]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVChargingPoolV25eMobilityServiceProvidersSayAA09EMobilityE8ProviderVGvp"></span>` `<span id="//apple_ref/swift/Property/eMobilityServiceProviders" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV25eMobilityServiceProvidersSayAA09EMobilityE8ProviderVGvp" class="token"><code>eMobilityServiceProviders</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of e-Mobility Service Providers. Only online search fills this field.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var eMobilityServiceProviders: [EMobilityServiceProvider]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVChargingPoolV6accessAA12EVAccessTypeOSgvp"></span>` `<span id="//apple_ref/swift/Property/access" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV6accessAA12EVAccessTypeOSgvp" class="token"><code>access</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The accessibility level of the charging pool, or `nil` if unknown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var access: EVAccessType?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVChargingPoolV24accessRestrictionReasonsSayAA08EVAccessE6ReasonOGvp"></span>` `<span id="//apple_ref/swift/Property/accessRestrictionReasons" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV24accessRestrictionReasonsSayAA08EVAccessE6ReasonOGvp" class="token"><code>accessRestrictionReasons</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the list of reasons for restriction. Populated only for offline search and when access is <a href="sdk-for-ios-explore-enums-evaccesstype#/s:7heresdk12EVAccessTypeO16restrictedAccessyA2CmF">`EVAccessType.restrictedAccess`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var accessRestrictionReasons: [EVAccessRestrictionReason]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVChargingPoolV7detailsAA0bC7DetailsVSgvp"></span>` `<span id="//apple_ref/swift/Property/details" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV7detailsAA0bC7DetailsVSgvp" class="token"><code>details</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EV charging station attributes details. It is available only for a place that has charging station for electric vehicles. Only offline search fills this field.

  **Note:** Not available as part of <a href="sdk-for-ios-explore-classes-suggestion">`Suggestion`</a> results.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var details: EVChargingPoolDetails?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVChargingPoolV2idSSSgvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV2idSSSgvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  HERE ID of the charging pool. Only online search fills this field.

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

  ` `<span id="/s:7heresdk14EVChargingPoolV5cpoIdSSSgvp"></span>` `<span id="//apple_ref/swift/Property/cpoId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV5cpoIdSSSgvp" class="token"><code>cpoId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  CPO (Charge Point Operator) id for charging pool. Only online search fills this field.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cpoId: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EVChargingPoolV8evseInfoSayAA4EvseVGvp"></span>` `<span id="//apple_ref/swift/Property/evseInfo" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingpool#/s:7heresdk14EVChargingPoolV8evseInfoSayAA4EvseVGvp" class="token"><code>evseInfo</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point. Only online search fills this field.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evseInfo: [Evse]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(chargingStations: eMobilityServiceProviders: access: accessRestrictionReasons: details: id: cpoId: evseInfo: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - chargingStations: List of charging stations.
    - eMobilityServiceProviders: List of e-Mobility Service Providers. Only online search fills this field.
    - access: The accessibility level of the charging pool, or `nil` if unknown.
    - accessRestrictionReasons: Contains the list of reasons for restriction. Populated only for offline search and when access is <a href="sdk-for-ios-explore-enums-evaccesstype#/s:7heresdk12EVAccessTypeO16restrictedAccessyA2CmF">`EVAccessType.restrictedAccess`</a>.
    - details: EV charging station attributes details. It is available only for a place that has charging station for electric vehicles. Only offline search fills this field.

    **Note:** Not available as part of <a href="sdk-for-ios-explore-classes-suggestion">`Suggestion`</a> results.

    - id: HERE ID of the charging pool. Only online search fills this field.
    - cpoId: CPO (Charge Point Operator) id for charging pool. Only online search fills this field.
    - evseInfo: Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point. Only online search fills this field.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( chargingStations : [ EVChargingStation ], eMobilityServiceProviders : [ EMobilityServiceProvider ], access : EVAccessType ? = nil , accessRestrictionReasons : [ EVAccessRestrictionReason ], details : EVChargingPoolDetails ? = nil , id : String ? = nil , cpoId : String ? = nil , evseInfo : [ Evse ] = [])
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

