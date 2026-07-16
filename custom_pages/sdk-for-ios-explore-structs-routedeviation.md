---
title: "RouteDeviation Structure Reference"
slug: "sdk-for-ios-explore-structs-routedeviation"
---

# RouteDeviation

<div class="declaration">

<div class="language">

``` highlight
public struct RouteDeviation : Hashable
```

</div>

</div>

Contains all the relevant information on a deviation from the route.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14RouteDeviationV014lastLocationOnB0AA09NavigableE0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastLocationOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routedeviation#sdk-for-ios-explore-s-7heresdk14RouteDeviationV014lastLocationOnB0AA09NavigableE0VSgvp" class="token"><code>lastLocationOnRoute</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The last known location on the route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastLocationOnRoute: NavigableLocation?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-navigablelocation">NavigableLocation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14RouteDeviationV24lastTraveledSectionIndexs5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastTraveledSectionIndex" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routedeviation#sdk-for-ios-explore-s-7heresdk14RouteDeviationV24lastTraveledSectionIndexs5Int32Vvp" class="token"><code>lastTraveledSectionIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the index of the last traveled route section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastTraveledSectionIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14RouteDeviationV37traveledDistanceOnLastSectionInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-traveledDistanceOnLastSectionInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routedeviation#sdk-for-ios-explore-s-7heresdk14RouteDeviationV37traveledDistanceOnLastSectionInMeterss5Int32Vvp" class="token"><code>traveledDistanceOnLastSectionInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Offset in meter to the last visited position on the route section defined by the last traveled section index.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var traveledDistanceOnLastSectionInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14RouteDeviationV15currentLocationAA09NavigableE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-currentLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routedeviation#sdk-for-ios-explore-s-7heresdk14RouteDeviationV15currentLocationAA09NavigableE0Vvp" class="token"><code>currentLocation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The current location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currentLocation: NavigableLocation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-navigablelocation">NavigableLocation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14RouteDeviationV014lastLocationOnB00D20TraveledSectionIndex016traveledDistancef4LastH8InMeters07currentE0AcA09NavigableE0VSg_s5Int32VAlItcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-lastLocationOnRoute-lastTraveledSectionIndex-traveledDistanceOnLastSectionInMeters-currentLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-routedeviation#sdk-for-ios-explore-s-7heresdk14RouteDeviationV014lastLocationOnB00D20TraveledSectionIndex016traveledDistancef4LastH8InMeters07currentE0AcA09NavigableE0VSg_s5Int32VAlItcfc" class="token"><code>init(lastLocationOnRoute:</code><wbr></wbr><code>lastTraveledSectionIndex:</code><wbr></wbr><code>traveledDistanceOnLastSectionInMeters:</code><wbr></wbr><code>currentLocation:</code><wbr></wbr><code>)</code></a> 

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
  public init(lastLocationOnRoute: NavigableLocation? = nil, lastTraveledSectionIndex: Int32 = 0, traveledDistanceOnLastSectionInMeters: Int32 = 0, currentLocation: NavigableLocation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-navigablelocation">NavigableLocation</a>

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

