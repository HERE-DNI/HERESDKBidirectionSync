---
title: "RoutePlace Structure Reference"
slug: "sdk-for-ios-explore-structs-routeplace"
---

# RoutePlace

<div class="declaration">

<div class="language">

``` highlight
public struct RoutePlace : Hashable
```

</div>

</div>

The location information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV4typeAA0bC4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV4typeAA0bC4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of the route place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: RoutePlaceType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/waypointIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp" class="token"><code>waypointIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If available, this index corresponds to the waypoint in the original user-defined waypoint list. Otherwise, this waypoint was added during route calculation by the system.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var waypointIndex: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV19originalCoordinatesAA03GeoE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/originalCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV19originalCoordinatesAA03GeoE0VSgvp" class="token"><code>originalCoordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  User-defined geographic coordinates. If not available, it means this place was added during route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var originalCoordinates: GeoCoordinates?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV21mapMatchedCoordinatesAA03GeoF0Vvp"></span>` `<span id="//apple_ref/swift/Property/mapMatchedCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV21mapMatchedCoordinatesAA03GeoF0Vvp" class="token"><code>mapMatchedCoordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map-matched geographic coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var mapMatchedCoordinates: GeoCoordinates
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV18displayCoordinatesAA03GeoE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/displayCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV18displayCoordinatesAA03GeoE0VSgvp" class="token"><code>displayCoordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Location of the Points of Interest (PoI) to be displayed in the visualization. In the map data, PoI have a set of display coordinates as well as a set of access/routing coordinates. While the access/routing coordinates specify the nearest accessible road network location that can be apart from actual location of the PoI, the display coordinates specify the location of the PoI to be displayed accurately in the visualization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var displayCoordinates: GeoCoordinates?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV21chargeInKilowattHoursSdSgvp"></span>` `<span id="//apple_ref/swift/Property/chargeInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV21chargeInKilowattHoursSdSgvp" class="token"><code>chargeInKilowattHours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimated battery charge in kWh for electric vehicles when leaving this place. Available only if the route was calculated with <a href="sdk-for-ios-explore-structs-electricvehicleoptions#/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp">`ElectricVehicleOptions.ensureReachability`</a> = `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargeInKilowattHours: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV15chargingStationAA08ChargingE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/chargingStation" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV15chargingStationAA08ChargingE0VSgvp" class="token"><code>chargingStation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Charging station data for electric vehicles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargingStation: ChargingStation?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV4nameSSSgvp"></span>` `<span id="//apple_ref/swift/Property/name" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV4nameSSSgvp" class="token"><code>name</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of a public transit place if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV2idSSSgvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV2idSSSgvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifier of a public transit place if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV8platformSSSgvp"></span>` `<span id="//apple_ref/swift/Property/platform" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV8platformSSSgvp" class="token"><code>platform</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Platform name or number of a public transit place if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var platform: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RoutePlaceV17sideOfDestinationAA04SideeF0OSgvp"></span>` `<span id="//apple_ref/swift/Property/sideOfDestination" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV17sideOfDestinationAA04SideeF0OSgvp" class="token"><code>sideOfDestination</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Side of destination: left, right or undefined. `nil` for transit sections and for origin points. `UNDEFINED` if <a href="sdk-for-ios-explore-structs-routeplace#/s:7heresdk10RoutePlaceV19originalCoordinatesAA03GeoE0VSgvp">`originalCoordinates`</a> are not identified or too close to the road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sideOfDestination: SideOfDestination?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      isOffRoad()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Checks whether the `RoutePlace` is off-road or not.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func isOffRoad () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  `true` if the `RoutePlace` is off-road, `false` otherwise.

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

