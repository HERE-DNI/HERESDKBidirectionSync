---
title: "LowSpeedZoneWarning Structure Reference"
slug: "sdk-for-ios-navigate-structs-lowspeedzonewarning"
---

# LowSpeedZoneWarning

<div class="declaration">

<div class="language">

``` highlight
public struct LowSpeedZoneWarning : Hashable
```

</div>

</div>

A struct that provides low speed zone. The main field describing the low speed zone is `LowSpeedZoneWarning.speed_limit_in_meters_per_second` specifying the speed limit of the low speed zone. Use `LowSpeedZoneWarningListener` to get notifications about upcoming low speed zones.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk19LowSpeedZoneWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lowspeedzonewarning#/s:7heresdk19LowSpeedZoneWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific low speed zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

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

  ` `<span id="/s:7heresdk19LowSpeedZoneWarningV010distanceTobcD8InMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceToLowSpeedZoneInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lowspeedzonewarning#/s:7heresdk19LowSpeedZoneWarningV010distanceTobcD8InMetersSdvp" class="token"><code>distanceToLowSpeedZoneInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the low speed warning in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToLowSpeedZoneInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LowSpeedZoneWarningV27speedLimitInMetersPerSecondSdvp"></span>` `<span id="//apple_ref/swift/Property/speedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lowspeedzonewarning#/s:7heresdk19LowSpeedZoneWarningV27speedLimitInMetersPerSecondSdvp" class="token"><code>speedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Speed limit of the low speed zone.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedLimitInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LowSpeedZoneWarningV12distanceTypeAA08DistanceG0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lowspeedzonewarning#/s:7heresdk19LowSpeedZoneWarningV12distanceTypeAA08DistanceG0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type for the warning, e.g. a warning for a new low speed zone ahead or a warning for passing a low speed zone.

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

  ` `<span id="/s:7heresdk19LowSpeedZoneWarningV16segmentReferenceAA07SegmentG0Vvp"></span>` `<span id="//apple_ref/swift/Property/segmentReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lowspeedzonewarning#/s:7heresdk19LowSpeedZoneWarningV16segmentReferenceAA07SegmentG0Vvp" class="token"><code>segmentReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The reference to the segment where the low speed zone is located. It can be used to identify the location.

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

      init(id: distanceToLowSpeedZoneInMeters: speedLimitInMetersPerSecond: distanceType: segmentReference: )

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
  public init ( id : Int32 = 0 , distanceToLowSpeedZoneInMeters : Double , speedLimitInMetersPerSecond : Double , distanceType : DistanceType , segmentReference : SegmentReference )
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

