---
title: "RoutingProtocol Protocol Reference"
slug: "sdk-for-ios-navigate-protocols-routingprotocol"
---

# RoutingProtocol

<div class="declaration">

<div class="language">

``` highlight
public protocol RoutingProtocol : AnyObject
```

</div>

</div>

Provides the protocol for the online and offline routing engines.

</div>

<div class="section section task-group-section">

<div class="task-group">

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
  @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], options : RoutingOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], carOptions : CarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], pedestrianOptions : PedestrianOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], truckOptions : TruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], scooterOptions : ScooterOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], bicycleOptions : BicycleOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], taxiOptions : TaxiOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], evCarOptions : EVCarOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], evTruckOptions : EVTruckOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], busOptions : BusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `calculate_route(﹚` methods with RoutingOptions parameter instead.") @discardableResult func calculateRoute ( with waypoints : [ Waypoint ], privateBusOptions : PrivateBusOptions , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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
  @discardableResult func returnToRoute ( _ route : Route , startingPoint : Waypoint , lastTraveledSectionIndex : Int32 , traveledDistanceOnLastSectionInMeters : Int32 , completion : @escaping CalculateRouteCompletionHandler ) -> TaskHandle
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

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

