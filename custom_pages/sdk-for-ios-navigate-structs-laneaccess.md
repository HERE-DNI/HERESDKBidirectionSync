---
title: "LaneAccess Structure Reference"
slug: "sdk-for-ios-navigate-structs-laneaccess"
---

# LaneAccess

<div class="declaration">

<div class="language">

``` highlight
public struct LaneAccess : Hashable
```

</div>

</div>

A struct which identifies the vehicle type(s) allowed to access a lane.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV11automobilesSbvp"></span>` `<span id="//apple_ref/swift/Property/automobiles" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV11automobilesSbvp" class="token"><code>automobiles</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var automobiles: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV5busesSbvp"></span>` `<span id="//apple_ref/swift/Property/buses" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV5busesSbvp" class="token"><code>buses</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Buses that are used for public transportation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var buses: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV5taxisSbvp"></span>` `<span id="//apple_ref/swift/Property/taxis" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV5taxisSbvp" class="token"><code>taxis</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Four-wheel vehicles that are usually fitted with a taximeter, that may be hired, along with their driver, to carry passengers to any specified destination.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var taxis: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV8carpoolsSbvp"></span>` `<span id="//apple_ref/swift/Property/carpools" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV8carpoolsSbvp" class="token"><code>carpools</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the sharing of car journeys so that more than one person travels in a car, and prevents the need for others to have to drive to a location themselves.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var carpools: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV11pedestriansSbvp"></span>` `<span id="//apple_ref/swift/Property/pedestrians" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV11pedestriansSbvp" class="token"><code>pedestrians</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Persons traveling on foot, whether walking or running.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pedestrians: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV6trucksSbvp"></span>` `<span id="//apple_ref/swift/Property/trucks" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV6trucksSbvp" class="token"><code>trucks</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Large vehicles that range from medium to heavy duty trucks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trucks: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV14throughTrafficSbvp"></span>` `<span id="//apple_ref/swift/Property/throughTraffic" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV14throughTrafficSbvp" class="token"><code>throughTraffic</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Passenger vehicles (i.e., those defined as passenger car/automobiles) that are allowed to access roads that have traffic restrictions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var throughTraffic: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV16deliveryVehiclesSbvp"></span>` `<span id="//apple_ref/swift/Property/deliveryVehicles" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV16deliveryVehiclesSbvp" class="token"><code>deliveryVehicles</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Delivery <a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV6trucksSbvp">`LaneAccess.trucks`</a> that are permitted to enter the city proper to unload goods at businesses.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var deliveryVehicles: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV17emergencyVehiclesSbvp"></span>` `<span id="//apple_ref/swift/Property/emergencyVehicles" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV17emergencyVehiclesSbvp" class="token"><code>emergencyVehicles</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Any vehicle that is designated and authorized to respond to an emergency in a life-threatening situation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var emergencyVehicles: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10LaneAccessV11motorcyclesSbvp"></span>` `<span id="//apple_ref/swift/Property/motorcycles" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-laneaccess#/s:7heresdk10LaneAccessV11motorcyclesSbvp" class="token"><code>motorcycles</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Motorized two-wheeled passenger vehicles. Generally, mopeds are considered motorcycles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var motorcycles: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(automobiles: buses: taxis: carpools: pedestrians: trucks: throughTraffic: deliveryVehicles: emergencyVehicles: motorcycles: )

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
  public init ( automobiles : Bool , buses : Bool , taxis : Bool , carpools : Bool , pedestrians : Bool , trucks : Bool , throughTraffic : Bool , deliveryVehicles : Bool , emergencyVehicles : Bool , motorcycles : Bool )
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

