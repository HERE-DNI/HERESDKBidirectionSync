---
title: "EVCarOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-evcaroptions"
---

# EVCarOptions

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")
public struct EVCarOptions : Hashable
```

</div>

</div>

All the options to specify how a route for an electric car should be calculated. At minimum, a valid <a href="sdk-for-ios-explore-structs-evconsumptionmodel">`EVConsumptionModel`</a> must be set or the route calculation will fail.\
Note: <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV18ensureReachabilitySbvp">`EVCarOptions.ensureReachability`</a> must be `true` to make sure that all stopovers are reachable. For this, charging stations may be added to the route. If <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV18ensureReachabilitySbvp">`EVCarOptions.ensureReachability`</a> is true, you need to specify the required route options and battery specifications that include the current charge level of the battery (<a href="sdk-for-ios-explore-structs-batteryspecifications#sdk-for-ios-explore-s-7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp">`BatterySpecifications.initialChargeInKilowattHours`</a>). See the parameter description below for more details.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05routeC0AA05RouteC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05routeC0AA05RouteC0Vvp" class="token"><code>routeOptions</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV04textC0AA09RouteTextC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-textOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV04textC0AA09RouteTextC0Vvp" class="token"><code>textOptions</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-avoidanceOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV09avoidanceC0AA09AvoidanceC0Vvp" class="token"><code>avoidanceOptions</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV04tollC0AA04TollC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tollOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV04tollC0AA04TollC0Vvp" class="token"><code>tollOptions</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-allowOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp" class="token"><code>allowOptions</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV15occupantsNumbers5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-occupantsNumber" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV15occupantsNumbers5Int32Vvp" class="token"><code>occupantsNumber</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the number of occupants in the vehicle, including driver, can affect the vehicle’s ability to use HOV/carpool restricted lanes. Shouldn’t be less than 1 or greater than 255. Defaults to 1.

  **Note:** This parameter has no effect unless HOV and/or HOT lane usage is enabled via <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp">`EVCarOptions.allowOptions`</a> and such lanes are available in the selected country.

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV27lastCharacterOfLicensePlateSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastCharacterOfLicensePlate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV27lastCharacterOfLicensePlateSSSgvp" class="token"><code>lastCharacterOfLicensePlate</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maxSpeedOnSegments" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp" class="token"><code>maxSpeedOnSegments</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Segments with restriction on maximum <a href="sdk-for-ios-explore-structs-dynamicspeedinfo#sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">`DynamicSpeedInfo.baseSpeedInMetersPerSecond`</a>.

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

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV18ensureReachabilitySbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-ensureReachability" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV18ensureReachabilitySbvp" class="token"><code>ensureReachability</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Ensure that the vehicle does not run out of energy along the way. Requires valid <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp">`EVCarOptions.batterySpecifications`</a>. It also requires that <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a> = <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO7fastestyA2CmF">`OptimizationMode.fastest`</a>, <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">`RouteOptions.speedCapInMetersPerSecond`</a> is not set, and <a href="sdk-for-ios-explore-structs-avoidanceoptions">`AvoidanceOptions`</a> is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.EVCarOptions.ensure_reachability\] is set to `true` in case \[sdk.routing.RoutingEngine.import_route\] is called. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ensureReachability: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV16consumptionModelAA013EVConsumptionE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-consumptionModel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV16consumptionModelAA013EVConsumptionE0Vvp" class="token"><code>consumptionModel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var consumptionModel: EVConsumptionModel
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evconsumptionmodel">EVConsumptionModel</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-batterySpecifications" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp" class="token"><code>batterySpecifications</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parameters that describe the electric vehicle’s battery.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var batterySpecifications: BatterySpecifications
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-batteryspecifications">BatterySpecifications</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV17carSpecificationsAA03CarE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-carSpecifications" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV17carSpecificationsAA03CarE0Vvp" class="token"><code>carSpecifications</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Detailed car specifications such as dimensions and weight.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var carSpecifications: CarSpecifications
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-carspecifications">CarSpecifications</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityfgH0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-evMobilityServiceProviderPreferences" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityfgH0Vvp" class="token"><code>evMobilityServiceProviderPreferences</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html> An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evMobilityServiceProviderPreferences: EVMobilityServiceProviderPreferences
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments18ensureReachability16consumptionModel21batterySpecifications03carY036evMobilityServiceProviderPreferencesAcA05RouteC0V_AA09RouteTextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGSbAA013EVConsumptionW0VAA07BatteryY0VAA03CarY0VAA36EVMobilityServiceProviderPreferencesVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-routeOptions-textOptions-avoidanceOptions-tollOptions-allowOptions-occupantsNumber-lastCharacterOfLicensePlate-maxSpeedOnSegments-ensureReachability-consumptionModel-batterySpecifications-carSpecifications-evMobilityServiceProviderPreferences" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments18ensureReachability16consumptionModel21batterySpecifications03carY036evMobilityServiceProviderPreferencesAcA05RouteC0V_AA09RouteTextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGSbAA013EVConsumptionW0VAA07BatteryY0VAA03CarY0VAA36EVMobilityServiceProviderPreferencesVtcfc" class="token"><code>init(routeOptions:</code><wbr></wbr><code>textOptions:</code><wbr></wbr><code>avoidanceOptions:</code><wbr></wbr><code>tollOptions:</code><wbr></wbr><code>allowOptions:</code><wbr></wbr><code>occupantsNumber:</code><wbr></wbr><code>lastCharacterOfLicensePlate:</code><wbr></wbr><code>maxSpeedOnSegments:</code><wbr></wbr><code>ensureReachability:</code><wbr></wbr><code>consumptionModel:</code><wbr></wbr><code>batterySpecifications:</code><wbr></wbr><code>carSpecifications:</code><wbr></wbr><code>evMobilityServiceProviderPreferences:</code><wbr></wbr><code>)</code></a> 

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

    **Note:** This parameter has no effect unless HOV and/or HOT lane usage is enabled via <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp">`EVCarOptions.allowOptions`</a> and such lanes are available in the selected country.

    - lastCharacterOfLicensePlate: Specifies the last character of a vehicle’s license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: “7”, when the license plate of a vehicle looks like “B-ET-182487”.

    If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

    - maxSpeedOnSegments: Segments with restriction on maximum <a href="sdk-for-ios-explore-structs-dynamicspeedinfo#sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">`DynamicSpeedInfo.baseSpeedInMetersPerSecond`</a>.
    - ensureReachability: Ensure that the vehicle does not run out of energy along the way. Requires valid <a href="sdk-for-ios-explore-structs-evcaroptions#sdk-for-ios-explore-s-7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp">`EVCarOptions.batterySpecifications`</a>. It also requires that <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a> = <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO7fastestyA2CmF">`OptimizationMode.fastest`</a>, <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">`RouteOptions.speedCapInMetersPerSecond`</a> is not set, and <a href="sdk-for-ios-explore-structs-avoidanceoptions">`AvoidanceOptions`</a> is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.EVCarOptions.ensure_reachability\] is set to `true` in case \[sdk.routing.RoutingEngine.import_route\] is called. Defaults to `false`.
    - consumptionModel: Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.
    - batterySpecifications: Parameters that describe the electric vehicle’s battery.
    - carSpecifications: Detailed car specifications such as dimensions and weight.
    - evMobilityServiceProviderPreferences: Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html> An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(routeOptions: RouteOptions = RouteOptions(), textOptions: RouteTextOptions = RouteTextOptions(), avoidanceOptions: AvoidanceOptions = AvoidanceOptions(), tollOptions: TollOptions = TollOptions(), allowOptions: AllowOptions = AllowOptions(), occupantsNumber: Int32 = 1, lastCharacterOfLicensePlate: String? = nil, maxSpeedOnSegments: [MaxSpeedOnSegment] = [], ensureReachability: Bool = false, consumptionModel: EVConsumptionModel = EVConsumptionModel(), batterySpecifications: BatterySpecifications = BatterySpecifications(), carSpecifications: CarSpecifications = CarSpecifications(), evMobilityServiceProviderPreferences: EVMobilityServiceProviderPreferences = EVMobilityServiceProviderPreferences())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions">TollOptions</a>
  - <a href="sdk-for-ios-explore-structs-allowoptions">AllowOptions</a>
  - <a href="sdk-for-ios-explore-structs-maxspeedonsegment">MaxSpeedOnSegment</a>
  - <a href="sdk-for-ios-explore-structs-evconsumptionmodel">EVConsumptionModel</a>
  - <a href="sdk-for-ios-explore-structs-batteryspecifications">BatterySpecifications</a>
  - <a href="sdk-for-ios-explore-structs-carspecifications">CarSpecifications</a>
  - <a href="sdk-for-ios-explore-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a>

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

