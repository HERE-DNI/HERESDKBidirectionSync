---
title: "SpeedLimitOffset Structure Reference"
slug: "sdk-for-ios-navigate-structs-speedlimitoffset"
---

# SpeedLimitOffset

<div class="declaration">

<div class="language">

``` highlight
public struct SpeedLimitOffset : Hashable
```

</div>

</div>

A struct that represents two separate speed limit offsets for higher and lower speed limits. A driver will be notified when the current driving speed is above the speed limit + offset. Only one of the two offsets is used depending on the current speed limit.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lowSpeedOffsetInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-speedlimitoffset#sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecondSdvp" class="token"><code>lowSpeedOffsetInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A speed limit offset for speed limits below the <a href="sdk-for-ios-navigate-structs-speedlimitoffset#sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp">`SpeedLimitOffset.highSpeedBoundaryInMetersPerSecond`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lowSpeedOffsetInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV04highbD17InMetersPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-highSpeedOffsetInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-speedlimitoffset#sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV04highbD17InMetersPerSecondSdvp" class="token"><code>highSpeedOffsetInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A speed limit offset for speed limits above the <a href="sdk-for-ios-navigate-structs-speedlimitoffset#sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp">`SpeedLimitOffset.highSpeedBoundaryInMetersPerSecond`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var highSpeedOffsetInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-highSpeedBoundaryInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-speedlimitoffset#sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV04highB25BoundaryInMetersPerSecondSdvp" class="token"><code>highSpeedBoundaryInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The boundary that defines higher and lower speed limits.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var highSpeedBoundaryInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecond04highbdfghI00jb8BoundaryfghI0ACSd_S2dtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-lowSpeedOffsetInMetersPerSecond-highSpeedOffsetInMetersPerSecond-highSpeedBoundaryInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-speedlimitoffset#sdk-for-ios-navigate-s-7heresdk16SpeedLimitOffsetV03lowbD17InMetersPerSecond04highbdfghI00jb8BoundaryfghI0ACSd_S2dtcfc" class="token"><code>init(lowSpeedOffsetInMetersPerSecond:</code><wbr></wbr><code>highSpeedOffsetInMetersPerSecond:</code><wbr></wbr><code>highSpeedBoundaryInMetersPerSecond:</code><wbr></wbr><code>)</code></a> 

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
  public init(lowSpeedOffsetInMetersPerSecond: Double = 0.0, highSpeedOffsetInMetersPerSecond: Double = 0.0, highSpeedBoundaryInMetersPerSecond: Double = 0.0)
  ```

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

