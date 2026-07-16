---
title: "TransitDeparture Structure Reference"
slug: "sdk-for-ios-explore-structs-transitdeparture"
---

# TransitDeparture

<div class="declaration">

<div class="language">

``` highlight
public struct TransitDeparture : Hashable
```

</div>

</div>

This struct holds the transit departure or arrival information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TransitDepartureV5placeAA10RoutePlaceVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-place" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitdeparture#sdk-for-ios-explore-s-7heresdk16TransitDepartureV5placeAA10RoutePlaceVvp" class="token"><code>place</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The departure or arrival place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var place: RoutePlace
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routeplace">RoutePlace</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TransitDepartureV4time10Foundation4DateVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-time" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitdeparture#sdk-for-ios-explore-s-7heresdk16TransitDepartureV4time10Foundation4DateVSgvp" class="token"><code>time</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Expected departure or arrival time of the event.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var time: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TransitDepartureV5delays5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-delay" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitdeparture#sdk-for-ios-explore-s-7heresdk16TransitDepartureV5delays5Int32VSgvp" class="token"><code>delay</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The accumulated delay in seconds from the scheduled time of the event.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var delay: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TransitDepartureV6statusAA0bC6StatusOSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-status" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitdeparture#sdk-for-ios-explore-s-7heresdk16TransitDepartureV6statusAA0bC6StatusOSgvp" class="token"><code>status</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Status of the departure.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var status: TransitDepartureStatus?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transitdeparturestatus">TransitDepartureStatus</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TransitDepartureV5place4time5delay6statusAcA10RoutePlaceV_10Foundation4DateVSgs5Int32VSgAA0bC6StatusOSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-place-time-delay-status" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitdeparture#sdk-for-ios-explore-s-7heresdk16TransitDepartureV5place4time5delay6statusAcA10RoutePlaceV_10Foundation4DateVSgs5Int32VSgAA0bC6StatusOSgtcfc" class="token"><code>init(place:</code><wbr></wbr><code>time:</code><wbr></wbr><code>delay:</code><wbr></wbr><code>status:</code><wbr></wbr><code>)</code></a> 

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
  public init(place: RoutePlace, time: Date? = nil, delay: Int32? = nil, status: TransitDepartureStatus? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routeplace">RoutePlace</a>
  - <a href="sdk-for-ios-explore-enums-transitdeparturestatus">TransitDepartureStatus</a>

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

