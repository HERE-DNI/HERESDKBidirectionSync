---
title: "Milestone Structure Reference"
slug: "sdk-for-ios-explore-structs-milestone"
---

# Milestone

<div class="declaration">

<div class="language">

``` highlight
public struct Milestone : Hashable
```

</div>

</div>

Represents information about the waypoints along the route.

Note that this can include additional waypoints added during route calculation that may not have been part of the original user-defined waypoint list. For example, additional waypoints are added automatically between sections that require a different transport mode like when taking a ferry.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk9MilestoneV12sectionIndexs5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/sectionIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-milestone#/s:7heresdk9MilestoneV12sectionIndexs5Int32Vvp" class="token"><code>sectionIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Index of the section on the route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sectionIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MilestoneV13waypointIndexs5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/waypointIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-milestone#/s:7heresdk9MilestoneV13waypointIndexs5Int32VSgvp" class="token"><code>waypointIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If present, this index corresponds to the waypoint in the original user-defined waypoint list. Otherwise this waypoint was added during route calculation by the system.

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

  ` `<span id="/s:7heresdk9MilestoneV19originalCoordinatesAA03GeoD0VSgvp"></span>` `<span id="//apple_ref/swift/Property/originalCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-milestone#/s:7heresdk9MilestoneV19originalCoordinatesAA03GeoD0VSgvp" class="token"><code>originalCoordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  User-defined geographic coordinates. If not available, this waypoint was added during route calculation.

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

  ` `<span id="/s:7heresdk9MilestoneV21mapMatchedCoordinatesAA03GeoE0Vvp"></span>` `<span id="//apple_ref/swift/Property/mapMatchedCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-milestone#/s:7heresdk9MilestoneV21mapMatchedCoordinatesAA03GeoE0Vvp" class="token"><code>mapMatchedCoordinates</code></a>` `

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

  ` `<span id="/s:7heresdk9MilestoneV4typeAA0B4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-milestone#/s:7heresdk9MilestoneV4typeAA0B4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of this Milestone

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: MilestoneType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(sectionIndex: waypointIndex: originalCoordinates: mapMatchedCoordinates: type: )

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
  public init ( sectionIndex : Int32 , waypointIndex : Int32 ? = nil , originalCoordinates : GeoCoordinates ? = nil , mapMatchedCoordinates : GeoCoordinates , type : MilestoneType = MilestoneType . stopover )
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

