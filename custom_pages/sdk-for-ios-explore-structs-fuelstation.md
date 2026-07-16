---
title: "FuelStation Structure Reference"
slug: "sdk-for-ios-explore-structs-fuelstation"
---

# FuelStation

<div class="declaration">

<div class="language">

``` highlight
public struct FuelStation : Hashable
```

</div>

</div>

Contains information about a specific fuel station.

Use <a href="sdk-for-ios-explore-classes-placecategory#sdk-for-ios-explore-s-7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ">`PlaceCategory.businessAndServicesPetrolGasolineStation`</a> to find fuel stations. In the <a href="sdk-for-ios-explore-structs-details">`Details`</a> of a <a href="sdk-for-ios-explore-classes-place">`Place`</a> result you can find the associated fuel station information, if any.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11FuelStationV5fuelsSayAA07GenericB0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-fuels" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-fuelstation#sdk-for-ios-explore-s-7heresdk11FuelStationV5fuelsSayAA07GenericB0VGvp" class="token"><code>fuels</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of car fuel types associated with the fuel station. The list can be empty when no generic fuels are offered or when the information is unknown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fuels: [GenericFuel]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-genericfuel">GenericFuel</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11FuelStationV10truckFuelsSayAA05TruckB0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-truckFuels" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-fuelstation#sdk-for-ios-explore-s-7heresdk11FuelStationV10truckFuelsSayAA05TruckB0VGvp" class="token"><code>truckFuels</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of truck fuel types associated with the fuel station. The list can be empty when no truck fuels are offered or when the information is unknown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckFuels: [TruckFuel]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-truckfuel">TruckFuel</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11FuelStationV12payAtThePumpSbSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-payAtThePump" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-fuelstation#sdk-for-ios-explore-s-7heresdk11FuelStationV12payAtThePumpSbSgvp" class="token"><code>payAtThePump</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if paying at the pump is supported or not. `nil` means information is unknown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var payAtThePump: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11FuelStationV15highVolumePumpsSbSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-highVolumePumps" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-fuelstation#sdk-for-ios-explore-s-7heresdk11FuelStationV15highVolumePumpsSbSgvp" class="token"><code>highVolumePumps</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if high volume pumps are available or not. `nil` means information is unknown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var highVolumePumps: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11FuelStationV5fuels10truckFuels12payAtThePump15highVolumePumpsACSayAA07GenericB0VG_SayAA05TruckB0VGSbSgANtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-fuels-truckFuels-payAtThePump-highVolumePumps" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-fuelstation#sdk-for-ios-explore-s-7heresdk11FuelStationV5fuels10truckFuels12payAtThePump15highVolumePumpsACSayAA07GenericB0VG_SayAA05TruckB0VGSbSgANtcfc" class="token"><code>init(fuels:</code><wbr></wbr><code>truckFuels:</code><wbr></wbr><code>payAtThePump:</code><wbr></wbr><code>highVolumePumps:</code><wbr></wbr><code>)</code></a> 

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
  public init(fuels: [GenericFuel] = [], truckFuels: [TruckFuel] = [], payAtThePump: Bool? = nil, highVolumePumps: Bool? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-genericfuel">GenericFuel</a>
  - <a href="sdk-for-ios-explore-structs-truckfuel">TruckFuel</a>

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

