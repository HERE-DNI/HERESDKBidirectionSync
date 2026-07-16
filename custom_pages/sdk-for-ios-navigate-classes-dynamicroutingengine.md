---
title: "DynamicRoutingEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-dynamicroutingengine"
---

# DynamicRoutingEngine

<div class="declaration">

<div class="language">

``` highlight
public class DynamicRoutingEngine
```

``` highlight
extension DynamicRoutingEngine: NativeBase
```

``` highlight
extension DynamicRoutingEngine: Hashable
```

</div>

</div>

This class queries the HERE routing backend to find routes with less traffic and therefore an earlier remaining estimated time of arrival.

`DynamicRoutingEngine` polls the HERE routing backend periodically to find the best new route out of a given initial route. For initial route calculation it is recommended to use the <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a> as it already requests traffic-optimized routes.

When a better route is found, it is recommended to follow these steps to set the new route:

1.  Stop the `DynamicRoutingEngine`.

2.  Update the currently active <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a>instance with the newly found route.

3.  Restart the `DynamicRoutingEngine`. This should be done outside of the

        onBetterRouteFound()

    callback.

For both `DynamicRoutingEngine` and <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a>, the resulting routes are optimized based on speed flow changes such as traffic jams, street closures or road accidents. To get the best result, it is recommended to not specify the <a href="sdk-for-ios-navigate-structs-routeoptions#sdk-for-ios-navigate-s-7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">`RouteOptions.departureTime`</a> as then the current time is used by default.

