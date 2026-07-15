---
title: "RailwayCrossing Structure Reference"
slug: "sdk-for-ios-navigate-structs-railwaycrossing"
---

# RailwayCrossing

<div class="declaration">

<div class="language">

``` highlight
public struct RailwayCrossing
```

</div>

</div>

Identifies the presence and the location of railway corssings. Included in <a href="sdk-for-ios-navigate-classes-segmentdata">`SegmentData`</a> only if <a href="sdk-for-ios-navigate-structs-segmentdataloaderoptions#/s:7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">`SegmentDataLoaderOptions.loadRailwayCrossings`</a> is set to `true`.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/startOffsetInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp" class="token"><code>startOffsetInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The start offset, in meters, from the beginning of the segment.

  If <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">`RailwayCrossing.endOffsetInMeters`</a> = 0, then `RailwayCrossing.startOffsetInMeters` approximately indicates a middle of a railway crossing. If <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">`RailwayCrossing.endOffsetInMeters`</a> \> 0, it means crossing consists of several rails, and `RailwayCrossing.startOffsetInMeters` and <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">`RailwayCrossing.endOffsetInMeters`</a> indicates starting and ending points of the crossing respectively. Default value is 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startOffsetInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/endOffsetInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp" class="token"><code>endOffsetInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The end offset, in meters, from the beginning of the segment. Could be 0. See <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">`RailwayCrossing.startOffsetInMeters`</a> description. Default value is 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var endOffsetInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RailwayCrossingV07railwayC4TypeAA0bcE0Ovp"></span>` `<span id="//apple_ref/swift/Property/railwayCrossingType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV07railwayC4TypeAA0bcE0Ovp" class="token"><code>railwayCrossingType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of barrier presented by the railway crossing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var railwayCrossingType: RailwayCrossingType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(startOffsetInMeters: endOffsetInMeters: railwayCrossingType: )

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

    - startOffsetInMeters: The start offset, in meters, from the beginning of the segment.

    If <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">`RailwayCrossing.endOffsetInMeters`</a> = 0, then <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">`RailwayCrossing.startOffsetInMeters`</a> approximately indicates a middle of a railway crossing. If <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">`RailwayCrossing.endOffsetInMeters`</a> \> 0, it means crossing consists of several rails, and <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">`RailwayCrossing.startOffsetInMeters`</a> and <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">`RailwayCrossing.endOffsetInMeters`</a> indicates starting and ending points of the crossing respectively. Default value is 0.

    - endOffsetInMeters: The end offset, in meters, from the beginning of the segment. Could be 0. See <a href="sdk-for-ios-navigate-structs-railwaycrossing#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">`RailwayCrossing.startOffsetInMeters`</a> description. Default value is 0.
    - railwayCrossingType: The type of barrier presented by the railway crossing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( startOffsetInMeters : Int32 = 0 , endOffsetInMeters : Int32 = 0 , railwayCrossingType : RailwayCrossingType )
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

