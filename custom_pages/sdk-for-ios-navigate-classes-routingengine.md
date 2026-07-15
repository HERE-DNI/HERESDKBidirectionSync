---
title: "RoutingEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-routingengine"
---

# RoutingEngine

<div class="declaration">

<div class="language">

``` highlight
public class RoutingEngine : RoutingProtocol
```

``` highlight
extension RoutingEngine: NativeBase
```

``` highlight
extension RoutingEngine: Hashable
```

</div>

</div>

Use the RoutingEngine to calculate a route from A to B with a number of waypoints in between.

Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.

**Note:** The engine does not support an unlimited number of waypoints. The limit is defined by the HERE backend services and may change. For now, the maximum number of waypoints should be below 200. This value may change and it is not guaranteed to be stable. If you need to support very large lists of waypoints, consider to import a route (see

    importRoute()

method) or use the <a href="sdk-for-ios-navigate-classes-offlineroutingengine">`OfflineRoutingEngine`</a> which supports an unlimited number of waypoints. The <a href="sdk-for-ios-navigate-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is only available for Navigate licence.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init()

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

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init () throws
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of RoutingEngine.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ sdkEngine : SDKNativeEngine ) throws
  ```

  </pre>

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

      init(connectionSettings: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of RoutingEngine.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( connectionSettings : RoutingConnectionSettings ) throws
  ```

  </pre>

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
  <td><code> </code><em><code>connectionSettings</code></em><code> </code></td>
  <td><div>
  <p>Settings for the route calculation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(_: connectionSettings: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of RoutingEngine.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ sdkEngine : SDKNativeEngine , connectionSettings : RoutingConnectionSettings ) throws
  ```

  </pre>

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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>An SDKEngine instance.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>connectionSettings</code></em><code> </code></td>
  <td><div>
  <p>Settings for the route calculation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      calculateRoute(with: options: completion: )

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
  @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], options : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      calculateRoute(with: carOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], carOptions : CarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      calculateRoute(with: pedestrianOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], pedestrianOptions : PedestrianOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>pedestrianOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for pedestrian route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for pedestrians and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      calculateRoute(with: truckOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], truckOptions : TruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      calculateRoute(with: scooterOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], scooterOptions : ScooterOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scooterOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for scooter route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for scooters and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      calculateRoute(with: bicycleOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], bicycleOptions : BicycleOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bicycleOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for bicycle route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for bicycles and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      calculateRoute(with: taxiOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], taxiOptions : TaxiOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>waypoints</code></em><code> </code></td>
  <td><div>
  <p>The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>taxiOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for taxi route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is is not supported for taxis and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      calculateRoute(with: evCarOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], evCarOptions : EVCarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      calculateRoute(with: evTruckOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], evTruckOptions : EVTruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      calculateRoute(with: busOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], busOptions : BusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      calculateRoute(with: privateBusOptions: completion: )

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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func calculateRoute ( with waypoints : [ Waypoint ], privateBusOptions : PrivateBusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      returnToRoute(_: startingPoint: lastTraveledSectionIndex: traveledDistanceOnLastSectionInMeters: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.

  **Note:** Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp">`RouteOptions.alternatives`</a>, <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">`RouteOptions.arrivalTime`</a>, and <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a>. Most route options are only applied to the newly calculated part back to the route.

  An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too.

  Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route.

  A typical use case is to await at least 3 <a href="sdk-for-ios-navigate-structs-routedeviation">`RouteDeviation`</a> events before calling this method.

  - Or alternatively, wait at least 10 seconds after getting the first deviation event.
  - On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time.
  - Optionally, it may make sense to verify if the vehicle was ever following the route by checking if <a href="sdk-for-ios-navigate-structs-routedeviation#/s:7heresdk14RouteDeviationV014lastLocationOnB0AA09NavigableE0VSgvp">`RouteDeviation.lastLocationOnRoute`</a> is set.

  Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the “Handle route deviations” section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func returnToRoute ( _ route : Route , startingPoint : Waypoint , lastTraveledSectionIndex : Int32 , traveledDistanceOnLastSectionInMeters : Int32 , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>route</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-navigate-classes-route"><code>Route</code></a> calculated using the online or offline route engine. For the offline case, It should not contain an indoor <a href="sdk-for-ios-navigate-classes-section"><code>Section</code></a> as such routes will fail. For the online case, it should have <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>startingPoint</code></em><code> </code></td>
  <td><div>
  <p>The current location, for example, provided by a <a href="sdk-for-ios-navigate-structs-routedeviation"><code>RouteDeviation</code></a> event. The waypoint needs to be of type <a href="sdk-for-ios-navigate-enums-waypointtype#/s:7heresdk12WaypointTypeO8stopoveryA2CmF"><code>WaypointType.stopover</code></a>. Otherwise, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF"><code>RoutingError.invalidParameter</code></a> error is generated.</p>
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

      refreshRoute(routeHandle: startingPoint: refreshRouteOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a>, updating the starting point and route metadata based on <a href="sdk-for-ios-navigate-classes-refreshrouteoptions">`RefreshRouteOptions`</a>. The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information or retrieve updated ETA duration, consider using

      RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)

  instead.
  </p>

  Calling this method will trigger a new “HERE Routing” transaction, for example, if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `refresh_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func refreshRoute ( routeHandle : RouteHandle , startingPoint : Waypoint , refreshRouteOptions : RefreshRouteOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>startingPoint</code></em><code> </code></td>
  <td><div>
  <p>Updates the starting point of the route. It should be of type <a href="sdk-for-ios-navigate-enums-waypointtype#/s:7heresdk12WaypointTypeO8stopoveryA2CmF"><code>WaypointType.stopover</code></a>. Otherwise, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF"><code>RoutingError.invalidParameter</code></a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-ios-navigate-structs-waypoint"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that was already travelled). Plus, <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp"><code>Route.lengthInMeters</code></a> and <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC8durationSdvp"><code>Route.duration</code></a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF"><code>RoutingError.couldNotMatchOrigin</code></a> error is triggered. In that case, an application may decide to calculate a new route from scratch.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>refreshRouteOptions</code></em><code> </code></td>
  <td><div>
  <p>Options to refresh the route.</p>
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

      refreshRoute(routeHandle: startingPoint: lastTraveledSectionIndex: traveledDistanceOnLastSectionInMeters: refreshRouteOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a>, updating the starting point and route metadata based on <a href="sdk-for-ios-navigate-classes-refreshrouteoptions">`RefreshRouteOptions`</a>. The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use

      RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)

  instead.
  </p>

  Calling this method will trigger a new “HERE Routing” transaction, for example, if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `refresh_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func refreshRoute ( routeHandle : RouteHandle , startingPoint : Waypoint ?, lastTraveledSectionIndex : Int32 ?, traveledDistanceOnLastSectionInMeters : Int32 ?, refreshRouteOptions : RefreshRouteOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>startingPoint</code></em><code> </code></td>
  <td><div>
  <p>Updates the starting point of the route. It should be of type <a href="sdk-for-ios-navigate-enums-waypointtype#/s:7heresdk12WaypointTypeO8stopoveryA2CmF"><code>WaypointType.stopover</code></a>. Otherwise, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF"><code>RoutingError.invalidParameter</code></a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-ios-navigate-structs-waypoint"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that was already travelled). Plus, <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp"><code>Route.lengthInMeters</code></a> and <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC8durationSdvp"><code>Route.duration</code></a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF"><code>RoutingError.couldNotMatchOrigin</code></a> error is triggered. In that case, an application may decide to calculate a new route from scratch.</p>
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
  <td><code> </code><em><code>refreshRouteOptions</code></em><code> </code></td>
  <td><div>
  <p>Options to refresh the route.</p>
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

      refreshRoute(routeHandle: startingPoint: lastTraveledSectionIndex: traveledDistanceOnLastSectionInMeters: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a>, updating the starting point and route metadata based on <a href="sdk-for-ios-navigate-structs-routingoptions">`RoutingOptions`</a>. The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use

      RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)

  instead.
  </p>

  Calling this method will trigger a new “HERE Routing” transaction, for example, if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `refresh_route(﹚` methods with RefreshRouteParameters parameter instead.") @discardableResult public func refreshRoute ( routeHandle : RouteHandle , startingPoint : Waypoint ?, lastTraveledSectionIndex : Int32 ?, traveledDistanceOnLastSectionInMeters : Int32 ?, options : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>startingPoint</code></em><code> </code></td>
  <td><div>
  <p>Updates the starting point of the route. It should be of type <a href="sdk-for-ios-navigate-enums-waypointtype#/s:7heresdk12WaypointTypeO8stopoveryA2CmF"><code>WaypointType.stopover</code></a>. Otherwise, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF"><code>RoutingError.invalidParameter</code></a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-ios-navigate-structs-waypoint"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that was already traveled). Plus, <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp"><code>Route.lengthInMeters</code></a> and <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC8durationSdvp"><code>Route.duration</code></a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF"><code>RoutingError.couldNotMatchOrigin</code></a> error is triggered. In that case, an application may decide to calculate a new route from scratch.</p>
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
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options define the vehicle and route options to calculate the route.</p>
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

      refreshRoute(routeHandle: startingPoint: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a>, updating the starting point and route metadata based on <a href="sdk-for-ios-navigate-structs-routingoptions">`RoutingOptions`</a>. The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use

      RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)

  instead.
  </p>

  Calling this method will trigger a new “HERE Routing” transaction, for example, if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `refresh_route(﹚` methods with RefreshRouteParameters parameter instead.") @discardableResult public func refreshRoute ( routeHandle : RouteHandle , startingPoint : Waypoint , options : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>startingPoint</code></em><code> </code></td>
  <td><div>
  <p>Updates the starting point of the route. It should be of type <a href="sdk-for-ios-navigate-enums-waypointtype#/s:7heresdk12WaypointTypeO8stopoveryA2CmF"><code>WaypointType.stopover</code></a>. Otherwise, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF"><code>RoutingError.invalidParameter</code></a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-ios-navigate-structs-waypoint"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that was already traveled). Plus, <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp"><code>Route.lengthInMeters</code></a> and <a href="sdk-for-ios-navigate-classes-route#/s:7heresdk5RouteC8durationSdvp"><code>Route.duration</code></a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF"><code>RoutingError.couldNotMatchOrigin</code></a> error is triggered. In that case, an application may decide to calculate a new route from scratch.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options define the vehicle and route options to calculate the route.</p>
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

      refreshRoute(refreshRouteParameters: routingOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a>, updating the starting point and route metadata based on <a href="sdk-for-ios-navigate-structs-routingoptions">`RoutingOptions`</a>. The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func refreshRoute ( refreshRouteParameters : RefreshRouteParameters , routingOptions : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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

      importRoute(routeHandle: refreshRouteOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously recreates a route from the <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a> provided, i.e. refreshes a previously calculated route, with the specified <a href="sdk-for-ios-navigate-classes-refreshrouteoptions">`RefreshRouteOptions`</a>.

  A route handle can be invalid when the map data changes that is used by the HERE backend to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time. Instead, a possible use case can be to plan a route with another HERE service. For example, a HERE REST API that allows to calculate a route on a desktop. Then this route can be transferred via the handle to a mobile device for further use with the HERE SDK.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( routeHandle : RouteHandle , refreshRouteOptions : RefreshRouteOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>refreshRouteOptions</code></em><code> </code></td>
  <td><div>
  <p>The options define the vehicle and route options to calculate the route. <strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.ElectricVehicleOptions.ensure_reachability] option is set to <code>true</code>.</p>
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

      importRoute(with: carOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], carOptions : CarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
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

      importRoute(with: routeStops: pedestrianOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], pedestrianOptions : PedestrianOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>pedestrianOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for pedestrian route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is not supported for pedestrians and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      importRoute(with: routeStops: bicycleOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], bicycleOptions : BicycleOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bicycleOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for bicycle route calculation, along with common route options.</p>
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

      importRoute(with: routeStops: scooterOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], scooterOptions : ScooterOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scooterOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for scooter route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is not supported for scooters and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      importRoute(with: pedestrianOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], pedestrianOptions : PedestrianOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>pedestrianOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for pedestrian route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is not supported for pedestrians and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      importRoute(with: bicycleOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], bicycleOptions : BicycleOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bicycleOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for bicycle route calculation, along with common route options.</p>
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

      importRoute(with: scooterOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], scooterOptions : ScooterOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scooterOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for scooter route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is not supported for scooters and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      importRoute(with: truckOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], truckOptions : TruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
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

      importRoute(with: taxiOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], taxiOptions : TaxiOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>taxiOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for taxi route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is not supported for taxis and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      importRoute(with: busOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], busOptions : BusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>busOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for bus route calculation, along with common route options.</p>
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

      importRoute(with: privateBusOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], privateBusOptions : PrivateBusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>privateBusOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for private bus route calculation, along with common route options.</p>
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

      importRoute(with: evCarOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], evCarOptions : EVCarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>evCarOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for an electric car route calculation, along with common route options. <strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.EVCarOptions.ensure_reachability] option is set to <code>true</code>.</p>
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

      importRoute(with: evTruckOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], evTruckOptions : EVTruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
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

      importRoute(with: routeStops: carOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], carOptions : CarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
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

      importRoute(with: routeStops: truckOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], truckOptions : TruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
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

      importRoute(with: routeStops: taxiOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], taxiOptions : TaxiOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>taxiOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for taxi route calculation, along with common route options. Note that <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO8shortestyA2CmF"><code>OptimizationMode.shortest</code></a> is not supported for taxis and converted to <a href="sdk-for-ios-navigate-enums-optimizationmode#/s:7heresdk16OptimizationModeO7fastestyA2CmF"><code>OptimizationMode.fastest</code></a> automatically.</p>
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

      importRoute(with: routeStops: busOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], busOptions : BusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>busOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for bus route calculation, along with common route options.</p>
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

      importRoute(with: routeStops: privateBusOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], privateBusOptions : PrivateBusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>privateBusOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for private bus route calculation, along with common route options.</p>
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

      importRoute(with: routeStops: evCarOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], evCarOptions : EVCarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>evCarOptions</code></em><code> </code></td>
  <td><div>
  <p>Options specific for an electric car route calculation, along with common route options. <strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.EVCarOptions.ensure_reachability] option is set to <code>true</code>.</p>
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

      importRoute(with: routeStops: evTruckOptions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `import_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], evTruckOptions : EVTruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
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

      importRoute(with: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func importRoute ( with locations : [ Location ], options : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options define the vehicle and route options to calculate the route.</p>
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

      importRoute(with: routeStops: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

  **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in <a href="sdk-for-ios-navigate-classes-section#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">`Section.sectionNotices`</a> .

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func importRoute ( with locations : [ Location ], routeStops : [ RouteStop ], options : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>locations</code></em><code> </code></td>
  <td><div>
  <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"><code>Location.coordinates</code></a> of a location are used to import the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeStops</code></em><code> </code></td>
  <td><div>
  <p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options define the vehicle and route options to calculate the route.</p>
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

      importRoute(routeHandle: options: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously recreates a route from the <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a> provided, i.e. refreshes a previously calculated route, with the specified <a href="sdk-for-ios-navigate-structs-routingoptions">`RoutingOptions`</a>.

  A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func importRoute ( routeHandle : RouteHandle , options : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>routeHandle</code></em><code> </code></td>
  <td><div>
  <p>The route handle holding the route to be refreshed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>The options define the vehicle and route options to calculate the route.</p>
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

      calculateTrafficOnRoute(route: lastTraveledSectionIndex: traveledDistanceOnLastSectionInMeters: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates the traffic along a route starting from the index of the last traveled route section and an offset (in meters) from the last visited position on the section. Call this when only the contained traffic information or the latest ETA duration is needed. This can be called periodically to retrieve updated ETA values during navigation.

  **Note:** Calling this method will trigger a new “HERE Traffic” transaction, for example, if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func calculateTrafficOnRoute ( route : Route , lastTraveledSectionIndex : Int32 , traveledDistanceOnLastSectionInMeters : Int32 , completion : @escaping CalculateTrafficOnRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>route</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-navigate-classes-route"><code>Route</code></a> calculated using the online routing engine. Its <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a> and the original route calculation options will be used to compute the traffic on the route. The original route remains untouched.</p>
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
  <p>Offset, in meters, to the last visited position on the route section defined by the last traveled section index.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.</p>
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

      calculateTrafficOnRoute(route: lastTraveledSectionIndex: traveledDistanceOnLastSectionInMeters: currentChargeInKilowattHours: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates the traffic along an EV car route starting from the index of the last traveled route section and an offset in meters from the last visited position on the section. The field <a href="sdk-for-ios-navigate-structs-trafficonspan#/s:7heresdk13TrafficOnSpanV26consumptionInKilowattHoursSdSgvp">`TrafficOnSpan.consumptionInKilowattHours`</a> will contain the power consumption in kilowatt-hours (kWh) necessary to traverse the span, and <a href="sdk-for-ios-navigate-structs-routeplace#/s:7heresdk10RoutePlaceV21chargeInKilowattHoursSdSgvp">`RoutePlace.chargeInKilowattHours`</a>, inside <a href="sdk-for-ios-navigate-structs-trafficonsection#/s:7heresdk16TrafficOnSectionV14departurePlaceAA05RouteF0Vvp">`TrafficOnSection.departurePlace`</a> and <a href="sdk-for-ios-navigate-structs-trafficonsection#/s:7heresdk16TrafficOnSectionV12arrivalPlaceAA05RouteF0Vvp">`TrafficOnSection.arrivalPlace`</a>, the estimated battery charge in kilowatt-hours (kWh) when leaving/arriving to a section. **Note:** Only EV cars are supported.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func calculateTrafficOnRoute ( route : Route , lastTraveledSectionIndex : Int32 , traveledDistanceOnLastSectionInMeters : Int32 , currentChargeInKilowattHours : Double , completion : @escaping CalculateTrafficOnRouteCompletionHandler ) -> TaskHandle
  ```

  </pre>

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
  <td><code> </code><em><code>route</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-navigate-classes-route"><code>Route</code></a> calculated using the online routing engine. Its <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a> and the original route calculation options, along with EV related information like <a href="sdk-for-ios-navigate-structs-batteryspecifications"><code>BatterySpecifications</code></a>, will be used to compute the traffic on the route. The original route remains untouched.</p>
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
  <p>Offset, in meters, to the last visited position on the route section defined by the last traveled section index.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>currentChargeInKilowattHours</code></em><code> </code></td>
  <td><div>
  <p>Charge level of the vehicle’s battery at the current location (in kWh). It must be non-negative and less than or equal to the value of <a href="sdk-for-ios-navigate-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp"><code>BatterySpecifications.totalCapacityInKilowattHours</code></a>, otherwise the <a href="sdk-for-ios-navigate-structs-batteryspecifications"><code>BatterySpecifications</code></a> instance is considered invalid. Sets <a href="sdk-for-ios-navigate-structs-batteryspecifications#/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp"><code>BatterySpecifications.initialChargeInKilowattHours</code></a> to the given value.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.</p>
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

      setCustomOption(name: value: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom option for routing backend queries. The custom option is applied to all the queries that `RoutingEngine` performs. For a complete list of available parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/routing-api-v8-api-reference/page/index.html">HERE Routing API v8</a>. **Note:** It’s easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomOption ( name : String , value : String ?) -> RoutingError ?
  ```

  </pre>

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>An option value. If the value is <code>nil</code>, the option will be removed. The option value must be a non-empty string.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  An optional error of setting the option. It’s `nil` if the option has been set successfully. It’s `RoutingError.INVALID_PARAMETER` if the input name and/or value haven’t passed internal validation.

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

