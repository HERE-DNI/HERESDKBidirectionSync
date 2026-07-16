---
title: "SafetyCameraWarning Structure Reference"
slug: "sdk-for-ios-explore-structs-safetycamerawarning"
---

# SafetyCameraWarning

<div class="declaration">

<div class="language">

``` highlight
public struct SafetyCameraWarning : Hashable
```

</div>

</div>

A struct that provides safety camera warning information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV2ids5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-safetycamerawarning#sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV2ids5Int32Vvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific safety camera warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

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

   <span id="sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV010distanceToC8InMetersSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-distanceToCameraInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-safetycamerawarning#sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV010distanceToC8InMetersSdvp" class="token"><code>distanceToCameraInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the safety camera in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToCameraInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV27speedLimitInMetersPerSecondSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-speedLimitInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-safetycamerawarning#sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV27speedLimitInMetersPerSecondSdvp" class="token"><code>speedLimitInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The speed limit observed by the safety camera.

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

   <span id="sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV4typeAA0bC4TypeOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-safetycamerawarning#sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV4typeAA0bC4TypeOvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of the safety camera element.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: SafetyCameraType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-safetycameratype">SafetyCameraType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV12distanceTypeAA08DistanceF0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-distanceType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-safetycamerawarning#sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type of the warning (e.g.: warning for a new safety camera ahead, warning for passing a safety camera). Since the safety camera warning is given relative to a single position on the route, <a href="sdk-for-ios-explore-enums-distancetype#sdk-for-ios-explore-s-7heresdk12DistanceTypeO7reachedyA2CmF">`DistanceType.reached`</a> will never be given for this warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-distancetype">DistanceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV2id010distanceToC8InMeters010speedLimithI9PerSecond4type0F4TypeACs5Int32V_S2dAA0bcO0OAA08DistanceO0Otcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-id-distanceToCameraInMeters-speedLimitInMetersPerSecond-type-distanceType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-safetycamerawarning#sdk-for-ios-explore-s-7heresdk19SafetyCameraWarningV2id010distanceToC8InMeters010speedLimithI9PerSecond4type0F4TypeACs5Int32V_S2dAA0bcO0OAA08DistanceO0Otcfc" class="token"><code>init(id:</code><wbr></wbr><code>distanceToCameraInMeters:</code><wbr></wbr><code>speedLimitInMetersPerSecond:</code><wbr></wbr><code>type:</code><wbr></wbr><code>distanceType:</code><wbr></wbr><code>)</code></a> 

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
  public init(id: Int32 = 0, distanceToCameraInMeters: Double, speedLimitInMetersPerSecond: Double, type: SafetyCameraType, distanceType: DistanceType)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-safetycameratype">SafetyCameraType</a>
  - <a href="sdk-for-ios-explore-enums-distancetype">DistanceType</a>

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

