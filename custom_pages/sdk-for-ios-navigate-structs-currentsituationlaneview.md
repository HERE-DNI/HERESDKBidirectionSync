---
title: "CurrentSituationLaneView Structure Reference"
slug: "sdk-for-ios-navigate-structs-currentsituationlaneview"
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

  ` `<span id="/s:7heresdk24CurrentSituationLaneViewV6accessAA0D6AccessVvp"></span>` `<span id="//apple_ref/swift/Property/access" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-currentsituationlaneview#/s:7heresdk24CurrentSituationLaneViewV6accessAA0D6AccessVvp" class="token"><code>access</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24CurrentSituationLaneViewV17directionCategoryAA0d9DirectionG0Vvp"></span>` `<span id="//apple_ref/swift/Property/directionCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-currentsituationlaneview#/s:7heresdk24CurrentSituationLaneViewV17directionCategoryAA0d9DirectionG0Vvp" class="token"><code>directionCategory</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24CurrentSituationLaneViewV4typeAA0D4TypeVvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-currentsituationlaneview#/s:7heresdk24CurrentSituationLaneViewV4typeAA0D4TypeVvp" class="token"><code>type</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24CurrentSituationLaneViewV12laneMarkingsAA0dG0Vvp"></span>` `<span id="//apple_ref/swift/Property/laneMarkings" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-currentsituationlaneview#/s:7heresdk24CurrentSituationLaneViewV12laneMarkingsAA0dG0Vvp" class="token"><code>laneMarkings</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24CurrentSituationLaneViewV10directionsSayAA0D9DirectionOGvp"></span>` `<span id="//apple_ref/swift/Property/directions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-currentsituationlaneview#/s:7heresdk24CurrentSituationLaneViewV10directionsSayAA0D9DirectionOGvp" class="token"><code>directions</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24CurrentSituationLaneViewV17directionsOnRouteSayAA0D9DirectionOGvp"></span>` `<span id="//apple_ref/swift/Property/directionsOnRoute" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-currentsituationlaneview#/s:7heresdk24CurrentSituationLaneViewV17directionsOnRouteSayAA0D9DirectionOGvp" class="token"><code>directionsOnRoute</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

      init(access: directionCategory: type: laneMarkings: directions: directionsOnRoute: )

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
  public init ( access : LaneAccess , directionCategory : LaneDirectionCategory , type : LaneType , laneMarkings : LaneMarkings = LaneMarkings (), directions : [ LaneDirection ] = [], directionsOnRoute : [ LaneDirection ] = [])
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

