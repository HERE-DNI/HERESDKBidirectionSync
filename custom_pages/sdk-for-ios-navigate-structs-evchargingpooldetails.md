---
title: "EVChargingPoolDetails Structure Reference"
slug: "sdk-for-ios-navigate-structs-evchargingpooldetails"
---

# EVChargingPoolDetails

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingPoolDetails : Hashable
```

</div>

</div>

Electric vehicle charging pool details.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk21EVChargingPoolDetailsV16evChargingOnSiteSbSgvp"></span>` `<span id="//apple_ref/swift/Property/evChargingOnSite" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingpooldetails#/s:7heresdk21EVChargingPoolDetailsV16evChargingOnSiteSbSgvp" class="token"><code>evChargingOnSite</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the Place offers EV charging to customer or the general public.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evChargingOnSite: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21EVChargingPoolDetailsV9evNetworkSSSgvp"></span>` `<span id="//apple_ref/swift/Property/evNetwork" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingpooldetails#/s:7heresdk21EVChargingPoolDetailsV9evNetworkSSSgvp" class="token"><code>evNetwork</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The name of the EV Network that operates the charging station. Note: not all stations participate in a network.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evNetwork: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21EVChargingPoolDetailsV16ownerInformationSSSgvp"></span>` `<span id="//apple_ref/swift/Property/ownerInformation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingpooldetails#/s:7heresdk21EVChargingPoolDetailsV16ownerInformationSSSgvp" class="token"><code>ownerInformation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the party of ownership provided by some suppliers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ownerInformation: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21EVChargingPoolDetailsV10reservableSbSgvp"></span>` `<span id="//apple_ref/swift/Property/reservable" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingpooldetails#/s:7heresdk21EVChargingPoolDetailsV10reservableSbSgvp" class="token"><code>reservable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the charging stations can be reserved. Note: Reservable charging stations operate on a first-come/first served basis.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var reservable: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21EVChargingPoolDetailsV21totalNumberOfStationss6UInt32VSgvp"></span>` `<span id="//apple_ref/swift/Property/totalNumberOfStations" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingpooldetails#/s:7heresdk21EVChargingPoolDetailsV21totalNumberOfStationss6UInt32VSgvp" class="token"><code>totalNumberOfStations</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the total number of stations available on the charging pool.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var totalNumberOfStations: UInt32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(evChargingOnSite: evNetwork: ownerInformation: reservable: totalNumberOfStations: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance. For offline EV rich attributes, also enable <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">`LayerConfiguration.Feature.ev`</a> in <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( evChargingOnSite : Bool ? = nil , evNetwork : String ? = nil , ownerInformation : String ? = nil , reservable : Bool ? = nil , totalNumberOfStations : UInt32 ? = nil )
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

