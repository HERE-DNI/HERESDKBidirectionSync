---
title: "TollStop Structure Reference"
slug: "sdk-for-ios-navigate-structs-tollstop"
---

# TollStop

<div class="declaration">

<div class="language">

``` highlight
public struct TollStop : Hashable
```

</div>

</div>

A struct that provides information for a toll stop with multiple toll booths.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8TollStopV2ids5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstop#sdk-for-ios-navigate-s-7heresdk8TollStopV2ids5Int32Vvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific toll stop warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

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

   <span id="sdk-for-ios-navigate-s-7heresdk8TollStopV12distanceTypeAA08DistanceE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-distanceType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstop#sdk-for-ios-navigate-s-7heresdk8TollStopV12distanceTypeAA08DistanceE0Ovp" class="token"><code>distanceType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the specified toll stop is ahead of the vehicle or has just passed by.

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

  - <a href="sdk-for-ios-navigate-enums-distancetype">DistanceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8TollStopV010distanceTobC8InMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-distanceToTollStopInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstop#sdk-for-ios-navigate-s-7heresdk8TollStopV010distanceTobC8InMetersSdvp" class="token"><code>distanceToTollStopInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the toll stop in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToTollStopInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8TollStopV5lanesSayAA0B9BoothLaneVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lanes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstop#sdk-for-ios-navigate-s-7heresdk8TollStopV5lanesSayAA0B9BoothLaneVGvp" class="token"><code>lanes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the features of the booth for the lane. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

  **Note:** Lanes going in opposite direction are not included in the list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lanes: [TollBoothLane]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-tollboothlane">TollBoothLane</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8TollStopV2id12distanceType0e2TobC8InMeters5lanesACs5Int32V_AA08DistanceF0OSdSayAA0B9BoothLaneVGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-id-distanceType-distanceToTollStopInMeters-lanes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-tollstop#sdk-for-ios-navigate-s-7heresdk8TollStopV2id12distanceType0e2TobC8InMeters5lanesACs5Int32V_AA08DistanceF0OSdSayAA0B9BoothLaneVGtcfc" class="token"><code>init(id:</code><wbr></wbr><code>distanceType:</code><wbr></wbr><code>distanceToTollStopInMeters:</code><wbr></wbr><code>lanes:</code><wbr></wbr><code>)</code></a> 

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

    - id: Unique identifier for this specific toll stop warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.
    - distanceType: Indicates if the specified toll stop is ahead of the vehicle or has just passed by.
    - distanceToTollStopInMeters: Distance to the toll stop in meters.
    - lanes: Describes the features of the booth for the lane. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

    **Note:** Lanes going in opposite direction are not included in the list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(id: Int32 = 0, distanceType: DistanceType, distanceToTollStopInMeters: Double, lanes: [TollBoothLane])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-distancetype">DistanceType</a>
  - <a href="sdk-for-ios-navigate-structs-tollboothlane">TollBoothLane</a>

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

