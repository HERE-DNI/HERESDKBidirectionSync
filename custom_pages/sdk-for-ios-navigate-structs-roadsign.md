---
title: "RoadSign Structure Reference"
slug: "sdk-for-ios-navigate-structs-roadsign"
---

# RoadSign

<div class="declaration">

<div class="language">

``` highlight
public struct RoadSign : Hashable
```

</div>

</div>

Describes a road sign.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV14offsetInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-offsetInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV14offsetInMeterss5Int32Vvp" class="token"><code>offsetInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The offset in meters from the beginning of the segment to the location of the road sign in positive direction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offsetInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV15travelDirectionAA06TravelE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-travelDirection" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV15travelDirectionAA06TravelE0Ovp" class="token"><code>travelDirection</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Segment direction which the road sign is applied.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var travelDirection: TravelDirection
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-traveldirection">TravelDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV04roadC4TypeAA0bcE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadSignType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV04roadC4TypeAA0bcE0Ovp" class="token"><code>roadSignType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of the road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadSignType: RoadSignType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-roadsigntype">RoadSignType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV04roadC8CategoryAA0bcE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadSignCategory" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV04roadC8CategoryAA0bcE0Ovp" class="token"><code>roadSignCategory</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The main category to which the road sign belongs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadSignCategory: RoadSignCategory
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-roadsigncategory">RoadSignCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV010isPriorityC0Sbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isPrioritySign" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV010isPriorityC0Sbvp" class="token"><code>isPrioritySign</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Flag indicating if the road sign is a priority sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPrioritySign: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV18generalWarningTypeAA07GeneralebcF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-generalWarningType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV18generalWarningTypeAA07GeneralebcF0Ovp" class="token"><code>generalWarningType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the general warning to which the road sign belongs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var generalWarningType: GeneralWarningRoadSignType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV12vehicleTypesSayAA0bC11VehicleTypeOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-vehicleTypes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV12vehicleTypesSayAA0bC11VehicleTypeOGvp" class="token"><code>vehicleTypes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies a list of vehicle types for which the road sign is applicable. The list will be empty when the road sign is applicable for all vehicles including cars.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleTypes: [RoadSignVehicleType]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-roadsignvehicletype">RoadSignVehicleType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV11weatherTypeAA07WeatherE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-weatherType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV11weatherTypeAA07WeatherE0Ovp" class="token"><code>weatherType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the weather type for which the sign is applicable. If weather type is <a href="sdk-for-ios-navigate-enums-weathertype#sdk-for-ios-navigate-s-7heresdk11WeatherTypeO7unknownyA2CmF">`WeatherType.unknown`</a>, the sign is actual for all weather types.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var weatherType: WeatherType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-weathertype">WeatherType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV09localizedC5ValueAA13LocalizedTextVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-localizedSignValue" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV09localizedC5ValueAA13LocalizedTextVSgvp" class="token"><code>localizedSignValue</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var localizedSignValue: LocalizedText?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtext">LocalizedText</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV19localizedPreWarningAA13LocalizedTextVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-localizedPreWarning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV19localizedPreWarningAA13LocalizedTextVSgvp" class="token"><code>localizedPreWarning</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional pre-warning in terms of distance, of the upcoming warning or regulation. The pre-warning information is given as printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var localizedPreWarning: LocalizedText?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtext">LocalizedText</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV17localizedDurationAA13LocalizedTextVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-localizedDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV17localizedDurationAA13LocalizedTextVSgvp" class="token"><code>localizedDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional length information during which the warning is applicable. Usually, this information is shown on a separate shield below the main shield. For example, a sign may warn on playing children for a length of 100 m, starting from the location of the warning sign. The length information (most likely with units) is given as printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var localizedDuration: LocalizedText?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtext">LocalizedText</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV21localizedValidityTimeAA13LocalizedTextVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-localizedValidityTime" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV21localizedValidityTimeAA13LocalizedTextVSgvp" class="token"><code>localizedValidityTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional text visible on the supplemental sign indicating specific time(s) at which the road sign is applicable. The time information is given as printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var localizedValidityTime: LocalizedText?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtext">LocalizedText</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8RoadSignV14offsetInMeters15travelDirection04roadC4Type0iC8Category010isPriorityC0014generalWarningJ012vehicleTypes07weatherJ009localizedC5Value0s3PreO00S8Duration0S12ValidityTimeACs5Int32V_AA06TravelH0OAA0bcJ0OAA0bcK0OSbAA07GeneralobcJ0OSayAA0bc7VehicleJ0OGAA07WeatherJ0OAA13LocalizedTextVSgA5_A5_A5_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-offsetInMeters-travelDirection-roadSignType-roadSignCategory-isPrioritySign-generalWarningType-vehicleTypes-weatherType-localizedSignValue-localizedPreWarning-localizedDuration-localizedValidityTime" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-roadsign#sdk-for-ios-navigate-s-7heresdk8RoadSignV14offsetInMeters15travelDirection04roadC4Type0iC8Category010isPriorityC0014generalWarningJ012vehicleTypes07weatherJ009localizedC5Value0s3PreO00S8Duration0S12ValidityTimeACs5Int32V_AA06TravelH0OAA0bcJ0OAA0bcK0OSbAA07GeneralobcJ0OSayAA0bc7VehicleJ0OGAA07WeatherJ0OAA13LocalizedTextVSgA5_A5_A5_tcfc" class="token"><code>init(offsetInMeters:</code><wbr></wbr><code>travelDirection:</code><wbr></wbr><code>roadSignType:</code><wbr></wbr><code>roadSignCategory:</code><wbr></wbr><code>isPrioritySign:</code><wbr></wbr><code>generalWarningType:</code><wbr></wbr><code>vehicleTypes:</code><wbr></wbr><code>weatherType:</code><wbr></wbr><code>localizedSignValue:</code><wbr></wbr><code>localizedPreWarning:</code><wbr></wbr><code>localizedDuration:</code><wbr></wbr><code>localizedValidityTime:</code><wbr></wbr><code>)</code></a> 

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
  public init(offsetInMeters: Int32, travelDirection: TravelDirection, roadSignType: RoadSignType, roadSignCategory: RoadSignCategory, isPrioritySign: Bool, generalWarningType: GeneralWarningRoadSignType, vehicleTypes: [RoadSignVehicleType], weatherType: WeatherType, localizedSignValue: LocalizedText? = nil, localizedPreWarning: LocalizedText? = nil, localizedDuration: LocalizedText? = nil, localizedValidityTime: LocalizedText? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-traveldirection">TravelDirection</a>
  - <a href="sdk-for-ios-navigate-enums-roadsigntype">RoadSignType</a>
  - <a href="sdk-for-ios-navigate-enums-roadsigncategory">RoadSignCategory</a>
  - <a href="sdk-for-ios-navigate-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a>
  - <a href="sdk-for-ios-navigate-enums-roadsignvehicletype">RoadSignVehicleType</a>
  - <a href="sdk-for-ios-navigate-enums-weathertype">WeatherType</a>
  - <a href="sdk-for-ios-navigate-structs-localizedtext">LocalizedText</a>

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

