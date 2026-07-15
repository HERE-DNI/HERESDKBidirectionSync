---
title: "RailwayCrossingWarning Structure Reference"
slug: "sdk-for-ios-explore-structs-railwaycrossingwarning"
---

# RailwayCrossingWarning

<div class="declaration">

<div class="language">

``` highlight
public struct RailwayCrossingWarning : Hashable
```

</div>

</div>

A struct that provides railway crossing. The main field describing the railway crossing is <a href="sdk-for-ios-explore-structs-railwaycrossingwarning#/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp">`RailwayCrossingWarning.type`</a> specifying whether the railway crossing is protected by a barrier or not. Use `RailwayCrossingWarningListener` to get notifications about upcoming railway crossings.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk22RailwayCrossingWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-railwaycrossingwarning#/s:7heresdk22RailwayCrossingWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific railway crossing warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RailwayCrossingWarningV010distanceTobC8InMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceToRailwayCrossingInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-railwaycrossingwarning#/s:7heresdk22RailwayCrossingWarningV010distanceTobC8InMetersSdvp" class="token"><code>distanceToRailwayCrossingInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the railway crossing in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToRailwayCrossingInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-railwaycrossingwarning#/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of railway crossing, specifying whether it is protected by a barrier or not.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: RouteRailwayCrossingType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RailwayCrossingWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-railwaycrossingwarning#/s:7heresdk22RailwayCrossingWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type for the warning, e.g. a warning for a new railway crossing ahead or a warning for passing a railway crossing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22RailwayCrossingWarningV16segmentReferenceAA07SegmentF0Vvp"></span>` `<span id="//apple_ref/swift/Property/segmentReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-railwaycrossingwarning#/s:7heresdk22RailwayCrossingWarningV16segmentReferenceAA07SegmentF0Vvp" class="token"><code>segmentReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The reference to the segment where the railway crossing is located. It can be used to identify the location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentReference: SegmentReference
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: distanceToRailwayCrossingInMeters: type: distanceType: segmentReference: )

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
  public init ( id : Int32 = 0 , distanceToRailwayCrossingInMeters : Double , type : RouteRailwayCrossingType = RouteRailwayCrossingType . unknown , distanceType : DistanceType , segmentReference : SegmentReference )
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

