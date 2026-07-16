---
title: "ImageStyle Structure Reference"
slug: "sdk-for-ios-explore-classes-mapmarkercluster-imagestyle"
---

# ImageStyle

<div class="declaration">

<div class="language">

``` highlight
public struct ImageStyle
```

</div>

</div>

This class specifies the visual appearance of a cluster marker.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV5imageAA0bE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-image" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle#sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV5imageAA0bE0Cvp" class="token"><code>image</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map image for the cluster marker.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let image: MapImage
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapimage">MapImage</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV6anchorAA8Anchor2DVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-anchor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle#sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV6anchorAA8Anchor2DVvp" class="token"><code>anchor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The anchor point for the marker image which specifies the position offset relative to the cluster’s position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let anchor: Anchor2D
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV5image6anchorAeA0bE0C_AA8Anchor2DVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-image-anchor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle#sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV5image6anchorAeA0bE0C_AA8Anchor2DVtcfc" class="token"><code>init(image:</code><wbr></wbr><code>anchor:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a cluster marker image style using a map image with anchor.

  The anchor is a way of specifying position offset relative to image’s dimensions on the screen. For example, (0, 0) places the top-left corner of the image at the cluster’s position. (1, 1) would place the bottom-right corner of the image at the cluster’s position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(image: MapImage, anchor: Anchor2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapimage">MapImage</a>
  - <a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a>

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
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>The map image for the cluster marker.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>anchor</code></em><code> </code></td>
  <td><div>
  <p>The anchor point for the marker image which specifies the position offset relative to the cluster’s position.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV5imageAeA0bE0C_tcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-image" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle#sdk-for-ios-explore-s-7heresdk16MapMarkerClusterC10ImageStyleV5imageAeA0bE0C_tcfc" class="token"><code>init(image:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a marker cluster image representation with default anchor.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(image: MapImage)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapimage">MapImage</a>

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
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>The map image for the cluster marker.</p>
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

