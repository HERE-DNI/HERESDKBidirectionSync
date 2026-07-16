---
title: "DynamicSpeedInfo Structure Reference"
slug: "sdk-for-ios-explore-structs-dynamicspeedinfo"
---

# DynamicSpeedInfo

<div class="declaration">

<div class="language">

``` highlight
public struct DynamicSpeedInfo : Hashable
```

</div>

</div>

Provides estimated speed information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-baseSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-dynamicspeedinfo#sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp" class="token"><code>baseSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The speed in meters per second without taking traffic into consideration.

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

   <span id="sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV07trafficC17InMetersPerSecondSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-dynamicspeedinfo#sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV07trafficC17InMetersPerSecondSdvp" class="token"><code>trafficSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The speed in meters per second considering traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficSpeedInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV17turnTimeInSecondss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-turnTimeInSeconds" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-dynamicspeedinfo#sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV17turnTimeInSecondss5Int32Vvp" class="token"><code>turnTimeInSeconds</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time it takes to make a turn, represented in seconds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var turnTimeInSeconds: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecond07trafficcfghI008turnTimeF7SecondsACSd_Sds5Int32Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-baseSpeedInMetersPerSecond-trafficSpeedInMetersPerSecond-turnTimeInSeconds" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-dynamicspeedinfo#sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecond07trafficcfghI008turnTimeF7SecondsACSd_Sds5Int32Vtcfc" class="token"><code>init(baseSpeedInMetersPerSecond:</code><wbr></wbr><code>trafficSpeedInMetersPerSecond:</code><wbr></wbr><code>turnTimeInSeconds:</code><wbr></wbr><code>)</code></a> 

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
  public init(baseSpeedInMetersPerSecond: Double, trafficSpeedInMetersPerSecond: Double, turnTimeInSeconds: Int32)
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV18calculateJamFactorSdyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-calculateJamFactor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-dynamicspeedinfo#sdk-for-ios-explore-s-7heresdk16DynamicSpeedInfoV18calculateJamFactorSdyF" class="token"><code>calculateJamFactor()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Calculates the traffic jam factor that shows the traffic condition in a numeric way.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func calculateJamFactor() -> Double
  ```

  </div>

  </div>

  <div>

  #### Return Value

  Returns calculated jam factor in the range \[0.0, 10.0\]. A large jamFactor value means more traffic jam in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.

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

