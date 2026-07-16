---
title: "RoutingOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-routingoptions"
---

# RoutingOptions

<div class="declaration">

<div class="language">

``` highlight
public struct RoutingOptions : Hashable
```

</div>

</div>

The options defines how a route should be calculated.

The options are used for all transport modes and engines.

\*\* Electric vehicle specific requirements \*\* Electric vehicle consumption are estimated when at least one consumption model is defined. Currently two models are supported:

- PhysicalConsumptionModel Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:
  - <a href="sdk-for-ios-navigate-structs-vehiclespecification#sdk-for-ios-navigate-s-7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#sdk-for-ios-navigate-s-7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">`RoutingOptions.transportSpecification`</a>
  - Additionally <a href="sdk-for-ios-navigate-structs-waypoint#sdk-for-ios-navigate-s-7heresdk8WaypointV30currentWeightChangeInKilogramss5Int32VSgvp">`Waypoint.currentWeightChangeInKilograms`</a> can be defined.
- EmpiricalConsumptionModel

By setting <a href="sdk-for-ios-navigate-structs-electricvehicleoptions#sdk-for-ios-navigate-s-7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp">`ElectricVehicleOptions.ensureReachability`</a> the <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> inserts additional charging stations to reach the waypoints. This feature requires setting the <a href="sdk-for-ios-navigate-structs-batteryspecifications">`BatterySpecifications`</a>. By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints. See the parameter description below for more details.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-transportSpecification" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp" class="token"><code>transportSpecification</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen. **Notes:**

  - The transport mode <a href="sdk-for-ios-navigate-enums-transportmode#sdk-for-ios-navigate-s-7heresdk13TransportModeO13publicTransityA2CmF">`TransportMode.publicTransit`</a> is not supported.
  - By default all vehicle specifications from `RoutingOptions.transportSpecification` are set to `nil` and the <a href="sdk-for-ios-navigate-structs-transportspecification#sdk-for-ios-navigate-s-7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a> from `RoutingOptions.transportSpecification` is set to <a href="sdk-for-ios-navigate-enums-transportmode#sdk-for-ios-navigate-s-7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>.
  - A route can be calculated with only the <a href="sdk-for-ios-navigate-structs-transportspecification#sdk-for-ios-navigate-s-7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a> from `RoutingOptions.transportSpecification` set.
  - It is highly recommended to define the <a href="sdk-for-ios-navigate-enums-truckcategory">`TruckCategory`</a> that is being used in <a href="sdk-for-ios-navigate-structs-vehiclespecification#sdk-for-ios-navigate-s-7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">`VehicleSpecification.truckCategory`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#sdk-for-ios-navigate-s-7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> from `RoutingOptions.transportSpecification`, if the <a href="sdk-for-ios-navigate-structs-transportspecification#sdk-for-ios-navigate-s-7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">`TransportSpecification.transportMode`</a> from `RoutingOptions.transportSpecification` is set to <a href="sdk-for-ios-navigate-enums-transportmode#sdk-for-ios-navigate-s-7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>.
  - The <a href="sdk-for-ios-navigate-structs-vehiclespecification#sdk-for-ios-navigate-s-7heresdk20VehicleSpecificationV9occupancys5Int32VSgvp">`VehicleSpecification.occupancy`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#sdk-for-ios-navigate-s-7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">`TransportSpecification.vehicleSpecification`</a> won’t have effect if HOV and/or HOT lane usage is not allowed using <a href="sdk-for-ios-navigate-structs-evtruckoptions#sdk-for-ios-navigate-s-7heresdk14EVTruckOptionsV05allowC0AA05AllowC0Vvp">`EVTruckOptions.allowOptions`</a>.
  - The <a href="sdk-for-ios-navigate-structs-pedestrianspecification#sdk-for-ios-navigate-s-7heresdk23PedestrianSpecificationV29walkingSpeedInMetersPerSecondSdvp">`PedestrianSpecification.walkingSpeedInMetersPerSecond`</a> from <a href="sdk-for-ios-navigate-structs-transportspecification#sdk-for-ios-navigate-s-7heresdk22TransportSpecificationV010pedestrianC0AA010PedestrianC0VSgvp">`TransportSpecification.pedestrianSpecification`</a> if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking along the route. The provided value must be in the range \[0.5, 2.0\]. When the value is outside this range, an invalid parameter error is raised. Refer to <a href="sdk-for-ios-navigate-enums-routingerror">`RoutingError`</a> for details. The default speed is 1 meter per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transportSpecification: TransportSpecification
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV05routeC0AA05RouteC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-routeOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV05routeC0AA05RouteC0Vvp" class="token"><code>routeOptions</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-routeoptions">RouteOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV04textC0AA09RouteTextC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-textOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV04textC0AA09RouteTextC0Vvp" class="token"><code>textOptions</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-routetextoptions">RouteTextOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-avoidanceOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV09avoidanceC0AA09AvoidanceC0Vvp" class="token"><code>avoidanceOptions</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-avoidanceoptions">AvoidanceOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV05allowC0AA05AllowC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-allowOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV05allowC0AA05AllowC0Vvp" class="token"><code>allowOptions</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-allowoptions">AllowOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV04tollC0AA04TollC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tollOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV04tollC0AA04TollC0Vvp" class="token"><code>tollOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type. **Note** Not used for offline calculations.

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

  - <a href="sdk-for-ios-navigate-structs-tolloptions">TollOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maxSpeedOnSegments" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp" class="token"><code>maxSpeedOnSegments</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Segments with restriction on maximum <a href="sdk-for-ios-navigate-structs-dynamicspeedinfo#sdk-for-ios-navigate-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">`DynamicSpeedInfo.baseSpeedInMetersPerSecond`</a>. **Note** Not used for offline calculations.

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

  - <a href="sdk-for-ios-navigate-structs-maxspeedonsegment">MaxSpeedOnSegment</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV02evC0AA015ElectricVehicleC0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-evOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV02evC0AA015ElectricVehicleC0VSgvp" class="token"><code>evOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability. When no EV options are defined an internal combustion engine is assumed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var evOptions: ElectricVehicleOptions?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-electricvehicleoptions">ElectricVehicleOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV22transportSpecification05routeC004textC009avoidanceC005allowC004tollC018maxSpeedOnSegments02evC0AcA09TransportE0V_AA05RouteC0VAA0q4TextC0VAA09AvoidanceC0VAA05AllowC0VAA04TollC0VSayAA03MaxlM7SegmentVGAA015ElectricVehicleC0VSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-transportSpecification-routeOptions-textOptions-avoidanceOptions-allowOptions-tollOptions-maxSpeedOnSegments-evOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV22transportSpecification05routeC004textC009avoidanceC005allowC004tollC018maxSpeedOnSegments02evC0AcA09TransportE0V_AA05RouteC0VAA0q4TextC0VAA09AvoidanceC0VAA05AllowC0VAA04TollC0VSayAA03MaxlM7SegmentVGAA015ElectricVehicleC0VSgtcfc" class="token"><code>init(transportSpecification:</code><wbr></wbr><code>routeOptions:</code><wbr></wbr><code>textOptions:</code><wbr></wbr><code>avoidanceOptions:</code><wbr></wbr><code>allowOptions:</code><wbr></wbr><code>tollOptions:</code><wbr></wbr><code>maxSpeedOnSegments:</code><wbr></wbr><code>evOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(transportSpecification: TransportSpecification = TransportSpecification(), routeOptions: RouteOptions = RouteOptions(), textOptions: RouteTextOptions = RouteTextOptions(), avoidanceOptions: AvoidanceOptions = AvoidanceOptions(), allowOptions: AllowOptions = AllowOptions(), tollOptions: TollOptions = TollOptions(), maxSpeedOnSegments: [MaxSpeedOnSegment] = [], evOptions: ElectricVehicleOptions? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-transportspecification">TransportSpecification</a>
  - <a href="sdk-for-ios-navigate-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-navigate-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-navigate-structs-avoidanceoptions">AvoidanceOptions</a>
  - <a href="sdk-for-ios-navigate-structs-allowoptions">AllowOptions</a>
  - <a href="sdk-for-ios-navigate-structs-tolloptions">TollOptions</a>
  - <a href="sdk-for-ios-navigate-structs-maxspeedonsegment">MaxSpeedOnSegment</a>
  - <a href="sdk-for-ios-navigate-structs-electricvehicleoptions">ElectricVehicleOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV33fromDefaultParameterConfigurationACyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-fromDefaultParameterConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingoptions#sdk-for-ios-navigate-s-7heresdk14RoutingOptionsV33fromDefaultParameterConfigurationACyFZ" class="token"><code>fromDefaultParameterConfiguration()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the default configuration for the transport specification selected in <a href="sdk-for-ios-navigate-structs-parameterconfiguration#sdk-for-ios-navigate-s-7heresdk22ParameterConfigurationV22transportSpecificationAA09TransportE0Vvp">`ParameterConfiguration.transportSpecification`</a> from <a href="sdk-for-ios-navigate-classes-sdknativeengine#sdk-for-ios-navigate-s-7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ">`SDKNativeEngine.parameterConfig`</a>. **Note** By default, the \[sdk.core.ParameterConfiguration.transport_specification\] from \[sdk.core.engine.SDKNativeEngine.parameter_config\] will return a valid <a href="sdk-for-ios-navigate-structs-transportspecification">`TransportSpecification`</a> object with the \[sdk.transport.TransportSpecification.transport_mode\] set to <a href="sdk-for-ios-navigate-enums-transportmode#sdk-for-ios-navigate-s-7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromDefaultParameterConfiguration() -> RoutingOptions
  ```

  </div>

  </div>

  <div>

  #### Return Value

  The `RoutingOptions` object with the default configuration for the transport specification selected in <a href="sdk-for-ios-navigate-structs-parameterconfiguration#sdk-for-ios-navigate-s-7heresdk22ParameterConfigurationV22transportSpecificationAA09TransportE0Vvp">`ParameterConfiguration.transportSpecification`</a> from <a href="sdk-for-ios-navigate-classes-sdknativeengine#sdk-for-ios-navigate-s-7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ">`SDKNativeEngine.parameterConfig`</a>.

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

