---
title: "TollStructureManeuver Structure Reference"
slug: "sdk-for-ios-navigate-structs-tollstructuremaneuver"
---

# TollStructureManeuver

<div class="declaration">

<div class="language">

``` highlight
public struct TollStructureManeuver
```

</div>

</div>

A struct that provides information for a toll structure at a toll point.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV04tollC0AA0bC0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tollStructure" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstructuremaneuver#sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV04tollC0AA0bC0VSgvp" class="token"><code>tollStructure</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Toll structure properties Could be empty for checkpoint not related to toll.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tollStructure: TollStructure?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-tollstructure">TollStructure</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV12isCheckpointSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isCheckpoint" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstructuremaneuver#sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV12isCheckpointSbvp" class="token"><code>isCheckpoint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle Checkpoint identifies locations on the through route, where vehicles are required to slow down/stop with the intended purpose of inspecting vehicles to deter illegal immigration and smuggling activities, to perform customs/passport checks, toll payment, etc. This is not limited to border locations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isCheckpoint: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV12destinationsSayAA20DirectedOCMSegmentIdVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-destinations" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstructuremaneuver#sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV12destinationsSayAA20DirectedOCMSegmentIdVGvp" class="token"><code>destinations</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional destinations segment references. Destination shows for which exactly outgoing segment current toll/checkpoint is applied. Empty if structure applied to all outgoing connected segments.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var destinations: [DirectedOCMSegmentId]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-directedocmsegmentid">DirectedOCMSegmentId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV15etcGuidanceFileAA0G9ReferenceVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-etcGuidanceFile" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstructuremaneuver#sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV15etcGuidanceFileAA0G9ReferenceVSgvp" class="token"><code>etcGuidanceFile</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional image providing guidance through an electronic toll collection (ETC) point.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var etcGuidanceFile: FileReference?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-filereference">FileReference</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV04tollC012isCheckpoint12destinations15etcGuidanceFileAcA0bC0VSg_SbSayAA20DirectedOCMSegmentIdVGAA0K9ReferenceVSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-tollStructure-isCheckpoint-destinations-etcGuidanceFile" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstructuremaneuver#sdk-for-ios-navigate-s-7heresdk21TollStructureManeuverV04tollC012isCheckpoint12destinations15etcGuidanceFileAcA0bC0VSg_SbSayAA20DirectedOCMSegmentIdVGAA0K9ReferenceVSgtcfc" class="token"><code>init(tollStructure:</code><wbr></wbr><code>isCheckpoint:</code><wbr></wbr><code>destinations:</code><wbr></wbr><code>etcGuidanceFile:</code><wbr></wbr><code>)</code></a> 

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
  public init(tollStructure: TollStructure? = nil, isCheckpoint: Bool = false, destinations: [DirectedOCMSegmentId], etcGuidanceFile: FileReference? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-tollstructure">TollStructure</a>
  - <a href="sdk-for-ios-navigate-structs-directedocmsegmentid">DirectedOCMSegmentId</a>
  - <a href="sdk-for-ios-navigate-structs-filereference">FileReference</a>

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