The poll interval is defined by <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions#sdk-for-ios-navigate-s-7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp">`DynamicRoutingEngineOptions.pollInterval`</a> and triggered by <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF">`DynamicRoutingEngine.updateCurrentLocation(...)`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC14StartExceptiona"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-StartException" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC14StartExceptiona" class="token"><code>StartException</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Start exception

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias StartException = DynamicRoutingEngine.StartError
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-dynamicroutingengine-starterror">StartError</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC7optionsAcA0bcD7OptionsVSg_tKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-options" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC7optionsAcA0bcD7OptionsVSg_tKcfc" class="token"><code>init(options:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when the engine was not initialized properly.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(options: DynamicRoutingEngineOptions?) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a>

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
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options defining the behavior of the <code>DynamicRoutingEngine</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVSgtKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_-options" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVSgtKcfc" class="token"><code>init(_:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when the engine was not initialized properly.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ sdkEngine: SDKNativeEngine, options: DynamicRoutingEngineOptions?) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a>

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
  <p>Instance of an existing SDKEngine.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options defining the behavior of the <code>DynamicRoutingEngine</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC10StartErrorO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-StartError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC10StartErrorO" class="token"><code>StartError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Start error

  <a href="sdk-for-ios-navigate-classes-dynamicroutingengine-starterror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum StartError : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension DynamicRoutingEngine.StartError : Error
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-dynamicroutingengine">DynamicRoutingEngine</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC5start5route8delegateyAA5RouteC_AA0bC8Delegate_ptKF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-start-route-delegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC5start5route8delegateyAA5RouteC_AA0bC8Delegate_ptKF" class="token"><code>start(route:</code><wbr></wbr><code>delegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions.

  **Note:** The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC14StartExceptiona">`DynamicRoutingEngine.StartException`</a> when the passed parameter are invalid.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start(route: Route, delegate: DynamicRoutingDelegate) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-route">Route</a>
  - <a href="sdk-for-ios-navigate-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a>

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
  <p>The route to be refreshed. The route must contain a <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>, therefore the route must have been requested with <a href="sdk-for-ios-navigate-structs-routeoptions#sdk-for-ios-navigate-s-7heresdk12RouteOptionsV06enableB6HandleSbvp"><code>RouteOptions.enableRouteHandle</code></a> set to <code>true</code>. The information to calculate new routes will be extracted from the provided route parameter. If more information from the original waypoints is important besides their location, consider to use one of the overloaded methods instead.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The listener to receive the events.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints19refreshRouteOptions8delegateyAA0jG0V_SayAA8WaypointVGAA07RefreshjK0CAA0bC8Delegate_ptKF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-start-routeHandle-waypoints-refreshRouteOptions-delegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints19refreshRouteOptions8delegateyAA0jG0V_SayAA8WaypointVGAA07RefreshjK0CAA0bC8Delegate_ptKF" class="token"><code>start(routeHandle:</code><wbr></wbr><code>waypoints:</code><wbr></wbr><code>refreshRouteOptions:</code><wbr></wbr><code>delegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts polling the HERE backend services to find a better route, as defined by the <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions">`DynamicRoutingEngineOptions`</a>.

  **Note:** The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC14StartExceptiona">`DynamicRoutingEngine.StartException`</a> when the passed parameter are invalid.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `start(﹚` method with RoutingOptions parameter instead.")
  public func start(routeHandle: RouteHandle, waypoints: [Waypoint], refreshRouteOptions: RefreshRouteOptions, delegate: DynamicRoutingDelegate) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-navigate-classes-refreshrouteoptions">RefreshRouteOptions</a>
  - <a href="sdk-for-ios-navigate-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a>

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
  <p>The route handle from the HERE routing backend.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>Allows to specify detailed information on the waypoints of the route. This parameter can be useful, when additional information needs to be specified besides the coordinates - as the coordinates can be retrieved from the contained <a href="sdk-for-ios-navigate-structs-routeplace"><code>RoutePlace</code></a> that are already contained in the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a> parameter.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>refreshRouteOptions</code></em><code> </code></td>
  <td><div>
  <p>The options for the route calculation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The listener to receive the events.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints14routingOptions8delegateyAA05RouteG0V_SayAA8WaypointVGAA0cJ0VAA0bC8Delegate_ptKF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-start-routeHandle-waypoints-routingOptions-delegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints14routingOptions8delegateyAA05RouteG0V_SayAA8WaypointVGAA0cJ0VAA0bC8Delegate_ptKF" class="token"><code>start(routeHandle:</code><wbr></wbr><code>waypoints:</code><wbr></wbr><code>routingOptions:</code><wbr></wbr><code>delegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts polling the HERE backend services to find a better route, as defined by the <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions">`DynamicRoutingEngineOptions`</a>.

  **Note:** The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC14StartExceptiona">`DynamicRoutingEngine.StartException`</a> when the passed parameter are invalid.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func start(routeHandle: RouteHandle, waypoints: [Waypoint], routingOptions: RoutingOptions, delegate: DynamicRoutingDelegate) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-navigate-structs-routingoptions">RoutingOptions</a>
  - <a href="sdk-for-ios-navigate-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a>

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
  <p>The route handle from the HERE routing backend.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>Allows to specify detailed information on the waypoints of the route. This parameter can be useful, when additional information needs to be specified besides the coordinates - as the coordinates can be retrieved from the contained <a href="sdk-for-ios-navigate-structs-routeplace"><code>RoutePlace</code></a> that are already contained in the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a> parameter.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routingOptions</code></em><code> </code></td>
  <td><div>
  <p>The options for the route calculation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The listener to receive the events.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC4stopyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-stop" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC4stopyyF" class="token"><code>stop()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stops polling the HERE backend services.

  **Note:** The engine is not automatically stopped when the destination is reached. Therefore, it is recommended to stop the engine when the destination was reached.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func stop()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-updateCurrentLocation-mapMatchedLocation-sectionIndex" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-dynamicroutingengine#sdk-for-ios-navigate-s-7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF" class="token"><code>updateCurrentLocation(mapMatchedLocation:</code><wbr></wbr><code>sectionIndex:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Updates the current location. This location will be used as new starting point when the next <a href="sdk-for-ios-navigate-structs-dynamicroutingengineoptions#sdk-for-ios-navigate-s-7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp">`DynamicRoutingEngineOptions.pollInterval`</a> is reached and a new route is requested. If an immediate route update is needed, consider to use the RoutingEngine instead. All subsequently calculated routes used for the ETA calculation will start from this location. The location needs to lie on the route or a <a href="sdk-for-ios-navigate-enums-routingerror">`RoutingError`</a> will be issued.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateCurrentLocation(mapMatchedLocation: MapMatchedLocation, sectionIndex: Int32)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmatchedlocation">MapMatchedLocation</a>

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
  <td><code> </code><em><code>mapMatchedLocation</code></em><code> </code></td>
  <td><div>
  <p>The last known location. It is recommended to use a <a href="sdk-for-ios-navigate-structs-navigablelocation#sdk-for-ios-navigate-s-7heresdk17NavigableLocationV010mapMatchedC0AA03MapeC0VSgvp"><code>NavigableLocation.mapMatchedLocation</code></a> as the driver is expected to be on a road.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>sectionIndex</code></em><code> </code></td>
  <td><div>
  <p>The current section from <a href="sdk-for-ios-navigate-structs-routeprogress#sdk-for-ios-navigate-s-7heresdk13RouteProgressV12sectionIndexs5Int32Vvp"><code>RouteProgress.sectionIndex</code></a>.</p>
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

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

