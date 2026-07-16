---
title: "WarningNotificationDistances Structure Reference"
slug: "sdk-for-ios-explore-structs-warningnotificationdistances"
---

# WarningNotificationDistances

<div class="declaration">

<div class="language">

``` highlight
public struct WarningNotificationDistances : Hashable
```

</div>

</div>

Distances for emitting warnings according to the timing profile.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-slowSpeedDistanceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warningnotificationdistances#sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeterss5Int32Vvp" class="token"><code>slowSpeedDistanceInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance in meters for emitting warnings when the speed limit or current speed is slow. The conditions for a speed to be considered slow are the same ones as for `TimingProfile.SLOW_SPEED`. The distance should be greater than 0. Defaults to 500 meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var slowSpeedDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV28regularSpeedDistanceInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-regularSpeedDistanceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warningnotificationdistances#sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV28regularSpeedDistanceInMeterss5Int32Vvp" class="token"><code>regularSpeedDistanceInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance in meters for emitting warnings when the speed limit or current speed is regular. The conditions for a speed to be considered regular are the same ones as for `TimingProfile.REGULAR_SPEED`. The distance should be greater than 0. Defaults to 750 meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var regularSpeedDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV25fastSpeedDistanceInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-fastSpeedDistanceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warningnotificationdistances#sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV25fastSpeedDistanceInMeterss5Int32Vvp" class="token"><code>fastSpeedDistanceInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance in meters for emitting warnings when the speed limit or current speed is fast. The conditions for a speed to be considered fast are the same ones as for `TimingProfile.FAST_SPEED`. The distance should be greater than 0. Defaults to 1500 meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fastSpeedDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeters07regularfghI004fastfghI0ACs5Int32V_A2Htcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-slowSpeedDistanceInMeters-regularSpeedDistanceInMeters-fastSpeedDistanceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-warningnotificationdistances#sdk-for-ios-explore-s-7heresdk28WarningNotificationDistancesV25slowSpeedDistanceInMeters07regularfghI004fastfghI0ACs5Int32V_A2Htcfc" class="token"><code>init(slowSpeedDistanceInMeters:</code><wbr></wbr><code>regularSpeedDistanceInMeters:</code><wbr></wbr><code>fastSpeedDistanceInMeters:</code><wbr></wbr><code>)</code></a> 

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
  public init(slowSpeedDistanceInMeters: Int32 = 500, regularSpeedDistanceInMeters: Int32 = 750, fastSpeedDistanceInMeters: Int32 = 1500)
  ```

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

