---
title: "CurrentSituationLaneView Structure Reference"
slug: "sdk-for-ios-explore-structs-currentsituationlaneview"
---

# CurrentSituationLaneView

<div class="declaration">

<div class="language">

``` highlight
public struct CurrentSituationLaneView : Hashable
```

</div>

</div>

A struct that provides current situation lane assistance view information for the street at the current position of a single lane.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV6accessAA0D6AccessVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-access" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-currentsituationlaneview#sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV6accessAA0D6AccessVvp" class="token"><code>access</code></a> 

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

  - <a href="sdk-for-ios-explore-structs-laneaccess">LaneAccess</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV17directionCategoryAA0d9DirectionG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-directionCategory" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-currentsituationlaneview#sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV17directionCategoryAA0d9DirectionG0Vvp" class="token"><code>directionCategory</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates towards which directions this lane leads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var directionCategory: LaneDirectionCategory
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-lanedirectioncategory">LaneDirectionCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV4typeAA0D4TypeVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-currentsituationlaneview#sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV4typeAA0D4TypeVvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates this lane’s properties.

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

  - <a href="sdk-for-ios-explore-structs-lanetype">LaneType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV12laneMarkingsAA0dG0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-laneMarkings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-currentsituationlaneview#sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV12laneMarkingsAA0dG0Vvp" class="token"><code>laneMarkings</code></a> 

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

  - <a href="sdk-for-ios-explore-structs-lanemarkings">LaneMarkings</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV10directionsSayAA0D9DirectionOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-directions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-currentsituationlaneview#sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV10directionsSayAA0D9DirectionOGvp" class="token"><code>directions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates which lane directions are available for this lane.

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

  - <a href="sdk-for-ios-explore-enums-lanedirection">LaneDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV17directionsOnRouteSayAA0D9DirectionOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-directionsOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-currentsituationlaneview#sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV17directionsOnRouteSayAA0D9DirectionOGvp" class="token"><code>directionsOnRoute</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates which lane directions are on the route. Following those directions keeps the driver on the route.

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

  - <a href="sdk-for-ios-explore-enums-lanedirection">LaneDirection</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV6access17directionCategory4type12laneMarkings10directions0L7OnRouteAcA0D6AccessV_AA0d9DirectionH0VAA0D4TypeVAA0dK0VSayAA0dP0OGATtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-access-directionCategory-type-laneMarkings-directions-directionsOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-currentsituationlaneview#sdk-for-ios-explore-s-7heresdk24CurrentSituationLaneViewV6access17directionCategory4type12laneMarkings10directions0L7OnRouteAcA0D6AccessV_AA0d9DirectionH0VAA0D4TypeVAA0dK0VSayAA0dP0OGATtcfc" class="token"><code>init(access:</code><wbr></wbr><code>directionCategory:</code><wbr></wbr><code>type:</code><wbr></wbr><code>laneMarkings:</code><wbr></wbr><code>directions:</code><wbr></wbr><code>directionsOnRoute:</code><wbr></wbr><code>)</code></a> 

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
  public init(access: LaneAccess, directionCategory: LaneDirectionCategory, type: LaneType, laneMarkings: LaneMarkings = LaneMarkings(), directions: [LaneDirection] = [], directionsOnRoute: [LaneDirection] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-laneaccess">LaneAccess</a>
  - <a href="sdk-for-ios-explore-structs-lanedirectioncategory">LaneDirectionCategory</a>
  - <a href="sdk-for-ios-explore-structs-lanetype">LaneType</a>
  - <a href="sdk-for-ios-explore-structs-lanemarkings">LaneMarkings</a>
  - <a href="sdk-for-ios-explore-enums-lanedirection">LaneDirection</a>

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

