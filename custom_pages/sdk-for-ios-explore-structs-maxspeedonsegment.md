---
title: "MaxSpeedOnSegment Structure Reference"
slug: "sdk-for-ios-explore-structs-maxspeedonsegment"
---

# MaxSpeedOnSegment

<div class="declaration">

<div class="language">

``` highlight
public struct MaxSpeedOnSegment : Hashable
```

</div>

</div>

New base speed for a segment. Affects route calculation and the ETA. Cannot increase base speed on segment.

**Note:** This option can only be used with the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a>. The <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is not supported and the option will be ignored. Note that the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is only available for the Navigate license.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17MaxSpeedOnSegmentV7segmentAA0E9ReferenceVvp"></span>` `<span id="//apple_ref/swift/Property/segment" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-maxspeedonsegment#/s:7heresdk17MaxSpeedOnSegmentV7segmentAA0E9ReferenceVvp" class="token"><code>segment</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A segment for which the new base speed is specified. Only the `segmendId` and `travelDirection` parameters are used, other parameters are ignored. Setting a `segmendId` is mandatory.

  **Note:** The <a href="sdk-for-ios-explore-structs-segmentreference">`SegmentReference`</a> is not directly accessible from the map via the HERE SDK. Although, after route calculation you can retrieve the related segments for each <a href="sdk-for-ios-explore-classes-span">`Span`</a>. The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>. These IDs are mostly stable and only change when the underlying map data changes due to a new road or similar changes in the real world.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segment: SegmentReference
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17MaxSpeedOnSegmentV04baseC17InMetersPerSecondSdvp"></span>` `<span id="//apple_ref/swift/Property/baseSpeedInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-maxspeedonsegment#/s:7heresdk17MaxSpeedOnSegmentV04baseC17InMetersPerSecondSdvp" class="token"><code>baseSpeedInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  New maximum value in m/s of baseSpeed on segment. The provided value must be in the range \[1.0, 70.0\]. Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var baseSpeedInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(segment: baseSpeedInMetersPerSecond: )

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

    - segment: A segment for which the new base speed is specified. Only the `segmendId` and `travelDirection` parameters are used, other parameters are ignored. Setting a `segmendId` is mandatory.

    **Note:** The <a href="sdk-for-ios-explore-structs-segmentreference">`SegmentReference`</a> is not directly accessible from the map via the HERE SDK. Although, after route calculation you can retrieve the related segments for each <a href="sdk-for-ios-explore-classes-span">`Span`</a>. The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>. These IDs are mostly stable and only change when the underlying map data changes due to a new road or similar changes in the real world.

    - baseSpeedInMetersPerSecond: New maximum value in m/s of baseSpeed on segment. The provided value must be in the range \[1.0, 70.0\]. Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( segment : SegmentReference , baseSpeedInMetersPerSecond : Double )
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

