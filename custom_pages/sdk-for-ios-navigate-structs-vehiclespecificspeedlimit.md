---
title: "VehicleSpecificSpeedLimit Structure Reference"
slug: "sdk-for-ios-navigate-structs-vehiclespecificspeedlimit"
---

# VehicleSpecificSpeedLimit

<div class="declaration">

<div class="language">

``` highlight
public struct VehicleSpecificSpeedLimit : Hashable
```

</div>

</div>

Speed limit regulation specific to a vehicle type.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-speedLimitInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificspeedlimit#sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecondSdvp" class="token"><code>speedLimitInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum permitted speed in meters per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedLimitInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV10isAdvisorySbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isAdvisory" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificspeedlimit#sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV10isAdvisorySbvp" class="token"><code>isAdvisory</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, this speed limit is advisory rather than legally enforced.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isAdvisory: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV022builtUpAreaMaxOverrideD17InMetersPerSecondSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-builtUpAreaMaxOverrideSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificspeedlimit#sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV022builtUpAreaMaxOverrideD17InMetersPerSecondSdSgvp" class="token"><code>builtUpAreaMaxOverrideSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Max Override Speed indicates the maximum speed a commercial vehicle may travel within a BUA. Could be 0 if unlimited. A `nil` value means the speed limit is not affected by the BUA override or not present.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var builtUpAreaMaxOverrideSpeedInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV9conditionAA0B20RestrictionConditionVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-condition" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificspeedlimit#sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV9conditionAA0B20RestrictionConditionVvp" class="token"><code>condition</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Conditions under which this speed limit is active.

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

   <span id="sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecond10isAdvisory022builtUpAreaMaxOverridedghiJ09conditionACSd_SbSdSgAA0B20RestrictionConditionVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-speedLimitInMetersPerSecond-isAdvisory-builtUpAreaMaxOverrideSpeedInMetersPerSecond-condition" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclespecificspeedlimit#sdk-for-ios-navigate-s-7heresdk25VehicleSpecificSpeedLimitV05speedE17InMetersPerSecond10isAdvisory022builtUpAreaMaxOverridedghiJ09conditionACSd_SbSdSgAA0B20RestrictionConditionVtcfc" class="token"><code>init(speedLimitInMetersPerSecond:</code><wbr></wbr><code>isAdvisory:</code><wbr></wbr><code>builtUpAreaMaxOverrideSpeedInMetersPerSecond:</code><wbr></wbr><code>condition:</code><wbr></wbr><code>)</code></a> 

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
  public init(speedLimitInMetersPerSecond: Double, isAdvisory: Bool, builtUpAreaMaxOverrideSpeedInMetersPerSecond: Double? = nil, condition: VehicleRestrictionCondition)
  ```

  </div>

  Related types:

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

