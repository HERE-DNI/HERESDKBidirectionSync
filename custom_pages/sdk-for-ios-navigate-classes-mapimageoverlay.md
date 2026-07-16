---
title: "MapImageOverlay Class Reference"
slug: "sdk-for-ios-navigate-classes-mapimageoverlay"
---

# MapImageOverlay

<div class="declaration">

<div class="language">

``` highlight
public class MapImageOverlay
```

``` highlight
extension MapImageOverlay: NativeBase
```

``` highlight
extension MapImageOverlay: Hashable
```

</div>

</div>

`MapImageOverlay` is used to draw images over the map, at a view coordinate inside the map viewport.

The image to be displayed is represented by a <a href="sdk-for-ios-navigate-classes-mapimage">`MapImage`</a> object. By default, the overlay is centered on the given view coordinate.

The resulting viewport area covered by the overlay is computed out of the overlay’s view coordinate, the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.

To display the map overlay, it needs to be added to the scene using <a href="sdk-for-ios-navigate-classes-mapscene#sdk-for-ios-navigate-s-7heresdk8MapSceneC03addB12ImageOverlayyyAA0beF0CF">`MapScene.addMapImageOverlay(...)`</a>. To stop displaying it, remove it from the scene using <a href="sdk-for-ios-navigate-classes-mapscene#sdk-for-ios-navigate-s-7heresdk8MapSceneC06removeB12ImageOverlayyyAA0beF0CF">`MapScene.removeMapImageOverlay(...)`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC2at5imageAcA7Point2DV_AA0bC0Ctcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-at-image" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapimageoverlay#sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC2at5imageAcA7Point2DV_AA0bC0Ctcfc" class="token"><code>init(at:</code><wbr></wbr><code>image:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of an overlay at given view coordinates, represented by specified image.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(at viewCoordinates: Point2D, image: MapImage)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>
  - <a href="sdk-for-ios-navigate-classes-mapimage">MapImage</a>

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
  <td><code> </code><em><code>viewCoordinates</code></em><code> </code></td>
  <td><div>
  <p>The overlay’s view coordinates in pixels.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>The image to draw on the map.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC2at5image6anchorAcA7Point2DV_AA0bC0CAA8Anchor2DVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-at-image-anchor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapimageoverlay#sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC2at5image6anchorAcA7Point2DV_AA0bC0CAA8Anchor2DVtcfc" class="token"><code>init(at:</code><wbr></wbr><code>image:</code><wbr></wbr><code>anchor:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of an overlay at given view coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the overlay’s view coordinates.

  The anchor is a way of specifying position offset relative to image’s dimensions on the view. For example, (0, 0) places the top-left corner of the image at the overlay’s view coordinates. (1, 1) would place the bottom-right corner of the image at the overlay’s view coordinates. (0.5, 0.5) which is the default value would center the image at the overlay’s view coordinates.

  Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the overlay’s view coordinates at the distance in pixels that is equal to the height of the image.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(at viewCoordinates: Point2D, image: MapImage, anchor: Anchor2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>
  - <a href="sdk-for-ios-navigate-classes-mapimage">MapImage</a>
  - <a href="sdk-for-ios-navigate-structs-anchor2d">Anchor2D</a>

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
  <td><code> </code><em><code>viewCoordinates</code></em><code> </code></td>
  <td><div>
  <p>The overlay’s view coordinates in pixels.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>The image to draw on the map.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>anchor</code></em><code> </code></td>
  <td><div>
  <p>The anchor point for the overlay image which specifies the position offset relative to the overlay’s view coordinates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC15viewCoordinatesAA7Point2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-viewCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapimageoverlay#sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC15viewCoordinatesAA7Point2DVvp" class="token"><code>viewCoordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The view point in pixels on the map viewport where the map overlay is drawn.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var viewCoordinates: Point2D { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC9drawOrders5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-drawOrder" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapimageoverlay#sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC9drawOrders5Int32Vvp" class="token"><code>drawOrder</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Draw order of this `MapImageOverlay`. Overlays with higher draw order value are drawn on top of overlays with lower draw order.

  In case multiple overlays have the same draw order value then the order in which they were added to the scene matters. Last added overlay is drawn on top.

  Allowed range is \[0, 1023\]. Values outside this range will be clamped. The default value is 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var drawOrder: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC5imageAA0bC0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-image" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapimageoverlay#sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC5imageAA0bC0Cvp" class="token"><code>image</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Image overlayed on the map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var image: MapImage { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapimage">MapImage</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC6anchorAA8Anchor2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-anchor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapimageoverlay#sdk-for-ios-navigate-s-7heresdk15MapImageOverlayC6anchorAA8Anchor2DVvp" class="token"><code>anchor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The anchor point for the overlay image which specifies the position offset relative to the overlay’s view coordinates. For example, (0, 0) places the top-left corner of the image at the overlay’s view coordinates. (1, 1) would place the bottom-right corner of the image at the overlay’s view coordinates. (0.5, 0.5) which is the default value would center the image at the overlay’s view coordinates.

  Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the overlay’s view coordinates at the distance in pixels that is equal to the height of the image.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var anchor: Anchor2D { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-anchor2d">Anchor2D</a>

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

