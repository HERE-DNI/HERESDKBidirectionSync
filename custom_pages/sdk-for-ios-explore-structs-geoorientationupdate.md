---
title: "GeoOrientationUpdate Structure Reference"
slug: "sdk-for-ios-explore-structs-geoorientationupdate"
---

# GeoOrientationUpdate

<div class="declaration">

<div class="language">

``` highlight
public struct GeoOrientationUpdate : Hashable
```

</div>

</div>

Describes geodetic orientation update with bearing and tilt. Updating an orientation value can be skipped by setting `nil` in an appriopriate field. For example, if one wants bearing not to be updated set it to `nil`.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateV7bearingSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-bearing" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geoorientationupdate#sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateV7bearingSdSgvp" class="token"><code>bearing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bearing in degrees. 0 is north up, positive is clockwise. A `nil` value means that bearing is not updated and the current value is kept.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let bearing: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateV4tiltSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tilt" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geoorientationupdate#sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateV4tiltSdSgvp" class="token"><code>tilt</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tilt in degrees. 0 is perpendicular to earth surface, a positive value turns the camera’s nose up and changes the camera’s location to ensure that the camera target is not changed. A `nil` value means that tilt is not updated and the current value is kept.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let tilt: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateV7bearing4tiltACSdSg_AFtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-bearing-tilt" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geoorientationupdate#sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateV7bearing4tiltACSdSg_AFtcfc" class="token"><code>init(bearing:</code><wbr></wbr><code>tilt:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(bearing: Double?, tilt: Double?)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>bearing</code></em><code> </code></td>
  <td><div>
  <p>Bearing in degrees. When the passed value is <code>nil</code> bearing is not updated and the current value is kept. NaN value is converted to <code>nil</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>tilt</code></em><code> </code></td>
  <td><div>
  <p>Tilt in degrees. When the passed value is <code>nil</code> tilt is not updated and the current value is kept. NaN value is converted to <code>nil</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateVyAcA0bC0Vcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geoorientationupdate#sdk-for-ios-explore-s-7heresdk20GeoOrientationUpdateVyAcA0bC0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new GeoOrientationUpdate instance from a GeoOrientation instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ orientation: GeoOrientation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geoorientation">GeoOrientation</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>A GeoOrientation instance used as a source for a GeoOrientationUpdate instance’s values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

