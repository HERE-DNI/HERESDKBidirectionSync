---
title: "RouteOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-routeoptions"
---

# RouteOptions

<div class="declaration">

<div class="language">

``` highlight
public struct RouteOptions : Hashable
```

</div>

</div>

The options to specify how the route will be calculated.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp"></span>` `<span id="//apple_ref/swift/Property/optimizationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp" class="token"><code>optimizationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-ios-explore-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF">`OptimizationMode.fastest`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var optimizationMode: OptimizationMode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/alternatives" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp" class="token"><code>alternatives</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var alternatives: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/departureTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp" class="token"><code>departureTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">`RouteOptions.trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

  **Note**:

  - Both departure time and <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">`RouteOptions.arrivalTime`</a> cannot be set at the same time.
  - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var departureTime: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/arrivalTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp" class="token"><code>arrivalTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">`RouteOptions.trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

  **Note**:

  - Both <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">`RouteOptions.departureTime`</a> and arrival time cannot be set at the same time.
  - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var arrivalTime: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/speedCapInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp" class="token"><code>speedCapInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a> and <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO7scooteryA2CmF">`TransportMode.scooter`</a> transport modes. For car, truck and scooter transport modes, it will affect <a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8durationSdvp">`Route.duration`</a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `nil`, which means that no speed cap is set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedCapInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV06enableB6HandleSbvp"></span>` `<span id="//apple_ref/swift/Property/enableRouteHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp" class="token"><code>enableRouteHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether the resulting route should contain a <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a>. Defaults to `false`. Note that a <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a> generated by the online <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a> is not compatible with the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> and vice versa.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enableRouteHandle: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp"></span>` `<span id="//apple_ref/swift/Property/trafficOptimizationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp" class="token"><code>trafficOptimizationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-ios-explore-enums-trafficoptimizationmode#/s:7heresdk23TrafficOptimizationModeO13timeDependentyA2CmF">`TrafficOptimizationMode.timeDependent`</a>, which enables traffic-aware routing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficOptimizationMode: TrafficOptimizationMode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV11enableTollsSbvp"></span>` `<span id="//apple_ref/swift/Property/enableTolls" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV11enableTollsSbvp" class="token"><code>enableTolls</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether the resulting route <a href="sdk-for-ios-explore-classes-section#/s:7heresdk7SectionC5tollsSayAA4TollVGvp">`Section.tolls`</a> properties should contain tolls data. Defaults to `false`.

  **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

  **Note:** For users of the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is only available for the Navigate license. For users of the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a> the feature is stable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enableTolls: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV22optimizeWaypointsOrderSbvp"></span>` `<span id="//apple_ref/swift/Property/optimizeWaypointsOrder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV22optimizeWaypointsOrderSbvp" class="token"><code>optimizeWaypointsOrder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether the order of waypoints that is passed to

      calculateRoute()

  should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-ios-explore-enums-optimizationmode">`OptimizationMode`</a>. The starting and destination <a href="sdk-for-ios-explore-structs-waypoint">`Waypoint`</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn’t affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see <a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">`Route.sections`</a>, <a href="sdk-for-ios-explore-classes-section#/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp">`Section.departurePlace`</a>, <a href="sdk-for-ios-explore-classes-section#/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp">`Section.arrivalPlace`</a>, <a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp">`RoutePlace.waypointIndex`</a>). Currently, the waypoints order optimization is available only when using the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> (only available for the Navigate license). Defaults to `false`.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var optimizeWaypointsOrder: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12RouteOptionsV06enableB6LabelsSbvp"></span>` `<span id="//apple_ref/swift/Property/enableRouteLabels" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV06enableB6LabelsSbvp" class="token"><code>enableRouteLabels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enableRouteLabels: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(optimizationMode: alternatives: departureTime: arrivalTime: speedCapInMetersPerSecond: enableRouteHandle: trafficOptimizationMode: enableTolls: optimizeWaypointsOrder: enableRouteLabels: )

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

    - optimizationMode: The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-ios-explore-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF">`OptimizationMode.fastest`</a>.
    - alternatives: Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.
    - departureTime: Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">`RouteOptions.trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">`RouteOptions.arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00
      - arrivalTime: Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">`RouteOptions.trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">`RouteOptions.departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00
      - speedCapInMetersPerSecond: Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a> and <a href="sdk-for-ios-explore-enums-transportmode#/s:7heresdk13TransportModeO7scooteryA2CmF">`TransportMode.scooter`</a> transport modes. For car, truck and scooter transport modes, it will affect <a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8durationSdvp">`Route.duration`</a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `nil`, which means that no speed cap is set.
      - enableRouteHandle: A flag that indicates whether the resulting route should contain a <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a>. Defaults to `false`. Note that a <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a> generated by the online <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a> is not compatible with the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> and vice versa.
      - trafficOptimizationMode: The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-ios-explore-enums-trafficoptimizationmode#/s:7heresdk23TrafficOptimizationModeO13timeDependentyA2CmF">`TrafficOptimizationMode.timeDependent`</a>, which enables traffic-aware routing.
      - enableTolls: A flag that indicates whether the resulting route <a href="sdk-for-ios-explore-classes-section#/s:7heresdk7SectionC5tollsSayAA4TollVGvp">`Section.tolls`</a> properties should contain tolls data. Defaults to `false`.

    **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

    **Note:** For users of the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is only available for the Navigate license. For users of the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a> the feature is stable.

    - optimizeWaypointsOrder: A flag that indicates whether the order of waypoints that is passed to

          calculateRoute()

      should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-ios-explore-enums-optimizationmode">`OptimizationMode`</a>. The starting and destination <a href="sdk-for-ios-explore-structs-waypoint">`Waypoint`</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn’t affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see <a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">`Route.sections`</a>, <a href="sdk-for-ios-explore-classes-section#/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp">`Section.departurePlace`</a>, <a href="sdk-for-ios-explore-classes-section#/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp">`Section.arrivalPlace`</a>, <a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp">`RoutePlace.waypointIndex`</a>). Currently, the waypoints order optimization is available only when using the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> (only available for the Navigate license). Defaults to `false`.

    - enableRouteLabels: Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( optimizationMode : OptimizationMode = OptimizationMode . fastest , alternatives : Int32 = 0 , departureTime : Date ? = nil , arrivalTime : Date ? = nil , speedCapInMetersPerSecond : Double ? = nil , enableRouteHandle : Bool = false , trafficOptimizationMode : TrafficOptimizationMode = TrafficOptimizationMode . timeDependent , enableTolls : Bool = false , optimizeWaypointsOrder : Bool = false , enableRouteLabels : Bool = false )
  ```

  </pre>

  </div>

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

