---
title: "RefreshRouteParameters Structure Reference"
slug: "sdk-for-ios-explore-structs-refreshrouteparameters"
---

# RefreshRouteParameters

<div class="declaration">

<div class="language">

``` highlight
public struct RefreshRouteParameters : Hashable
```

</div>

</div>

This struct provides the necessary information for refreshing a route from a specific location on it.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandleAA0cF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeHandle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-refreshrouteparameters#sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandleAA0cF0Vvp" class="token"><code>routeHandle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The route handle holding the route to be refreshed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeHandle: RouteHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV13startingPointAA8WaypointVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-startingPoint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-refreshrouteparameters#sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV13startingPointAA8WaypointVSgvp" class="token"><code>startingPoint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identify the new starting point of the route. It should be of type <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO8stopoveryA2CmF">`WaypointType.stopover`</a>. Otherwise, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO16invalidParameteryA2CmF">`RoutingError.invalidParameter`</a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-ios-explore-structs-routehandle">`RouteHandle`</a>. The location of this waypoint may by provided, for example, by a <a href="sdk-for-ios-explore-structs-routeprogress">`RouteProgress`</a> event. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-ios-explore-structs-waypoint">`Waypoint`</a> items that lie behind the new starting point (i.e. the path that was already traveled). Plus, <a href="sdk-for-ios-explore-classes-route#sdk-for-ios-explore-s-7heresdk5RouteC14lengthInMeterss5Int32Vvp">`Route.lengthInMeters`</a>, <a href="sdk-for-ios-explore-classes-route#sdk-for-ios-explore-s-7heresdk5RouteC8durationSdvp">`Route.duration`</a>, and similar values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">`RoutingError.couldNotMatchOrigin`</a> error is triggered. In that case, an application may decide to calculate a new route from scratch.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startingPoint: Waypoint?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV20startingSectionIndexs5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-startingSectionIndex" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-refreshrouteparameters#sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV20startingSectionIndexs5Int32VSgvp" class="token"><code>startingSectionIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the index of the last traveled route section. When it is provided, the previous sections are discarded from the refreshed route and the starting point is searched in the provided section. If the starting point is not found in that section an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">`RoutingError.couldNotMatchOrigin`</a> error is triggered.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startingSectionIndex: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV41traveledDistanceOnStartingSectionInMeterss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-traveledDistanceOnStartingSectionInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-refreshrouteparameters#sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV41traveledDistanceOnStartingSectionInMeterss5Int32VSgvp" class="token"><code>traveledDistanceOnStartingSectionInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides an indication on how much of the starting section is already traveled. The refresh route function would ignore the first part of the section. If it is provided with an invalid starting section index, an <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO16invalidParameteryA2CmF">`RoutingError.invalidParameter`</a> error is generated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var traveledDistanceOnStartingSectionInMeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandle13startingPointAcA0cF0V_AA8WaypointVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-routeHandle-startingPoint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-refreshrouteparameters#sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandle13startingPointAcA0cF0V_AA8WaypointVtcfc" class="token"><code>init(routeHandle:</code><wbr></wbr><code>startingPoint:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create a new instance of `RefreshRouteParameters` with the new starting point on the route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(routeHandle: RouteHandle, startingPoint: Waypoint)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>

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
  <p>Identify the new starting point of the route.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandle20startingSectionIndex026traveledDistanceOnStartingH8InMetersAcA0cF0V_s5Int32VAJtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-routeHandle-startingSectionIndex-traveledDistanceOnStartingSectionInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-refreshrouteparameters#sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandle20startingSectionIndex026traveledDistanceOnStartingH8InMetersAcA0cF0V_s5Int32VAJtcfc" class="token"><code>init(routeHandle:</code><wbr></wbr><code>startingSectionIndex:</code><wbr></wbr><code>traveledDistanceOnStartingSectionInMeters:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create a new instance of `RefreshRouteParameters` with the point on the section of the route as a new starting point.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(routeHandle: RouteHandle, startingSectionIndex: Int32, traveledDistanceOnStartingSectionInMeters: Int32)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>

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
  <td><code> </code><em><code>startingSectionIndex</code></em><code> </code></td>
  <td><div>
  <p>Indicates the index of the last traveled route section.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>traveledDistanceOnStartingSectionInMeters</code></em><code> </code></td>
  <td><div>
  <p>Provides an indication on how much of the starting section is already traveled.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandle13startingPoint0G12SectionIndex026traveledDistanceOnStartingI8InMetersAcA0cF0V_AA8WaypointVs5Int32VAMtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-routeHandle-startingPoint-startingSectionIndex-traveledDistanceOnStartingSectionInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-refreshrouteparameters#sdk-for-ios-explore-s-7heresdk22RefreshRouteParametersV11routeHandle13startingPoint0G12SectionIndex026traveledDistanceOnStartingI8InMetersAcA0cF0V_AA8WaypointVs5Int32VAMtcfc" class="token"><code>init(routeHandle:</code><wbr></wbr><code>startingPoint:</code><wbr></wbr><code>startingSectionIndex:</code><wbr></wbr><code>traveledDistanceOnStartingSectionInMeters:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create a new instance of `RefreshRouteParameters` with the new starting point and the section position on the route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(routeHandle: RouteHandle, startingPoint: Waypoint, startingSectionIndex: Int32, traveledDistanceOnStartingSectionInMeters: Int32)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>

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
  <p>Identify the new starting point of the route.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>startingSectionIndex</code></em><code> </code></td>
  <td><div>
  <p>Indicates the index of the last traveled route section.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>traveledDistanceOnStartingSectionInMeters</code></em><code> </code></td>
  <td><div>
  <p>Provides an indication on how much of the starting section is already traveled.</p>
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

