---
title: "LaneType Structure Reference"
slug: "sdk-for-ios-explore-structs-lanetype"
---

# LaneType

<div class="declaration">

<div class="language">

``` highlight
public struct LaneType : Hashable
```

</div>

</div>

A struct that provides information on the available lane properties. The lane type values can be combined as follows:

- High Occupancy Vehicle, Reversible
- High Occupancy Vehicle and Express
- Reversible and Express
- High Occupancy Vehicle, Reversible and Express
- High Occupancy Vehicle and Acceleration
- Reversible, Acceleration Lane
- High Occupancy Vehicle, Reversible, Acceleration Lane
- Express and Acceleration
- High Occupancy Vehicle and Deceleration
- Reversible, Deceleration Lane
- High Occupancy Vehicle, Reversible, Deceleration Lane
- Express and Deceleration

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV9isRegularSbvp"></span>` `<span id="//apple_ref/swift/Property/isRegular" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV9isRegularSbvp" class="token"><code>isRegular</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Regular lane is a lane that does not have a specific use.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRegular: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV22isHighOccupancyVehicleSbvp"></span>` `<span id="//apple_ref/swift/Property/isHighOccupancyVehicle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV22isHighOccupancyVehicleSbvp" class="token"><code>isHighOccupancyVehicle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A lane which is restricted for high occupancy vehicles. Note: High occupancy vehicles are vehicles with a driver and one or more passengers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isHighOccupancyVehicle: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV12isReversibleSbvp"></span>` `<span id="//apple_ref/swift/Property/isReversible" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV12isReversibleSbvp" class="token"><code>isReversible</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A lane in which traffic may travel in either direction, depending on certain conditions such as the time of the day to improve traffic flow during rush hours.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isReversible: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV9isExpressSbvp"></span>` `<span id="//apple_ref/swift/Property/isExpress" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV9isExpressSbvp" class="token"><code>isExpress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Express lane is a lane or set of lanes usually physically separated from the major roadway with limited entry and exit points to quickly move traffic in and out of a major metropolitan city. An express lane can be reversible, bidirectional, or one-way.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isExpress: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV14isAccelerationSbvp"></span>` `<span id="//apple_ref/swift/Property/isAcceleration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV14isAccelerationSbvp" class="token"><code>isAcceleration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle increase its speed to where it can safely merge with ongoing traffic. These lanes can be accessed from ramps, rest areas, or weigh stations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isAcceleration: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV14isDecelerationSbvp"></span>` `<span id="//apple_ref/swift/Property/isDeceleration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV14isDecelerationSbvp" class="token"><code>isDeceleration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A deceleration lane is the same as an acceleration lane but used for the opposite scenario.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDeceleration: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV11isAuxiliarySbvp"></span>` `<span id="//apple_ref/swift/Property/isAuxiliary" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV11isAuxiliarySbvp" class="token"><code>isAuxiliary</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next interchange.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isAuxiliary: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV6isSlowSbvp"></span>` `<span id="//apple_ref/swift/Property/isSlow" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV6isSlowSbvp" class="token"><code>isSlow</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isSlow: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV9isPassingSbvp"></span>` `<span id="//apple_ref/swift/Property/isPassing" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV9isPassingSbvp" class="token"><code>isPassing</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A passing lane is a lane that can occur on steep mountain grades or other roads where overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass slow moving vehicles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPassing: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV10isShoulderSbvp"></span>` `<span id="//apple_ref/swift/Property/isShoulder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV10isShoulderSbvp" class="token"><code>isShoulder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is not generally used for driving, although it is possible under certain circumstances.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isShoulder: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV17isRegulatedAccessSbvp"></span>` `<span id="//apple_ref/swift/Property/isRegulatedAccess" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV17isRegulatedAccessSbvp" class="token"><code>isRegulatedAccess</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A regulated lane access is a lane designated as a holding zone, used to regulate traffic using time intervals. Regulated lane access is only coded for truck holding zones that are used to regulate truck access into tunnels and over bridges using time intervals (e.g., some tunnel accesses in Switzerland).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRegulatedAccess: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV6isTurnSbvp"></span>` `<span id="//apple_ref/swift/Property/isTurn" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV6isTurnSbvp" class="token"><code>isTurn</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTurn: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV12isCenterTurnSbvp"></span>` `<span id="//apple_ref/swift/Property/isCenterTurn" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV12isCenterTurnSbvp" class="token"><code>isCenterTurn</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Center turn lane is a bidirectional turn lane located in the middle of a road that allows traffic in both directions to turn left (right for left side driving countries).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isCenterTurn: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV14isTruckParkingSbvp"></span>` `<span id="//apple_ref/swift/Property/isTruckParking" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV14isTruckParkingSbvp" class="token"><code>isTruckParking</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for emergency.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTruckParking: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV9isParkingSbvp"></span>` `<span id="//apple_ref/swift/Property/isParking" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV9isParkingSbvp" class="token"><code>isParking</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parking lanes are portions of the road bed that may be used for parking legally. They may allow vehicles to use them as driving lanes at times, though.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isParking: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV17isVariableDrivingSbvp"></span>` `<span id="//apple_ref/swift/Property/isVariableDriving" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV17isVariableDrivingSbvp" class="token"><code>isVariableDriving</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Variable driving lanes are lanes added to a road that open and close to accommodate traffic volume and flow using variable indicators.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isVariableDriving: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LaneTypeV9isBicycleSbvp"></span>` `<span id="//apple_ref/swift/Property/isBicycle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-lanetype#/s:7heresdk8LaneTypeV9isBicycleSbvp" class="token"><code>isBicycle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by lane markings, signs, buffers or barriers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isBicycle: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(isRegular: isHighOccupancyVehicle: isReversible: isExpress: isAcceleration: isDeceleration: isAuxiliary: isSlow: isPassing: isShoulder: isRegulatedAccess: isTurn: isCenterTurn: isTruckParking: isParking: isVariableDriving: isBicycle: )

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
  public init ( isRegular : Bool , isHighOccupancyVehicle : Bool , isReversible : Bool , isExpress : Bool , isAcceleration : Bool , isDeceleration : Bool , isAuxiliary : Bool , isSlow : Bool , isPassing : Bool , isShoulder : Bool , isRegulatedAccess : Bool , isTurn : Bool , isCenterTurn : Bool , isTruckParking : Bool , isParking : Bool , isVariableDriving : Bool , isBicycle : Bool )
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

