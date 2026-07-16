---
title: "JunctionViewLaneAssistance Structure Reference"
slug: "sdk-for-ios-navigate-structs-junctionviewlaneassistance"
---

# JunctionViewLaneAssistance

<div class="declaration">

<div class="language">

``` highlight
public struct JunctionViewLaneAssistance : Hashable
```

</div>

</div>

A struct that provides lane assistance information for the next complex junction in order to keep following the route. It is recommended to indicate `JunctionViewLaneAssistance` and <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> separately or to indicate only <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> information - `JunctionViewLaneAssistance` will recommend all lanes that allow to pass the upcoming complex junction, regardless if they will lead to the next maneuver or not. If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be the same as the ones from <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a>.

A junction is recognized as complex only if:

- it is at least a bifurcation;
- it has at least two lanes whose directions do not follow the current route. In opposition to <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a>, notifications are also forwarded when there is no maneuver action occurring at the next complex junction. Therefore, `JunctionViewLaneAssistance` can be disjointed from maneuvers. If lane assistance should be used to associate it with upcoming maneuvers, consider to use <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> instead. Note that <a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">`ManeuverViewLaneAssistance`</a> notifications are synchronized with maneuver events, whereas `JunctionViewLaneAssistance` events are not strictly synchronized with maneuver events.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lanesForNextJunction" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance#sdk-for-ios-navigate-s-7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp" class="token"><code>lanesForNextJunction</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of lanes on the next complex junction. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

  **Note:** Lanes going in opposite direction are not included in the list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lanesForNextJunction: [Lane]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lane">Lane</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26JunctionViewLaneAssistanceV010distanceToB8InMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-distanceToJunctionInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance#sdk-for-ios-navigate-s-7heresdk26JunctionViewLaneAssistanceV010distanceToB8InMetersSdvp" class="token"><code>distanceToJunctionInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the next complex junction in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToJunctionInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0010distanceToB8InMetersACSayAA0D0VG_Sdtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-lanesForNextJunction-distanceToJunctionInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-junctionviewlaneassistance#sdk-for-ios-navigate-s-7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0010distanceToB8InMetersACSayAA0D0VG_Sdtcfc" class="token"><code>init(lanesForNextJunction:</code><wbr></wbr><code>distanceToJunctionInMeters:</code><wbr></wbr><code>)</code></a> 

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

    - lanesForNextJunction: A list of lanes on the next complex junction. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

    **Note:** Lanes going in opposite direction are not included in the list.

    - distanceToJunctionInMeters: Distance to the next complex junction in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(lanesForNextJunction: [Lane], distanceToJunctionInMeters: Double)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lane">Lane</a>

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

