---
title: "IndoorRoutePlace Structure Reference"
slug: "sdk-for-ios-navigate-structs-indoorrouteplace"
---

# IndoorRoutePlace

<div class="declaration">

<div class="language">

``` highlight
public struct IndoorRoutePlace : Hashable
```

</div>

</div>

Represents a place within an indoor route.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV4typeAA0cD4TypeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-indoorrouteplace#sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV4typeAA0cD4TypeOvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of the route place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: RoutePlaceType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-routeplacetype">RoutePlaceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV11coordinatesAA14GeoCoordinatesVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-indoorrouteplace#sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic coordinates of the place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV11levelZIndexs5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-levelZIndex" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-indoorrouteplace#sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV11levelZIndexs5Int32Vvp" class="token"><code>levelZIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The vertical level index of this indoor location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var levelZIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV7venueIdSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-venueId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-indoorrouteplace#sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV7venueIdSSvp" class="token"><code>venueId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The venue identifier of this indoor location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var venueId: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV7levelIdSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-levelId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-indoorrouteplace#sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV7levelIdSSvp" class="token"><code>levelId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The level identifier of this indoor location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var levelId: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV4type11coordinates11levelZIndex7venueId0gJ0AcA0cD4TypeO_AA14GeoCoordinatesVs5Int32VS2Stcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-type-coordinates-levelZIndex-venueId-levelId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-indoorrouteplace#sdk-for-ios-navigate-s-7heresdk16IndoorRoutePlaceV4type11coordinates11levelZIndex7venueId0gJ0AcA0cD4TypeO_AA14GeoCoordinatesVs5Int32VS2Stcfc" class="token"><code>init(type:</code><wbr></wbr><code>coordinates:</code><wbr></wbr><code>levelZIndex:</code><wbr></wbr><code>venueId:</code><wbr></wbr><code>levelId:</code><wbr></wbr><code>)</code></a> 

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
  public init(type: RoutePlaceType, coordinates: GeoCoordinates, levelZIndex: Int32, venueId: String, levelId: String)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-routeplacetype">RoutePlaceType</a>
  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

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

