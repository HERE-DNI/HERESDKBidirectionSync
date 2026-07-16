---
title: "PickMapItemsResult Class Reference"
slug: "sdk-for-ios-navigate-classes-pickmapitemsresult"
---

# PickMapItemsResult

<div class="declaration">

<div class="language">

``` highlight
public class PickMapItemsResult
```

``` highlight
extension PickMapItemsResult: NativeBase
```

``` highlight
extension PickMapItemsResult: Hashable
```

</div>

</div>

Carries results from the picking of map items on the map scene.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC16clusteredMarkersSayAA0C13MarkerClusterC8GroupingVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-clusteredMarkers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pickmapitemsresult#sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC16clusteredMarkersSayAA0C13MarkerClusterC8GroupingVGvp" class="token"><code>clusteredMarkers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of marker groups (represented by a single cluster marker) or individual markers belonging to a cluster at the location of picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var clusteredMarkers: [MapMarkerCluster.Grouping] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarkercluster">MapMarkerCluster</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC7markersSayAA0C6MarkerCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-markers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pickmapitemsresult#sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC7markersSayAA0C6MarkerCGvp" class="token"><code>markers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of markers at the location of picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var markers: [MapMarker] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC9markers3dSayAA0C8Marker3DCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-markers3d" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pickmapitemsresult#sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC9markers3dSayAA0C8Marker3DCGvp" class="token"><code>markers3d</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of 3d markers at the location of picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var markers3d: [MapMarker3D] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker3d">MapMarker3D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC9polylinesSayAA0C8PolylineCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-polylines" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pickmapitemsresult#sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC9polylinesSayAA0C8PolylineCGvp" class="token"><code>polylines</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of polylines at the location of picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var polylines: [MapPolyline] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mappolyline">MapPolyline</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC8polygonsSayAA0C7PolygonCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-polygons" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pickmapitemsresult#sdk-for-ios-navigate-s-7heresdk18PickMapItemsResultC8polygonsSayAA0C7PolygonCGvp" class="token"><code>polygons</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of polygons at the location of picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var polygons: [MapPolygon] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mappolygon">MapPolygon</a>

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

