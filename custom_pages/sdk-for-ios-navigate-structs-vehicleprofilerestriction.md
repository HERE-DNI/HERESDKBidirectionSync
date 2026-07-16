---
title: "VehicleProfileRestriction Structure Reference"
slug: "sdk-for-ios-navigate-structs-vehicleprofilerestriction"
---

# VehicleProfileRestriction

<div class="declaration">

<div class="language">

``` highlight
public struct VehicleProfileRestriction : Hashable
```

</div>

</div>

Physical and cargo profile of a vehicle that triggers a regulation.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV09requestedB4TypeAA0bF9ConditionOSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-requestedVehicleType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehicleprofilerestriction#sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV09requestedB4TypeAA0bF9ConditionOSgvp" class="token"><code>requestedVehicleType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle type to which this restriction applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requestedVehicleType: VehicleTypeCondition?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-vehicletypecondition">VehicleTypeCondition</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV25requiredWeightInKilogramsAA12IntegerRangeVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-requiredWeightInKilograms" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehicleprofilerestriction#sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV25requiredWeightInKilogramsAA12IntegerRangeVvp" class="token"><code>requiredWeightInKilograms</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Weight limits in kilograms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredWeightInKilograms: IntegerRange
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV30requiredGrossWeightInKilogramsAA12IntegerRangeVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-requiredGrossWeightInKilograms" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehicleprofilerestriction#sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV30requiredGrossWeightInKilogramsAA12IntegerRangeVvp" class="token"><code>requiredGrossWeightInKilograms</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gross weight limits in kilograms.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredGrossWeightInKilograms: IntegerRange
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV24requiredAmountOfTrailersAA12IntegerRangeVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-requiredAmountOfTrailers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehicleprofilerestriction#sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV24requiredAmountOfTrailersAA12IntegerRangeVvp" class="token"><code>requiredAmountOfTrailers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Trailer count limits.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredAmountOfTrailers: IntegerRange
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV17hazardousMaterialAA09HazardousF4TypeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-hazardousMaterial" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehicleprofilerestriction#sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV17hazardousMaterialAA09HazardousF4TypeOvp" class="token"><code>hazardousMaterial</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Hazardous material condition associated with this profile.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hazardousMaterial: HazardousMaterialType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-hazardousmaterialtype">HazardousMaterialType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV09requestedB4Type25requiredWeightInKilograms0g5GrosshiJ00G16AmountOfTrailers17hazardousMaterialAcA0bF9ConditionOSg_AA12IntegerRangeVA2mA09HazardouspF0Otcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-requestedVehicleType-requiredWeightInKilograms-requiredGrossWeightInKilograms-requiredAmountOfTrailers-hazardousMaterial" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehicleprofilerestriction#sdk-for-ios-navigate-s-7heresdk25VehicleProfileRestrictionV09requestedB4Type25requiredWeightInKilograms0g5GrosshiJ00G16AmountOfTrailers17hazardousMaterialAcA0bF9ConditionOSg_AA12IntegerRangeVA2mA09HazardouspF0Otcfc" class="token"><code>init(requestedVehicleType:</code><wbr></wbr><code>requiredWeightInKilograms:</code><wbr></wbr><code>requiredGrossWeightInKilograms:</code><wbr></wbr><code>requiredAmountOfTrailers:</code><wbr></wbr><code>hazardousMaterial:</code><wbr></wbr><code>)</code></a> 

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
  public init(requestedVehicleType: VehicleTypeCondition? = nil, requiredWeightInKilograms: IntegerRange, requiredGrossWeightInKilograms: IntegerRange, requiredAmountOfTrailers: IntegerRange, hazardousMaterial: HazardousMaterialType)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-vehicletypecondition">VehicleTypeCondition</a>
  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>
  - <a href="sdk-for-ios-navigate-enums-hazardousmaterialtype">HazardousMaterialType</a>

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

