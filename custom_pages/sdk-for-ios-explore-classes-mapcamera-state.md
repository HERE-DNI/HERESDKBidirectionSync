---
title: "State Structure Reference"
slug: "sdk-for-ios-explore-classes-mapcamera-state"
---

# State

<div class="declaration">

<div class="language">

``` highlight
public struct State
```

</div>

</div>

Encapsulates state of the camera.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV17targetCoordinatesAA03GeoF0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-targetCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV17targetCoordinatesAA03GeoF0Vvp" class="token"><code>targetCoordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s ‘LookAt’ target position in geodetic space.

  Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var targetCoordinates: GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV19orientationAtTargetAA14GeoOrientationVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-orientationAtTarget" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV19orientationAtTargetAA14GeoOrientationVvp" class="token"><code>orientationAtTarget</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera’s orientation at target point.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var orientationAtTarget: GeoOrientation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geoorientation">GeoOrientation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-distanceToTargetInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp" class="token"><code>distanceToTargetInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance from the camera to the target point in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToTargetInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV9zoomLevelSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-zoomLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV9zoomLevelSdvp" class="token"><code>zoomLevel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zoom level corresponding to the current distance to target.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoomLevel: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV17targetCoordinates19orientationAtTarget010distanceToI8InMeters9zoomLevelAeA03GeoF0V_AA0P11OrientationVS2dtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-targetCoordinates-orientationAtTarget-distanceToTargetInMeters-zoomLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV17targetCoordinates19orientationAtTarget010distanceToI8InMeters9zoomLevelAeA03GeoF0V_AA0P11OrientationVS2dtcfc" class="token"><code>init(targetCoordinates:</code><wbr></wbr><code>orientationAtTarget:</code><wbr></wbr><code>distanceToTargetInMeters:</code><wbr></wbr><code>zoomLevel:</code><wbr></wbr><code>)</code></a> 

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

    - targetCoordinates: Camera’s ‘LookAt’ target position in geodetic space.

    Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    - orientationAtTarget: Camera’s orientation at target point.
    - distanceToTargetInMeters: Distance from the camera to the target point in meters.
    - zoomLevel: Zoom level corresponding to the current distance to target.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(targetCoordinates: GeoCoordinates, orientationAtTarget: GeoOrientation, distanceToTargetInMeters: Double, zoomLevel: Double)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-geoorientation">GeoOrientation</a>

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

