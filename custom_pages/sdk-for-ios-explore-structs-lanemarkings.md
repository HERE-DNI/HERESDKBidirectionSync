---
title: "LaneMarkings Structure Reference"
slug: "sdk-for-ios-explore-structs-lanemarkings"
---

# LaneMarkings

<div class="declaration">

<div class="language">

``` highlight
public struct LaneMarkings : Hashable
```

</div>

</div>

A struct that provides information for the lane markings.

Lane markings indicate the markings on the road.

Lane Divider Marker indicates the lane separator on the right side of the specified lane in the lane driving direction for Right-side driving countries. For left-sided driving countries the Lane Divider Marker is indicating the lane separator on the left side of the specified lane in the lane driving direction.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12LaneMarkingsV19centerDividerMarkerAA0eF0OSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-centerDividerMarker" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-lanemarkings#sdk-for-ios-explore-s-7heresdk12LaneMarkingsV19centerDividerMarkerAA0eF0OSgvp" class="token"><code>centerDividerMarker</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Center Divider Marker describes the type of lane separator for center dividers on bidirectional roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var centerDividerMarker: DividerMarker?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-dividermarker">DividerMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12LaneMarkingsV17laneDividerMarkerAA0eF0OSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-laneDividerMarker" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-lanemarkings#sdk-for-ios-explore-s-7heresdk12LaneMarkingsV17laneDividerMarkerAA0eF0OSgvp" class="token"><code>laneDividerMarker</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Lane Divider Marker describes the appearance and type of driving lane separators existing on a road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var laneDividerMarker: DividerMarker?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-dividermarker">DividerMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12LaneMarkingsV10directionsSayAA0B9DirectionOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-directions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-lanemarkings#sdk-for-ios-explore-s-7heresdk12LaneMarkingsV10directionsSayAA0B9DirectionOGvp" class="token"><code>directions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of lane directions

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

   <span id="sdk-for-ios-explore-s-7heresdk12LaneMarkingsV19centerDividerMarker04laneeF010directionsAcA0eF0OSg_AISayAA0B9DirectionOGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-centerDividerMarker-laneDividerMarker-directions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-lanemarkings#sdk-for-ios-explore-s-7heresdk12LaneMarkingsV19centerDividerMarker04laneeF010directionsAcA0eF0OSg_AISayAA0B9DirectionOGtcfc" class="token"><code>init(centerDividerMarker:</code><wbr></wbr><code>laneDividerMarker:</code><wbr></wbr><code>directions:</code><wbr></wbr><code>)</code></a> 

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
  public init(centerDividerMarker: DividerMarker? = nil, laneDividerMarker: DividerMarker? = nil, directions: [LaneDirection] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-dividermarker">DividerMarker</a>
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

