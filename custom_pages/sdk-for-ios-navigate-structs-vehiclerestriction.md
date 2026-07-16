---
title: "VehicleRestriction Structure Reference"
slug: "sdk-for-ios-navigate-structs-vehiclerestriction"
---

# VehicleRestriction

<div class="declaration">

<div class="language">

``` highlight
public struct VehicleRestriction : Hashable
```

</div>

</div>

Represents a vehicle restriction.

Any non `nil` property adds more details to the restriction. A general truck restriction is represented with `nil` values for properties `restriction` and `hazmatRestriction`.

**Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV11restrictionAA08SpecificC0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-restriction" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV11restrictionAA08SpecificC0VSgvp" class="token"><code>restriction</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A <a href="sdk-for-ios-navigate-structs-specificrestriction">`SpecificRestriction`</a> defines what type of restriction applies (weight, height, etc.) and the range of allowed values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var restriction: SpecificRestriction?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-specificrestriction">SpecificRestriction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV06hazmatC0AA017HazardousMaterialC0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-hazmatRestriction" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV06hazmatC0AA017HazardousMaterialC0VSgvp" class="token"><code>hazmatRestriction</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Restriction on transport of hazardous materials and max allowed tunnel category. For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks carrying flammable materials are not allowed to enter tunnels category D and E - (TunnelCategory.B and TunnelCategory.C allowed).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hazmatRestriction: HazardousMaterialRestriction?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-hazardousmaterialrestriction">HazardousMaterialRestriction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV04timeC0AA04TimeC0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-timeRestriction" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV04timeC0AA04TimeC0VSgvp" class="token"><code>timeRestriction</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Restriction applies during specific time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeRestriction: TimeRestriction?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-timerestriction">TimeRestriction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV17appliesToDeliverySbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-appliesToDelivery" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV17appliesToDeliverySbvp" class="token"><code>appliesToDelivery</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Flag indicating whether this restriction applies to delivery vehicles.

  - `false` means delivery is allowed into this restricted street.
  - `true` means delivery is NOT allowed into this restricted street.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var appliesToDelivery: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV7weatherAA11WeatherTypeOSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-weather" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV7weatherAA11WeatherTypeOSgvp" class="token"><code>weather</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of weather in which restriction applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var weather: WeatherType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-weathertype">WeatherType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV13truckCategoryAA05TruckE0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-truckCategory" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV13truckCategoryAA05TruckE0OSgvp" class="token"><code>truckCategory</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Restriction applies to a specific truck category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckCategory: TruckCategory?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-truckcategory">TruckCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV12trailerCountAA12IntegerRangeVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trailerCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV12trailerCountAA12IntegerRangeVSgvp" class="token"><code>trailerCount</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of trailers for which the restriction applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trailerCount: IntegerRange?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV9axleCountAA12IntegerRangeVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-axleCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV9axleCountAA12IntegerRangeVSgvp" class="token"><code>axleCount</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The axle count for which the current restriction applies. Can be used in conjunction with <a href="sdk-for-ios-navigate-enums-restrictiontype#sdk-for-ios-navigate-s-7heresdk15RestrictionTypeO18weightPerAxleCountyA2CmF">`RestrictionType.weightPerAxleCount`</a> to specify restriction based on weight per number of axles. The `axleCount` considers total number of axles on the whole vehicle (truck + trailers). This can be used to limit the weight per axle for the whole truck. If `axleCount` is null, the restriction is general and applies regardless of axle count. If the upper limit of the `axleCount` range is 0 or `nil` then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. When a user taps the icon, the allowed `axleCount` range can be retrieved directly from `VehicleRestriction.axleCount`. Examples:

  - (2,2) → Restriction applies to vehicles with exactly 2 axles.
  - (2,4) → Restriction applies to vehicles with 2, 3, or 4 axles.
  - (2, 0) → Restriction applies to vehicles with 2 or more axles (equivalent to 2…∞)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var axleCount: IntegerRange?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV16axleCountInGroupAA12IntegerRangeVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-axleCountInGroup" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV16axleCountInGroupAA12IntegerRangeVSgvp" class="token"><code>axleCountInGroup</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of axles in a group for which the current restriction applies. `axleCountInGroup` is a set of axles close together: single, tandem (2), triple (3), etc. Can be used in conjunction with <a href="sdk-for-ios-navigate-enums-restrictiontype#sdk-for-ios-navigate-s-7heresdk15RestrictionTypeO18weightPerAxleGroupyA2CmF">`RestrictionType.weightPerAxleGroup`</a> to specify restriction based on weight per axle group. The `axleCountInGroup` considers number of axles in a specific axle group (usually rear axles on the truck or trailer). This can be used to limit weight for a tandem/triple rear axle group. If the upper limit of the `axleCountInGroup` range is 0 or `nil` then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. Examples:

  - (1,1) → Restriction applies to single axle group.
  - (2,2) → Restriction applies to tandem axle group.
  - (2,4) → Restriction applies to any axle group from 2 to 4 axles.
  - (2,0) → Restriction applies to axle groups with 2 or more axles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var axleCountInGroup: IntegerRange?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV11restriction06hazmatC004timeC017appliesToDelivery7weather13truckCategory12trailerCount04axleN00oN7InGroupAcA08SpecificC0VSg_AA017HazardousMaterialC0VSgAA04TimeC0VSgSbAA11WeatherTypeOSgAA05TruckL0OSgAA12IntegerRangeVSgA2_A2_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-restriction-hazmatRestriction-timeRestriction-appliesToDelivery-weather-truckCategory-trailerCount-axleCount-axleCountInGroup" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-vehiclerestriction#sdk-for-ios-navigate-s-7heresdk18VehicleRestrictionV11restriction06hazmatC004timeC017appliesToDelivery7weather13truckCategory12trailerCount04axleN00oN7InGroupAcA08SpecificC0VSg_AA017HazardousMaterialC0VSgAA04TimeC0VSgSbAA11WeatherTypeOSgAA05TruckL0OSgAA12IntegerRangeVSgA2_A2_tcfc" class="token"><code>init(restriction:</code><wbr></wbr><code>hazmatRestriction:</code><wbr></wbr><code>timeRestriction:</code><wbr></wbr><code>appliesToDelivery:</code><wbr></wbr><code>weather:</code><wbr></wbr><code>truckCategory:</code><wbr></wbr><code>trailerCount:</code><wbr></wbr><code>axleCount:</code><wbr></wbr><code>axleCountInGroup:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(restriction: SpecificRestriction? = nil, hazmatRestriction: HazardousMaterialRestriction? = nil, timeRestriction: TimeRestriction? = nil, appliesToDelivery: Bool = true, weather: WeatherType? = nil, truckCategory: TruckCategory? = nil, trailerCount: IntegerRange? = nil, axleCount: IntegerRange? = nil, axleCountInGroup: IntegerRange? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-specificrestriction">SpecificRestriction</a>
  - <a href="sdk-for-ios-navigate-structs-hazardousmaterialrestriction">HazardousMaterialRestriction</a>
  - <a href="sdk-for-ios-navigate-structs-timerestriction">TimeRestriction</a>
  - <a href="sdk-for-ios-navigate-enums-weathertype">WeatherType</a>
  - <a href="sdk-for-ios-navigate-enums-truckcategory">TruckCategory</a>
  - <a href="sdk-for-ios-navigate-structs-integerrange">IntegerRange</a>

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

