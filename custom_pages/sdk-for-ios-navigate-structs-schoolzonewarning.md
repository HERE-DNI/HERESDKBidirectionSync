---
title: "SchoolZoneWarning Structure Reference"
slug: "sdk-for-ios-navigate-structs-schoolzonewarning"
---

# SchoolZoneWarning

<div class="declaration">

<div class="language">

``` highlight
public struct SchoolZoneWarning : Hashable
```

</div>

</div>

A school zone warning which notifies about a school zone presence on road with a speed limit different than the default speed limit applicable for cars. Use `SchoolZoneWarningListener` to get notifications about school zones.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17SchoolZoneWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-schoolzonewarning#/s:7heresdk17SchoolZoneWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific school zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

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

  ` `<span id="/s:7heresdk17SchoolZoneWarningV010distanceTobC8InMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceToSchoolZoneInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-schoolzonewarning#/s:7heresdk17SchoolZoneWarningV010distanceTobC8InMetersSdvp" class="token"><code>distanceToSchoolZoneInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance from the current location to the school zone in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToSchoolZoneInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17SchoolZoneWarningV27speedLimitInMetersPerSecondSdvp"></span>` `<span id="//apple_ref/swift/Property/speedLimitInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-schoolzonewarning#/s:7heresdk17SchoolZoneWarningV27speedLimitInMetersPerSecondSdvp" class="token"><code>speedLimitInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Speed limit meters/second, which applies to current school zone.

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

  ` `<span id="/s:7heresdk17SchoolZoneWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-schoolzonewarning#/s:7heresdk17SchoolZoneWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type for the warning, e.g. a warning for a new school zone ahead or a warning for passing a school zone.

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

  ` `<span id="/s:7heresdk17SchoolZoneWarningV8timeRuleAA04TimeF0CSgvp"></span>` `<span id="//apple_ref/swift/Property/timeRule" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-schoolzonewarning#/s:7heresdk17SchoolZoneWarningV8timeRuleAA04TimeF0CSgvp" class="token"><code>timeRule</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time rule indicating the time periods for which the warning applies. If the field is ‘null’ then the warning is applicable at anytime.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeRule: TimeRule?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: distanceToSchoolZoneInMeters: speedLimitInMetersPerSecond: distanceType: timeRule: )

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
  public init ( id : Int32 = 0 , distanceToSchoolZoneInMeters : Double , speedLimitInMetersPerSecond : Double , distanceType : DistanceType , timeRule : TimeRule ? = nil )
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

