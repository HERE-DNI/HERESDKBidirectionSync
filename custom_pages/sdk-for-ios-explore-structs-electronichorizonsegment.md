---
title: "ElectronicHorizonSegment Structure Reference"
slug: "sdk-for-ios-explore-structs-electronichorizonsegment"
---

# ElectronicHorizonSegment

<div class="declaration">

<div class="language">

``` highlight
public struct ElectronicHorizonSegment : Hashable
```

</div>

</div>

Represents a segment in an <a href="sdk-for-ios-explore-structs-electronichorizonpath">`ElectronicHorizonPath`</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV9segmentIdAA0bcdF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-segmentId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-electronichorizonsegment#sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV9segmentIdAA0bcdF0Vvp" class="token"><code>segmentId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique identifier of the segment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentId: ElectronicHorizonSegmentId
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV15parentPathIndexs5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-parentPathIndex" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-electronichorizonsegment#sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV15parentPathIndexs5Int32Vvp" class="token"><code>parentPathIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The index of the parent path.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parentPathIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV19startOffsetInMetersSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-startOffsetInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-electronichorizonsegment#sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV19startOffsetInMetersSdvp" class="token"><code>startOffsetInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The start offset from the beginning of the most preferred path in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startOffsetInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV17endOffsetInMetersSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-endOffsetInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-electronichorizonsegment#sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV17endOffsetInMetersSdvp" class="token"><code>endOffsetInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The end offset from the beginning of the most preferred path in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var endOffsetInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV15sidePathIndexesSays5Int32VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sidePathIndexes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-electronichorizonsegment#sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV15sidePathIndexesSays5Int32VGvp" class="token"><code>sidePathIndexes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of indexes of the paths that branch off at the end of this segment. The list can be empty when no side paths branch off at this segment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sidePathIndexes: [Int32]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV9segmentId15parentPathIndex19startOffsetInMeters03endklM004sideH7IndexesAcA0bcdF0V_s5Int32VS2dSayALGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-segmentId-parentPathIndex-startOffsetInMeters-endOffsetInMeters-sidePathIndexes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-electronichorizonsegment#sdk-for-ios-explore-s-7heresdk24ElectronicHorizonSegmentV9segmentId15parentPathIndex19startOffsetInMeters03endklM004sideH7IndexesAcA0bcdF0V_s5Int32VS2dSayALGtcfc" class="token"><code>init(segmentId:</code><wbr></wbr><code>parentPathIndex:</code><wbr></wbr><code>startOffsetInMeters:</code><wbr></wbr><code>endOffsetInMeters:</code><wbr></wbr><code>sidePathIndexes:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  Offline availability: This property is available online and offline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(segmentId: ElectronicHorizonSegmentId, parentPathIndex: Int32, startOffsetInMeters: Double, endOffsetInMeters: Double, sidePathIndexes: [Int32] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a>

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

