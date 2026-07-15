---
title: "ElectricVehicleOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-electricvehicleoptions"
---

# ElectricVehicleOptions

<div class="declaration">

<div class="language">

``` highlight
public struct ElectricVehicleOptions : Hashable
```

</div>

</div>

These options define the parameters of the electric vehicle. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp"></span>` `<span id="//apple_ref/swift/Property/ensureReachability" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp" class="token"><code>ensureReachability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Ensure that the vehicle does not run out of energy along the way. Requires valid `battery_specifications`. It also requires that <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a> = <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF">`OptimizationMode.fastest`</a>, <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">`RouteOptions.speedCapInMetersPerSecond`</a> is not set, and <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a> is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations.

  **Note** An <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">`RoutingError.invalidParameter`</a> is generated when this option is set to `true` in case `sdk.routing.RoutingEngine.import_route` is called. Defaults to `false`.

  **Note** Not supported for offline routing.

  **Note** Only supported for car routing.

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

  ` `<span id="/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp"></span>` `<span id="//apple_ref/swift/Property/evMobilityServiceProviderPreferences" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp" class="token"><code>evMobilityServiceProviderPreferences</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html> An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used. **Note** Not yet supported for offline routing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evMobilityServiceProviderPreferences: EVMobilityServiceProviderPreferences
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22ElectricVehicleOptionsV25empiricalConsumptionModelAA09EmpiricalfG0VSgvp"></span>` `<span id="//apple_ref/swift/Property/empiricalConsumptionModel" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV25empiricalConsumptionModelAA09EmpiricalfG0VSgvp" class="token"><code>empiricalConsumptionModel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the empirical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var empiricalConsumptionModel: EmpiricalConsumptionModel?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22ElectricVehicleOptionsV24physicalConsumptionModelAA08PhysicalfG0VSgvp"></span>` `<span id="//apple_ref/swift/Property/physicalConsumptionModel" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV24physicalConsumptionModelAA08PhysicalfG0VSgvp" class="token"><code>physicalConsumptionModel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the physical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var physicalConsumptionModel: PhysicalConsumptionModel?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22ElectricVehicleOptionsV21batterySpecificationsAA07BatteryF0VSgvp"></span>` `<span id="//apple_ref/swift/Property/batterySpecifications" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV21batterySpecificationsAA07BatteryF0VSgvp" class="token"><code>batterySpecifications</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parameters that describe the electric vehicle’s battery. By default, it is set to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var batterySpecifications: BatterySpecifications?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(ensureReachability: evMobilityServiceProviderPreferences: empiricalConsumptionModel: physicalConsumptionModel: batterySpecifications: )

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

    - ensureReachability: Ensure that the vehicle does not run out of energy along the way. Requires valid `battery_specifications`. It also requires that <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a> = <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF">`OptimizationMode.fastest`</a>, <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">`RouteOptions.speedCapInMetersPerSecond`</a> is not set, and <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a> is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations.

    **Note** An <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">`RoutingError.invalidParameter`</a> is generated when this option is set to `true` in case `sdk.routing.RoutingEngine.import_route` is called. Defaults to `false`.

    **Note** Not supported for offline routing.

    **Note** Only supported for car routing.

    - evMobilityServiceProviderPreferences: Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html> An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used. **Note** Not yet supported for offline routing.
    - empiricalConsumptionModel: Defines the empirical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.
    - physicalConsumptionModel: Defines the physical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.
    - batterySpecifications: Parameters that describe the electric vehicle’s battery. By default, it is set to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( ensureReachability : Bool = false , evMobilityServiceProviderPreferences : EVMobilityServiceProviderPreferences = EVMobilityServiceProviderPreferences (), empiricalConsumptionModel : EmpiricalConsumptionModel ? = nil , physicalConsumptionModel : PhysicalConsumptionModel ? = nil , batterySpecifications : BatterySpecifications ? = nil )
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

