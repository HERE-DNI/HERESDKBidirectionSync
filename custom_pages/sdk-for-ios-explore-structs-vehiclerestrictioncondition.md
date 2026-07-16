---
title: "VehicleRestrictionCondition Structure Reference"
slug: "sdk-for-ios-explore-structs-vehiclerestrictioncondition"
---

# VehicleRestrictionCondition

<div class="declaration">

<div class="language">

``` highlight
public struct VehicleRestrictionCondition : Hashable
```

</div>

</div>

Combined set of conditions that must all be satisfied for a regulation to apply.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV19requiredRoadProfileAA0fgD0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-requiredRoadProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition#sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV19requiredRoadProfileAA0fgD0VSgvp" class="token"><code>requiredRoadProfile</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road profile conditions that activate this restriction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredRoadProfile: RoadProfileCondition?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-roadprofilecondition">RoadProfileCondition</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV015requiredWeatherD0AA0F4TypeOSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-requiredWeatherCondition" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition#sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV015requiredWeatherD0AA0F4TypeOSgvp" class="token"><code>requiredWeatherCondition</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Weather condition that must be present for this restriction to apply.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredWeatherCondition: WeatherType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-weathertype">WeatherType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV13appliesDuringSayAA8TimeRuleCGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-appliesDuring" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition#sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV13appliesDuringSayAA8TimeRuleCGvp" class="token"><code>appliesDuring</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time rules during which this restriction is active.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var appliesDuring: [TimeRule]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV08requiredB7ProfileSayAA0bfC0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-requiredVehicleProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition#sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV08requiredB7ProfileSayAA0bfC0VGvp" class="token"><code>requiredVehicleProfile</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle profile that is subject to this restriction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredVehicleProfile: [VehicleProfileRestriction]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-vehicleprofilerestriction">VehicleProfileRestriction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV19requiredRoadProfile0e7WeatherD013appliesDuring0ebG0AcA0fgD0VSg_AA0H4TypeOSgSayAA8TimeRuleCGSayAA0bgC0VGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-requiredRoadProfile-requiredWeatherCondition-appliesDuring-requiredVehicleProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition#sdk-for-ios-explore-s-7heresdk27VehicleRestrictionConditionV19requiredRoadProfile0e7WeatherD013appliesDuring0ebG0AcA0fgD0VSg_AA0H4TypeOSgSayAA8TimeRuleCGSayAA0bgC0VGtcfc" class="token"><code>init(requiredRoadProfile:</code><wbr></wbr><code>requiredWeatherCondition:</code><wbr></wbr><code>appliesDuring:</code><wbr></wbr><code>requiredVehicleProfile:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance with default values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(requiredRoadProfile: RoadProfileCondition? = nil, requiredWeatherCondition: WeatherType? = nil, appliesDuring: [TimeRule] = [], requiredVehicleProfile: [VehicleProfileRestriction] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-roadprofilecondition">RoadProfileCondition</a>
  - <a href="sdk-for-ios-explore-enums-weathertype">WeatherType</a>
  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>
  - <a href="sdk-for-ios-explore-structs-vehicleprofilerestriction">VehicleProfileRestriction</a>

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

