---
title: "PickedPlace Structure Reference"
slug: "sdk-for-ios-navigate-structs-pickedplace"
---

# PickedPlace

<div class="declaration">

<div class="language">

``` highlight
public struct PickedPlace : Hashable
```

</div>

</div>

Carries the result of picking a Carto POI (point of interest) object.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11PickedPlaceV4nameSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-name" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-pickedplace#sdk-for-ios-navigate-s-7heresdk11PickedPlaceV4nameSSvp" class="token"><code>name</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The name of the POI localized in the currently selected map language.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11PickedPlaceV11coordinatesAA14GeoCoordinatesVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-pickedplace#sdk-for-ios-navigate-s-7heresdk11PickedPlaceV11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the POI.

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

   <span id="sdk-for-ios-navigate-s-7heresdk11PickedPlaceV15placeCategoryIdSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-placeCategoryId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-pickedplace#sdk-for-ios-navigate-s-7heresdk11PickedPlaceV15placeCategoryIdSSvp" class="token"><code>placeCategoryId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The place category ID of the POI. This is the same String value as <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC2idSSvp">`PlaceCategory.id`</a> that can be obtained from the <a href="sdk-for-ios-navigate-classes-searchengine">`SearchEngine`</a> and the <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a>. Note that not all editions include the <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var placeCategoryId: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11PickedPlaceV15offlineSearchIdSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-offlineSearchId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-pickedplace#sdk-for-ios-navigate-s-7heresdk11PickedPlaceV15offlineSearchIdSSvp" class="token"><code>offlineSearchId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The place ID to query an offline search to obtain additional data about this POI with the <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a>. Note that not all editions include the <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offlineSearchId: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11PickedPlaceV4name11coordinates15placeCategoryId013offlineSearchH0ACSS_AA14GeoCoordinatesVS2Stcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-name-coordinates-placeCategoryId-offlineSearchId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-pickedplace#sdk-for-ios-navigate-s-7heresdk11PickedPlaceV4name11coordinates15placeCategoryId013offlineSearchH0ACSS_AA14GeoCoordinatesVS2Stcfc" class="token"><code>init(name:</code><wbr></wbr><code>coordinates:</code><wbr></wbr><code>placeCategoryId:</code><wbr></wbr><code>offlineSearchId:</code><wbr></wbr><code>)</code></a> 

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
  public init(name: String, coordinates: GeoCoordinates, placeCategoryId: String, offlineSearchId: String = "")
  ```

  </div>

  Related types:

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

