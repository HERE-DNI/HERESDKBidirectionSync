---
title: "RefreshRouteOptions Class Reference"
slug: "sdk-for-ios-navigate-classes-refreshrouteoptions"
---

# RefreshRouteOptions

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use the `RoutingOptions` class instead.") public class RefreshRouteOptions
```

</pre>

``` highlight
extension RefreshRouteOptions: NativeBase
```

``` highlight
extension RefreshRouteOptions: Hashable
```

</div>

</div>

The options to specify how to refresh an already calculated route identified by a <a href="sdk-for-ios-navigate-structs-routehandle">`RouteHandle`</a>. All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp">`RouteOptions.alternatives`</a>, <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">`RouteOptions.arrivalTime`</a>, and <a href="sdk-for-ios-navigate-structs-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a>. If new <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a> are specified, they are ignored as well and instead new <a href="sdk-for-ios-navigate-structs-sectionnotice">`SectionNotice`</a>‘s are generated that indicate where the requested <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a> are violated. Note that when <a href="sdk-for-ios-navigate-structs-evcaroptions#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">`EVCarOptions.ensureReachability`</a> is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-enums-transportmode">`TransportMode`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ transportMode : TransportMode )
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
  <td><code> </code><em><code>transportMode</code></em><code> </code></td>
  <td><div>
  <p>Updates the transport mode for the route.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-caroptions">`CarOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ carOptions : CarOptions )
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
  <td><code> </code><em><code>carOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a car route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-truckoptions">`TruckOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ truckOptions : TruckOptions )
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
  <td><code> </code><em><code>truckOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a truck route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-pedestrianoptions">`PedestrianOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ pedestrianOptions : PedestrianOptions )
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
  <td><code> </code><em><code>pedestrianOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a pedestrian route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-scooteroptions">`ScooterOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ scooterOptions : ScooterOptions )
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
  <td><code> </code><em><code>scooterOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a scooter route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-taxioptions">`TaxiOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ taxiOptions : TaxiOptions )
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
  <td><code> </code><em><code>taxiOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a taxi route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-evcaroptions">`EVCarOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ evCarOptions : EVCarOptions )
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
  <td><code> </code><em><code>evCarOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to an electric car route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-evtruckoptions">`EVTruckOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ evTruckOptions : EVTruckOptions )
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
  <td><code> </code><em><code>evTruckOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to an electric truck route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-bicycleoptions">`BicycleOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ bicycleOptions : BicycleOptions )
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
  <td><code> </code><em><code>bicycleOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a bicycle route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-busoptions">`BusOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ busOptions : BusOptions )
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
  <td><code> </code><em><code>busOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a bus route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

  Constructs a RefreshRouteOptions object with <a href="sdk-for-ios-navigate-structs-privatebusoptions">`PrivateBusOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ privateBusOptions : PrivateBusOptions )
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
  <td><code> </code><em><code>privateBusOptions</code></em><code> </code></td>
  <td><div>
  <p>Converts the route to a private bus route, if a different transport mode was used for the <a href="sdk-for-ios-navigate-structs-routehandle"><code>RouteHandle</code></a>. Note that in case this is not possible, an <a href="sdk-for-ios-navigate-enums-routingerror#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF"><code>RoutingError.noRouteFound</code></a> error will be triggered.</p>
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

