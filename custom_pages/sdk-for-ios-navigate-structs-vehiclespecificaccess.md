---
title: "VehicleSpecificAccess Structure Reference"
slug: "sdk-for-ios-navigate-structs-vehiclespecificaccess"
---

# VehicleSpecificAccess

<div class="declaration">

<div class="language">

``` highlight
public struct VehicleSpecificAccess : Hashable
```

</div>

</div>

Access regulation for a specific vehicle type on a road segment.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV13isPermitBasedSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isPermitBased" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificaccess#sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV13isPermitBasedSbvp" class="token"><code>isPermitBased</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, access is only permitted with a special permit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPermitBased: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV17physicalStructureAA08PhysicalF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-physicalStructure" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificaccess#sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV17physicalStructureAA08PhysicalF0Ovp" class="token"><code>physicalStructure</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Physical structure (e.g. bridge or tunnel) to which this access regulation applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var physicalStructure: PhysicalStructure
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-physicalstructure">PhysicalStructure</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV20noTruckInnermostLanes5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-noTruckInnermostLane" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificaccess#sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV20noTruckInnermostLanes5Int32VSgvp" class="token"><code>noTruckInnermostLane</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, trucks are prohibited from using the innermost lane.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var noTruckInnermostLane: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV9conditionAA0B20RestrictionConditionVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-condition" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificaccess#sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV9conditionAA0B20RestrictionConditionVvp" class="token"><code>condition</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Conditions under which this access regulation is active.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var condition: VehicleRestrictionCondition
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV13isPermitBased17physicalStructure20noTruckInnermostLane9conditionACSb_AA08PhysicalI0Os5Int32VSgAA0B20RestrictionConditionVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-isPermitBased-physicalStructure-noTruckInnermostLane-condition" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificaccess#sdk-for-ios-navigate-s-7heresdk21VehicleSpecificAccessV13isPermitBased17physicalStructure20noTruckInnermostLane9conditionACSb_AA08PhysicalI0Os5Int32VSgAA0B20RestrictionConditionVtcfc" class="token"><code>init(isPermitBased:</code><wbr></wbr><code>physicalStructure:</code><wbr></wbr><code>noTruckInnermostLane:</code><wbr></wbr><code>condition:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance with specified parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(isPermitBased: Bool, physicalStructure: PhysicalStructure, noTruckInnermostLane: Int32? = nil, condition: VehicleRestrictionCondition)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-physicalstructure">PhysicalStructure</a>
  - <a href="sdk-for-ios-navigate-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a>

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

