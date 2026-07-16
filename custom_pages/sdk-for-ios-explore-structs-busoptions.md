---
title: "BusOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-busoptions"
---

# BusOptions

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")
public struct BusOptions : Hashable
```

</div>

</div>

All the options to specify how a bus route should be calculated.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV05routeC0AA05RouteC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV05routeC0AA05RouteC0Vvp" class="token"><code>routeOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the common route calculation options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeOptions: RouteOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV04textC0AA09RouteTextC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-textOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV04textC0AA09RouteTextC0Vvp" class="token"><code>textOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Customize textual content returned from the route calculation, such as localization, format, and unit system.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textOptions: RouteTextOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-avoidanceOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV09avoidanceC0AA09AvoidanceC0Vvp" class="token"><code>avoidanceOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options to specify restrictions for route calculations. By default no restrictions are applied.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidanceOptions: AvoidanceOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV04tollC0AA04TollC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tollOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV04tollC0AA04TollC0Vvp" class="token"><code>tollOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tollOptions: TollOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tolloptions">TollOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV05allowC0AA05AllowC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-allowOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV05allowC0AA05AllowC0Vvp" class="token"><code>allowOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options explicitly allowed by user for route calculations. By default no options are opt in.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var allowOptions: AllowOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-allowoptions">AllowOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV15occupantsNumbers5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-occupantsNumber" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV15occupantsNumbers5Int32Vvp" class="token"><code>occupantsNumber</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the number of occupants in the vehicle, including driver, can affect the vehicle’s ability to use HOV/carpool restricted lanes. Shouldn’t be less than 1 or greater than 255. Defaults to 1.

  **Note:** This parameter has no effect unless HOV and/or HOT lane usage is enabled via <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV05allowC0AA05AllowC0Vvp">`BusOptions.allowOptions`</a> and such lanes are available in the selected country.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var occupantsNumber: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV27lastCharacterOfLicensePlateSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastCharacterOfLicensePlate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV27lastCharacterOfLicensePlateSSSgvp" class="token"><code>lastCharacterOfLicensePlate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the last character of a vehicle’s license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: “7”, when the license plate of a vehicle looks like “B-ET-182487”.

  If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastCharacterOfLicensePlate: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maxSpeedOnSegments" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp" class="token"><code>maxSpeedOnSegments</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Segments with restriction on maximum baseSpeed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxSpeedOnSegments: [MaxSpeedOnSegment]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-maxspeedonsegment">MaxSpeedOnSegment</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV17busSpecificationsAA0bE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-busSpecifications" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV17busSpecificationsAA0bE0Vvp" class="token"><code>busSpecifications</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Detailed bus specifications such as dimensions and weight.

  **Note:** Some members of `bus_specifications` have limited value range.

  - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV22grossWeightInKilogramss5Int32VSgvp">`BusSpecifications.grossWeightInKilograms`</a> must not be negative.
  - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV19heightInCentimeterss5Int32VSgvp">`BusSpecifications.heightInCentimeters`</a> must be in the range \[0, 5000\].
  - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV18widthInCentimeterss5Int32VSgvp">`BusSpecifications.widthInCentimeters`</a> must be in the range \[0, 5000\].
  - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV19lengthInCentimeterss5Int32VSgvp">`BusSpecifications.lengthInCentimeters`</a> must be in the range \[0, 30000\]. The validation of the range is done in the method that takes `BusOptions` as parameter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var busSpecifications: BusSpecifications
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-busspecifications">BusSpecifications</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10BusOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments17busSpecificationsAcA05RouteC0V_AA0v4TextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGAA0bU0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-routeOptions-textOptions-avoidanceOptions-tollOptions-allowOptions-occupantsNumber-lastCharacterOfLicensePlate-maxSpeedOnSegments-busSpecifications" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments17busSpecificationsAcA05RouteC0V_AA0v4TextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGAA0bU0Vtcfc" class="token"><code>init(routeOptions:</code><wbr></wbr><code>textOptions:</code><wbr></wbr><code>avoidanceOptions:</code><wbr></wbr><code>tollOptions:</code><wbr></wbr><code>allowOptions:</code><wbr></wbr><code>occupantsNumber:</code><wbr></wbr><code>lastCharacterOfLicensePlate:</code><wbr></wbr><code>maxSpeedOnSegments:</code><wbr></wbr><code>busSpecifications:</code><wbr></wbr><code>)</code></a> 

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

    - routeOptions: Specifies the common route calculation options.
    - textOptions: Customize textual content returned from the route calculation, such as localization, format, and unit system.
    - avoidanceOptions: Options to specify restrictions for route calculations. By default no restrictions are applied.
    - tollOptions: Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.
    - allowOptions: The options explicitly allowed by user for route calculations. By default no options are opt in.
    - occupantsNumber: Specifies the number of occupants in the vehicle, including driver, can affect the vehicle’s ability to use HOV/carpool restricted lanes. Shouldn’t be less than 1 or greater than 255. Defaults to 1.

    **Note:** This parameter has no effect unless HOV and/or HOT lane usage is enabled via <a href="sdk-for-ios-explore-structs-busoptions#sdk-for-ios-explore-s-7heresdk10BusOptionsV05allowC0AA05AllowC0Vvp">`BusOptions.allowOptions`</a> and such lanes are available in the selected country.

    - lastCharacterOfLicensePlate: Specifies the last character of a vehicle’s license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: “7”, when the license plate of a vehicle looks like “B-ET-182487”.

    If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

    - maxSpeedOnSegments: Segments with restriction on maximum baseSpeed.
    - busSpecifications: Detailed bus specifications such as dimensions and weight.

    **Note:** Some members of `bus_specifications` have limited value range.

    - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV22grossWeightInKilogramss5Int32VSgvp">`BusSpecifications.grossWeightInKilograms`</a> must not be negative.
    - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV19heightInCentimeterss5Int32VSgvp">`BusSpecifications.heightInCentimeters`</a> must be in the range \[0, 5000\].
    - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV18widthInCentimeterss5Int32VSgvp">`BusSpecifications.widthInCentimeters`</a> must be in the range \[0, 5000\].
    - <a href="sdk-for-ios-explore-structs-busspecifications#sdk-for-ios-explore-s-7heresdk17BusSpecificationsV19lengthInCentimeterss5Int32VSgvp">`BusSpecifications.lengthInCentimeters`</a> must be in the range \[0, 30000\]. The validation of the range is done in the method that takes `BusOptions` as parameter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(routeOptions: RouteOptions = RouteOptions(), textOptions: RouteTextOptions = RouteTextOptions(), avoidanceOptions: AvoidanceOptions = AvoidanceOptions(), tollOptions: TollOptions = TollOptions(), allowOptions: AllowOptions = AllowOptions(), occupantsNumber: Int32 = 1, lastCharacterOfLicensePlate: String? = nil, maxSpeedOnSegments: [MaxSpeedOnSegment] = [], busSpecifications: BusSpecifications = BusSpecifications())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions">TollOptions</a>
  - <a href="sdk-for-ios-explore-structs-allowoptions">AllowOptions</a>
  - <a href="sdk-for-ios-explore-structs-maxspeedonsegment">MaxSpeedOnSegment</a>
  - <a href="sdk-for-ios-explore-structs-busspecifications">BusSpecifications</a>

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

