---
title: "TollOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-tolloptions"
---

# TollOptions

<div class="declaration">

<div class="language">

``` highlight
public struct TollOptions : Hashable
```

</div>

</div>

The option to specify how the tolls should be calculated. **Note** Not used for offline calculations.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TollOptionsV12transpondersSaySSGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-transponders" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV12transpondersSaySSGvp" class="token"><code>transponders</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the toll collection systems for which the user has valid transponders. Note: currently, the only valid value is “all”. This means the user has a transponder that is accepted by all toll systems.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transponders: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TollOptionsV15vehicleCategoryAC07VehicleE0OSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-vehicleCategory" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV15vehicleCategoryAC07VehicleE0OSgvp" class="token"><code>vehicleCategory</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines special vehicle category for toll calculation. Usual types like car or truck are determined from transport mode.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleCategory: TollOptions.VehicleCategory?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tolloptions-vehiclecategory">VehicleCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TollOptionsV12emissionTypeAC08EmissionE0OSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-emissionType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV12emissionTypeAC08EmissionE0OSgvp" class="token"><code>emissionType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the emission type as defined by the toll operator for toll calculation based on vehicle emissions class. The emission type is based on the European emission standards (Euro 1 to Euro 6, and Euro EEV).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var emissionType: TollOptions.EmissionType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tolloptions-emissiontype">EmissionType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TollOptionsV8co2Classs5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-co2Class" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV8co2Classs5Int32VSgvp" class="token"><code>co2Class</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the CO2 class of the vehicle as defined by the toll operator. CO2 class is used with <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV12emissionTypeAC08EmissionE0OSgvp">`emissionType`</a>. Allowed values for CO2 class are 1, 2, 3, 4, or 5, where a lower value generally indicates lower CO2 emissions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var co2Class: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TollOptionsV12transponders15vehicleCategory12emissionType8co2ClassACSaySSG_AC07VehicleF0OSgAC08EmissionH0OSgs5Int32VSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-transponders-vehicleCategory-emissionType-co2Class" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV12transponders15vehicleCategory12emissionType8co2ClassACSaySSG_AC07VehicleF0OSgAC08EmissionH0OSgs5Int32VSgtcfc" class="token"><code>init(transponders:</code><wbr></wbr><code>vehicleCategory:</code><wbr></wbr><code>emissionType:</code><wbr></wbr><code>co2Class:</code><wbr></wbr><code>)</code></a> 

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
  public init(transponders: [String] = [], vehicleCategory: TollOptions.VehicleCategory? = nil, emissionType: TollOptions.EmissionType? = nil, co2Class: Int32? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tolloptions-vehiclecategory">VehicleCategory</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions-emissiontype">EmissionType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TollOptionsV15VehicleCategoryO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-VehicleCategory" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV15VehicleCategoryO" class="token"><code>VehicleCategory</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Supported options of vehicle category for toll calculation.

  <a href="sdk-for-ios-explore-structs-tolloptions-vehiclecategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum VehicleCategory : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TollOptionsV12EmissionTypeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-EmissionType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tolloptions#sdk-for-ios-explore-s-7heresdk11TollOptionsV12EmissionTypeO" class="token"><code>EmissionType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Supported options of emission type

  <a href="sdk-for-ios-explore-structs-tolloptions-emissiontype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EmissionType : UInt32, CaseIterable, Codable
  ```

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

