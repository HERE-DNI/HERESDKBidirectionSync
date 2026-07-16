---
title: "OfflineRoutingEngine Class Reference"
slug: "sdk-for-ios-explore-classes-offlineroutingengine"
---

# OfflineRoutingEngine

<div class="declaration">

<div class="language">

``` highlight
public class OfflineRoutingEngine : RoutingProtocol
```

``` highlight
extension OfflineRoutingEngine: NativeBase
```

``` highlight
extension OfflineRoutingEngine: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-explore-protocols-routingprotocol">RoutingProtocol</a>

</div>

Use this class to calculate a route offline from A to B with a number of waypoints in between.

Route calculation is done asynchronously, and requires map data that is available offline. This can be temporarily cached map data or downloaded offline map data stored in the persisted storage via <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a>. Note that when using the cache there is a risk of missing data and this may reduce the overall quality of the route or can result in a <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF">`RoutingError.noRouteFound`</a> error.

The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data, but it does not contain traffic information.

Unlike the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a> (which requires an online connection), this engine allows to use an unlimited number of waypoints.

As an alternative to this engine, consider to use the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a> for online route calculations to get fresher traffic, maneuver, route handles and street information, and to use a more elaborate algorithms to calculate the fastest route.

For offline bus routing, enable “OFFLINE_BUS_ROUTING” as feature configuration. For more details, please look at <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a>. If this feature is not enabled, the engine may not be able to find bus routes.

**Note:** EV routing is available when calculating a route using the <a href="sdk-for-ios-explore-structs-routingoptions">`RoutingOptions`</a>, by setting the <a href="sdk-for-ios-explore-structs-routingoptions#sdk-for-ios-explore-s-7heresdk14RoutingOptionsV02evC0AA015ElectricVehicleC0VSgvp">`RoutingOptions.evOptions`</a>.

**Note:** Traffic related information is completely excluded. No historic traffic patterns are taking into consideration for the ETA. Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e. the road may pass through such road. Only seasonal road closures are considered based on the departure time, if given. Traffic information is only considered for online route calculation with the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a>.

**Note:** Route handles produced by this engine are not compatible with those created by the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a>. Importing, refreshing, or returning to a route via a route handle is supported only when the route was calculated with the same engine. However, this engine supports returning to a route calculated with the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a> when the route object is provided.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineCACyKcfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineCyAcA09SDKNativeD0CKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineCyAcA09SDKNativeD0CKcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of OfflineRoutingEngine.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ sdkEngine: SDKNativeEngine) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>An SDKEngine instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_-options" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVtKcfc" class="token"><code>init(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of OfflineRoutingEngine.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ sdkEngine: SDKNativeEngine, options: OfflineRoutingEngineOptions) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-structs-offlineroutingengineoptions">OfflineRoutingEngineOptions</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>An SDKEngine instance.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Options to configure offline routing engine.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC19trafficDataProviderAA07TrafficfG0CSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficDataProvider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC19trafficDataProviderAA07TrafficfG0CSgvp" class="token"><code>trafficDataProvider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The traffic data provider that gets internal traffic information considering in routing. If the traffic data provider is `nil`, traffic is not considered in routing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficDataProvider: TrafficDataProvider? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk19TrafficDataProviderC">TrafficDataProvider</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], options: RoutingOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Options describing routing options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-carOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>carOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], carOptions: CarOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-caroptions">CarOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>carOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for car route calculation, along with common route options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-pedestrianOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>pedestrianOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], pedestrianOptions: PedestrianOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianoptions">PedestrianOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>pedestrianOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for pedestrian route calculation, along with common route options. Note that <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for pedestrians and converted to <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-truckOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>truckOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], truckOptions: TruckOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-truckoptions">TruckOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>truckOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for truck route calculation, along with common route options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-scooterOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>scooterOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], scooterOptions: ScooterOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-scooteroptions">ScooterOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scooterOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for scooter route calculation, along with common route options. Note that <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for scooters and converted to <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-bicycleOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>bicycleOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], bicycleOptions: BicycleOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-bicycleoptions">BicycleOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bicycleOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for bicycle route calculation, along with common route options. Note that <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for bicycles and converted to <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-taxiOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>taxiOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], taxiOptions: TaxiOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-taxioptions">TaxiOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>taxiOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for taxi route calculation, along with common route options. Note that <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for taxis and converted to <a href="sdk-for-ios-explore-enums-optimizationmode#sdk-for-ios-explore-s-7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-evCarOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>evCarOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], evCarOptions: EVCarOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-evcaroptions">EVCarOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>evCarOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for an electric car route calculation, along with common route options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-evTruckOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>evTruckOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], evTruckOptions: EVTruckOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-evtruckoptions">EVTruckOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>evTruckOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for an electric truck route calculation, along with common route options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-busOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>busOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], busOptions: BusOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-busoptions">BusOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>busOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for a bus route calculation, along with common route options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivateiJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateRoute-with-privateBusOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivateiJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(with:</code><wbr></wbr><code>privateBusOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.")
  @discardableResult
  public func calculateRoute(with waypoints: [Waypoint], privateBusOptions: PrivateBusOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-structs-privatebusoptions">PrivateBusOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>privateBusOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for a private bus route calculation, along with common route options.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters10completionAA10TaskHandle_pAA0G0C_AA8WaypointVs5Int32VAOyAA0C5ErrorOSg_SayAKGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-returnToRoute-_-startingPoint-lastTraveledSectionIndex-traveledDistanceOnLastSectionInMeters-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters10completionAA10TaskHandle_pAA0G0C_AA8WaypointVs5Int32VAOyAA0C5ErrorOSg_SayAKGSgtctF" class="token"><code>returnToRoute(_:</code><wbr></wbr><code>startingPoint:</code><wbr></wbr><code>lastTraveledSectionIndex:</code><wbr></wbr><code>traveledDistanceOnLastSectionInMeters:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.

  **Note:** Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV12alternativess5Int32Vvp">`RouteOptions.alternatives`</a>, <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">`RouteOptions.arrivalTime`</a>, and <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a>. Most route options are only applied to the newly calculated part back to the route.

  An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too.

  Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route.

  A typical use case is to await at least 3 <a href="sdk-for-ios-explore-structs-routedeviation">`RouteDeviation`</a> events before calling this method.

  - Or alternatively, wait at least 10 seconds after getting the first deviation event.
  - On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time.
  - Optionally, it may make sense to verify if the vehicle was ever following the route by checking if <a href="sdk-for-ios-explore-structs-routedeviation#sdk-for-ios-explore-s-7heresdk14RouteDeviationV014lastLocationOnB0AA09NavigableE0VSgvp">`RouteDeviation.lastLocationOnRoute`</a> is set.

  Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the “Handle route deviations” section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func returnToRoute(_ route: Route, startingPoint: Waypoint, lastTraveledSectionIndex: Int32, traveledDistanceOnLastSectionInMeters: Int32, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-route">Route</a>
  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>route</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-explore-classes-route"><code>Route</code></a> calculated using the online or offline route engine. For the offline case, It should not contain an indoor <a href="sdk-for-ios-explore-classes-section"><code>Section</code></a> as such routes will fail. For the online case, it should have <a href="sdk-for-ios-explore-structs-routehandle"><code>RouteHandle</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>startingPoint</code></em><code> </code></td>
  <td><div>
  <p>The current location, for example, provided by a <a href="sdk-for-ios-explore-structs-routedeviation"><code>RouteDeviation</code></a> event. The waypoint needs to be of type <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO8stopoveryA2CmF"><code>WaypointType.stopover</code></a>. Otherwise, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO16invalidParameteryA2CmF"><code>RoutingError.invalidParameter</code></a> error is generated.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>lastTraveledSectionIndex</code></em><code> </code></td>
  <td><div>
  <p>Indicates the index of the last traveled route section. Traveled part of the route won’t be reused.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>traveledDistanceOnLastSectionInMeters</code></em><code> </code></td>
  <td><div>
  <p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC12refreshRoute0eF10Parameters14routingOptions10completionAA10TaskHandle_pAA07RefreshfG0V_AA0cI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-refreshRoute-refreshRouteParameters-routingOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC12refreshRoute0eF10Parameters14routingOptions10completionAA10TaskHandle_pAA07RefreshfG0V_AA0cI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>refreshRoute(refreshRouteParameters:</code><wbr></wbr><code>routingOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a>, updating the starting point and route metadata based on <a href="sdk-for-ios-explore-structs-routingoptions">`RoutingOptions`</a>. The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func refreshRoute(refreshRouteParameters: RefreshRouteParameters, routingOptions: RoutingOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-refreshrouteparameters">RefreshRouteParameters</a>
  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>refreshRouteParameters</code></em><code> </code></td>
  <td><div>
  <p>The parameters used to refresh the route</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routingOptions</code></em><code> </code></td>
  <td><div>
  <p>The options define the vehicle and route options used to calculate the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC11importRoute11routeHandle07refreshF7Options10completionAA04TaskH0_pAA0fH0V_AA07RefreshfJ0CyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-importRoute-routeHandle-refreshRouteOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC11importRoute11routeHandle07refreshF7Options10completionAA04TaskH0_pAA0fH0V_AA07RefreshfJ0CyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>importRoute(routeHandle:</code><wbr></wbr><code>refreshRouteOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously recreates a route from the <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a> provided, i.e. refreshes a previously calculated route, with the specified <a href="sdk-for-ios-explore-classes-refreshrouteoptions">`RefreshRouteOptions`</a>.

  A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` method with RoutingOptions parameter instead.")
  @discardableResult
  public func importRoute(routeHandle: RouteHandle, refreshRouteOptions: RefreshRouteOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-explore-classes-refreshrouteoptions">RefreshRouteOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>refreshRouteOptions</code></em><code> </code></td>
  <td><div>
  <p>Options to import the route from handle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC11importRoute11routeHandle7options10completionAA04TaskH0_pAA0fH0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-importRoute-routeHandle-options-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC11importRoute11routeHandle7options10completionAA04TaskH0_pAA0fH0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>importRoute(routeHandle:</code><wbr></wbr><code>options:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously recreates a route from the <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a> provided, i.e. refreshes a previously calculated route, with the specified <a href="sdk-for-ios-explore-classes-refreshrouteoptions">`RefreshRouteOptions`</a>.

  A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func importRoute(routeHandle: RouteHandle, options: RoutingOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>
  - <a href="sdk-for-ios-explore-routing#sdk-for-ios-explore-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Options to import the route from handle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC17setInternalOption3key5valueySS_SStF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setInternalOption-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-offlineroutingengine#sdk-for-ios-explore-s-7heresdk20OfflineRoutingEngineC17setInternalOption3key5valueySS_SStF" class="token"><code>setInternalOption(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method sets internal options that controls offline route calculation behavior. Unsupported options will be logged as warnings. Undocumented options can change their meaning without going through deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setInternalOption(key: String, value: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>Option name</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>New option value</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

