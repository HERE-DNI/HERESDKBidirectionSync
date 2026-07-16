---
title: "Lane Structure Reference"
slug: "sdk-for-ios-navigate-structs-lane"
---

# Lane

<div class="declaration">

<div class="language">

``` highlight
public struct Lane : Hashable
```

</div>

</div>

A struct that provides information for a lane.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4LaneV4typeAA0B4TypeVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV4typeAA0B4TypeVvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the properties of this lane. For example, it indicates whether parking is allowed, if it is an acceleration lane, an express lane, or other attributes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: LaneType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lanetype">LaneType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4LaneV19recommendationStateAA0b14RecommendationD0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-recommendationState" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV19recommendationStateAA0b14RecommendationD0Ovp" class="token"><code>recommendationState</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if this lane leads to the upcoming maneuvers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var recommendationState: LaneRecommendationState
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-lanerecommendationstate">LaneRecommendationState</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4LaneV6accessAA0B6AccessVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-access" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV6accessAA0B6AccessVvp" class="token"><code>access</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates which vehicle types can access this lane.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var access: LaneAccess
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-laneaccess">LaneAccess</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4LaneV12laneMarkingsAA0bD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-laneMarkings" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV12laneMarkingsAA0bD0Vvp" class="token"><code>laneMarkings</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the lane markings between the lanes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var laneMarkings: LaneMarkings
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lanemarkings">LaneMarkings</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4LaneV10directionsSayAA0B9DirectionOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-directions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV10directionsSayAA0B9DirectionOGvp" class="token"><code>directions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates all the lane directions that are available for this lane.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var directions: [LaneDirection]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-lanedirection">LaneDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4LaneV17directionsOnRouteSayAA0B9DirectionOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-directionsOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV17directionsOnRouteSayAA0B9DirectionOGvp" class="token"><code>directionsOnRoute</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the lane directions that are on the route. Following these directions keeps the driver on the route. This is a subset of <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV10directionsSayAA0B9DirectionOGvp">`Lane.directions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var directionsOnRoute: [LaneDirection]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-lanedirection">LaneDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk4LaneV4type19recommendationState6access12laneMarkings10directions0I7OnRouteAcA0B4TypeV_AA0b14RecommendationE0OAA0B6AccessVAA0bH0VSayAA0B9DirectionOGATtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-type-recommendationState-access-laneMarkings-directions-directionsOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-lane#sdk-for-ios-navigate-s-7heresdk4LaneV4type19recommendationState6access12laneMarkings10directions0I7OnRouteAcA0B4TypeV_AA0b14RecommendationE0OAA0B6AccessVAA0bH0VSayAA0B9DirectionOGATtcfc" class="token"><code>init(type:</code><wbr></wbr><code>recommendationState:</code><wbr></wbr><code>access:</code><wbr></wbr><code>laneMarkings:</code><wbr></wbr><code>directions:</code><wbr></wbr><code>directionsOnRoute:</code><wbr></wbr><code>)</code></a> 

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
  public init(type: LaneType, recommendationState: LaneRecommendationState = LaneRecommendationState.notRecommended, access: LaneAccess, laneMarkings: LaneMarkings, directions: [LaneDirection] = [], directionsOnRoute: [LaneDirection] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lanetype">LaneType</a>
  - <a href="sdk-for-ios-navigate-enums-lanerecommendationstate">LaneRecommendationState</a>
  - <a href="sdk-for-ios-navigate-structs-laneaccess">LaneAccess</a>
  - <a href="sdk-for-ios-navigate-structs-lanemarkings">LaneMarkings</a>
  - <a href="sdk-for-ios-navigate-enums-lanedirection">LaneDirection</a>

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

