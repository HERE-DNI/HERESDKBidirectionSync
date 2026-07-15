---
title: "ScooterOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-scooteroptions"
---

# ScooterOptions

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.") public struct ScooterOptions : Hashable
```

</pre>

</div>

</div>

All the options to specify how a scooter route should be calculated.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk14ScooterOptionsV05routeC0AA05RouteC0Vvp"></span>` `<span id="//apple_ref/swift/Property/routeOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV05routeC0AA05RouteC0Vvp" class="token"><code>routeOptions</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14ScooterOptionsV04textC0AA09RouteTextC0Vvp"></span>` `<span id="//apple_ref/swift/Property/textOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV04textC0AA09RouteTextC0Vvp" class="token"><code>textOptions</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14ScooterOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></span>` `<span id="//apple_ref/swift/Property/avoidanceOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV09avoidanceC0AA09AvoidanceC0Vvp" class="token"><code>avoidanceOptions</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14ScooterOptionsV04tollC0AA04TollC0Vvp"></span>` `<span id="//apple_ref/swift/Property/tollOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV04tollC0AA04TollC0Vvp" class="token"><code>tollOptions</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14ScooterOptionsV15occupantsNumbers5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/occupantsNumber" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV15occupantsNumbers5Int32Vvp" class="token"><code>occupantsNumber</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the number of occupants in the vehicle, including driver. Shouldn’t be less than 1 or greater than 255. Defaults to 1. This option is only relevant for Japan and will be ignored for other countries.

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

  ` `<span id="/s:7heresdk14ScooterOptionsV27lastCharacterOfLicensePlateSSSgvp"></span>` `<span id="//apple_ref/swift/Property/lastCharacterOfLicensePlate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV27lastCharacterOfLicensePlateSSSgvp" class="token"><code>lastCharacterOfLicensePlate</code></a>` `

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

  ` `<span id="/s:7heresdk14ScooterOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></span>` `<span id="//apple_ref/swift/Property/maxSpeedOnSegments" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp" class="token"><code>maxSpeedOnSegments</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Segments with restriction on maximum <a href="sdk-for-ios-navigate-structs-dynamicspeedinfo#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">`DynamicSpeedInfo.baseSpeedInMetersPerSecond`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxSpeedOnSegments: [MaxSpeedOnSegment]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14ScooterOptionsV12allowHighwaySbvp"></span>` `<span id="//apple_ref/swift/Property/allowHighway" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV12allowHighwaySbvp" class="token"><code>allowHighway</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. By default it is set to `false`. Note that there is a similar parameter in <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a>, to disallow highway usage, see <a href="sdk-for-ios-navigate-enums-roadfeatures#/s:7heresdk12RoadFeaturesO23controlledAccessHighwayyA2CmF">`RoadFeatures.controlledAccessHighway`</a>. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a <a href="sdk-for-ios-navigate-structs-sectionnotice">`SectionNotice`</a> will be provided in the related <a href="sdk-for-ios-navigate-classes-section">`Section`</a> to indicate that the highway usage restriction is violated on this route. A few examples:

  1 - If no avoidance option is set, and `allowHighway = false`, when no route is found without highway usage, a notice is received.

  2 - If no avoidance option is set, and `allowHighway = true`, when no route is found without highway usage, no notice is received.

  3 - If only `avoid[features] = controlledAccessHighway` is set, when no route is found without highway usage, a notice is received.

  4 - If both `avoid[features] = controlledAccessHighway` and `allowHighway = true` are set, when no route is found without highway usage, a notice is received.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var allowHighway: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14ScooterOptionsV28engineSizeInCubicCentimeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/engineSizeInCubicCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV28engineSizeInCubicCentimeterss5Int32VSgvp" class="token"><code>engineSizeInCubicCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535. Default value is `nil`, which means the scooter route calculation ignores all engine size limits on the road.

  **Note:** For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var engineSizeInCubicCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(routeOptions: textOptions: avoidanceOptions: tollOptions: occupantsNumber: lastCharacterOfLicensePlate: maxSpeedOnSegments: allowHighway: engineSizeInCubicCentimeters: )

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
    - occupantsNumber: Specifies the number of occupants in the vehicle, including driver. Shouldn’t be less than 1 or greater than 255. Defaults to 1. This option is only relevant for Japan and will be ignored for other countries.
    - lastCharacterOfLicensePlate: Specifies the last character of a vehicle’s license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: “7”, when the license plate of a vehicle looks like “B-ET-182487”.

    If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

    - maxSpeedOnSegments: Segments with restriction on maximum <a href="sdk-for-ios-navigate-structs-dynamicspeedinfo#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">`DynamicSpeedInfo.baseSpeedInMetersPerSecond`</a>.
    - allowHighway: Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. By default it is set to `false`. Note that there is a similar parameter in <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a>, to disallow highway usage, see <a href="sdk-for-ios-navigate-enums-roadfeatures#/s:7heresdk12RoadFeaturesO23controlledAccessHighwayyA2CmF">`RoadFeatures.controlledAccessHighway`</a>. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if <a href="sdk-for-ios-navigate-structs-scooteroptions#/s:7heresdk14ScooterOptionsV12allowHighwaySbvp">`allowHighway`</a> is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a <a href="sdk-for-ios-navigate-structs-sectionnotice">`SectionNotice`</a> will be provided in the related <a href="sdk-for-ios-navigate-classes-section">`Section`</a> to indicate that the highway usage restriction is violated on this route. A few examples:

    1 - If no avoidance option is set, and `allowHighway = false`, when no route is found without highway usage, a notice is received.

    2 - If no avoidance option is set, and `allowHighway = true`, when no route is found without highway usage, no notice is received.

    3 - If only `avoid[features] = controlledAccessHighway` is set, when no route is found without highway usage, a notice is received.

    4 - If both `avoid[features] = controlledAccessHighway` and `allowHighway = true` are set, when no route is found without highway usage, a notice is received.

    - engineSizeInCubicCentimeters: Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535. Default value is `nil`, which means the scooter route calculation ignores all engine size limits on the road.

    **Note:** For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( routeOptions : RouteOptions = RouteOptions (), textOptions : RouteTextOptions = RouteTextOptions (), avoidanceOptions : AvoidanceOptions = AvoidanceOptions (), tollOptions : TollOptions = TollOptions (), occupantsNumber : Int32 = 1 , lastCharacterOfLicensePlate : String ? = nil , maxSpeedOnSegments : [ MaxSpeedOnSegment ] = [], allowHighway : Bool = false , engineSizeInCubicCentimeters : Int32 ? = nil )
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

