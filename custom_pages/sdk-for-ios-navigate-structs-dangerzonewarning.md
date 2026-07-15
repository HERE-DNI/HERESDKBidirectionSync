---
title: "DangerZoneWarning Structure Reference"
slug: "sdk-for-ios-navigate-structs-dangerzonewarning"
---

# DangerZoneWarning

<div class="declaration">

<div class="language">

``` highlight
public struct DangerZoneWarning : Hashable
```

</div>

</div>

Represents danger zones. A danger zone refers to areas where there is an increased risk of traffic incidents. These zones are designated to alert drivers to potential hazards and encourage safer driving behaviors. Legally, certain devices can alert you to being in a danger zone, typically indicating the presence of a speed camera. In line with applicable law and industry standard, these alerts are usually provided along a road within a range of 4 km on a motorway, 2 km outside built-up areas, and 300 m in built-up areas​​. The HERE SDK warns when approaching the danger zone, as well as when leaving such a zone. A danger zone may or may not have one or more speed cameras in it. The exact location of such speed cameras is not provided. Note that danger zones are only available in selected countries, such as France.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17DangerZoneWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-dangerzonewarning#/s:7heresdk17DangerZoneWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific danger zone warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

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

  ` `<span id="/s:7heresdk17DangerZoneWarningV02isC5StartSbvp"></span>` `<span id="//apple_ref/swift/Property/isZoneStart" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-dangerzonewarning#/s:7heresdk17DangerZoneWarningV02isC5StartSbvp" class="token"><code>isZoneStart</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag indicating whether the Danger Zone officially start in the location the user is entering it.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isZoneStart: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17DangerZoneWarningV16distanceInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-dangerzonewarning#/s:7heresdk17DangerZoneWarningV16distanceInMetersSdvp" class="token"><code>distanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance from the current location to the Danger zone.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17DangerZoneWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-dangerzonewarning#/s:7heresdk17DangerZoneWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the specified zone is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-ios-navigate-structs-dangerzonewarning#/s:7heresdk17DangerZoneWarningV16distanceInMetersSdvp">`DangerZoneWarning.distanceInMeters`</a> is greater than 0.

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

      init(id: isZoneStart: distanceInMeters: distanceType: )

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
  public init ( id : Int32 = 0 , isZoneStart : Bool , distanceInMeters : Double , distanceType : DistanceType )
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

