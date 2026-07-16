---
title: "MapViewBase Protocol Reference"
slug: "sdk-for-ios-navigate-protocols-mapviewbase"
---

# MapViewBase

<div class="declaration">

<div class="language">

``` highlight
public protocol MapViewBase : AnyObject
```

</div>

</div>

Represents the available public API from <a href="sdk-for-ios-navigate-classes-mapview">`MapView`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04PickB7Handlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-PickMapHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04PickB7Handlera" class="token"><code>PickMapHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Callback for a pick request. In case of an error the result is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  typealias PickMapHandler = (_ mapPickResult: MapPickResult?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mappickresult">MapPickResult</a>

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
  <td><code> </code><em><code>mapPickResult</code></em><code> </code></td>
  <td><div>
  <p>The operation result.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP7isValidSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isValid" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP7isValidSbvp" class="token"><code>isValid</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates whether this instance is valid.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var isValid: Bool { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP6cameraAA0B6CameraCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-camera" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP6cameraAA0B6CameraCvp" class="token"><code>camera</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The camera to control the view for the map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var camera: MapCamera { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcamera">MapCamera</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP8gesturesAA8GesturesCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-gestures" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP8gesturesAA8GesturesCvp" class="token"><code>gestures</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The gestures control object for setting up the capture of gestures.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var gestures: Gestures { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-gestures">Gestures</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-mapScene" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp" class="token"><code>mapScene</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map scene associated with this map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var mapScene: MapScene { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscene">MapScene</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP10mapContextAA0bF0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-mapContext" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP10mapContextAA0bF0Cvp" class="token"><code>mapContext</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map context associated with this map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var mapContext: MapContext { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcontext">MapContext</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-hereMap" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp" class="token"><code>hereMap</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Here Map associated with this map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var hereMap: HereMap { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-heremap">HereMap</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP12viewportSizeAA6Size2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-viewportSize" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP12viewportSizeAA6Size2DVvp" class="token"><code>viewportSize</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The size of this map view in physical pixels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var viewportSize: Size2D { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-size2d">Size2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP9frameRates5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-frameRate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP9frameRates5Int32Vvp" class="token"><code>frameRate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum render frame rate in frames per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var frameRate: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP10pixelScaleSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-pixelScale" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP10pixelScaleSdvp" class="token"><code>pixelScale</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The pixel scale factor used by this <a href="sdk-for-ios-navigate-classes-mapview">`MapView`</a>.

  Pixel scale is 0.0 if the map view is not initialized.

  In cases where the <a href="sdk-for-ios-navigate-classes-mapview">`MapView`</a> moves in between screens (e.g. from main screen to a CarPlay screen), / the most up-to-date pixel scale value can be obtained after a render target gets attached to the view. / To get notified when a render target gets attached to the <a href="sdk-for-ios-navigate-classes-mapview">`MapView`</a>, see <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">`MapViewLifecycleDelegate`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var pixelScale: Double { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP13watermarkSizeAA6Size2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-watermarkSize" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP13watermarkSizeAA6Size2DVvp" class="token"><code>watermarkSize</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the size of the watermark in physical pixels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  var watermarkSize: Size2D { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-size2d">Size2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP20viewToGeoCoordinates0eH0AA0gH0VSgAA7Point2DV_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-viewToGeoCoordinates-viewCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP20viewToGeoCoordinates0eH0AA0gH0VSgAA7Point2DV_tF" class="token"><code>viewToGeoCoordinates(viewCoordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Converts view coordinates (in pixels) to geographical coordinates.

  An optional altitude component of the resulting geographical coordinate is not set.

  If the view coordinates specify a point above a horizon, then the result is geographical coordinates of the point on a horizon below the specified view coordinates.

  The fog effect is ignored for the calculation, meaning that for the view point within the area covered by the fog, the result is geographical coordinates that would be displayed at the specified point if the fog effect was not applied.

  If the render surface is not attached, it will return `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func viewToGeoCoordinates(viewCoordinates: Point2D) -> GeoCoordinates?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>
  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

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
  <p>Point inside the view to convert.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The geographical coordinates under specified view point or `nil` if there is no render surface attached.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP05geoToC11Coordinates0eG0AA7Point2DVSgAA03GeoG0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-geoToViewCoordinates-geoCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP05geoToC11Coordinates0eG0AA7Point2DVSgAA03GeoG0V_tF" class="token"><code>geoToViewCoordinates(geoCoordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Converts geographical coordinates to view coordinates (in pixels).

  If specified, altitude of the input coordinates is interpreted as altitude above sea level. If not specified, the input coordinates are interpreted as being on ground elevation. The above distinction is only relevant when 3D terrain feature is enabled.

  The resulting view coordinates might be outside of current viewport, i.e. result might contain values less than zero or greater than view’s dimensions.

  If the render surface is not attached, it will return `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func geoToViewCoordinates(geoCoordinates: GeoCoordinates) -> Point2D?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>

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
  <td><code> </code><em><code>geoCoordinates</code></em><code> </code></td>
  <td><div>
  <p>Geographical coordinates to convert.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The view coordinates of the specified geographical point or `nil` if there is no render surface attached.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setWatermarkLocation-anchor-offset" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF" class="token"><code>setWatermarkLocation(anchor:</code><wbr></wbr><code>offset:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the position of the HERE logo watermark within the map view.

  By default, the watermark is aligned to the bottom-right corner of the view: Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2). It is recommended to change the default position only if necessary to avoid overlapping UI elements. The watermark should always be fully visible within the view. The anchor point on the watermark is its center (width/2, height/2), around which it will be placed in the map view. For map views smaller than 250 dip in both width and height, the watermark will not be shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func setWatermarkLocation(anchor: Anchor2D, offset: Point2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-anchor2d">Anchor2D</a>
  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>

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
  <td><code> </code><em><code>anchor</code></em><code> </code></td>
  <td><div>
  <p>Anchor point in normalized view coordinates [0, 1]. Map view’s origin at (0, 0) indicates a top-left corner of the map view. Out of boundary anchor point values will be clamped to the [0, 1] range.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>offset</code></em><code> </code></td>
  <td><div>
  <p>A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that allows shifting the watermark from the anchor point position in one or the other direction. For the quadrant of values expressing visible part of the map view negative offset shifts the watermark to the direction of the origin, positive - away from it. For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to the bottom. If specified offset will result in watermark being completely or partially out-of-view the offset will be adjusted internally so that watermark is fully visible. Offset is not being scaled when the map view size changes.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP20addLifecycleDelegateyyAA0bcfG0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-addLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP20addLifecycleDelegateyyAA0bcfG0_pF" class="token"><code>addLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">`MapViewLifecycleDelegate`</a> to this map view. Adding the same object multiple times has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func addLifecycleDelegate(_ lifecycleListener: MapViewLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>

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
  <td><code> </code><em><code>lifecycleListener</code></em><code> </code></td>
  <td><div>
  <p>An object to be notified of lifecycle events.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP23removeLifecycleDelegateyyAA0bcfG0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP23removeLifecycleDelegateyyAA0bcfG0_pF" class="token"><code>removeLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">`MapViewLifecycleDelegate`</a> from this map view. Trying to remove an object that was not added or was removed before has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func removeLifecycleDelegate(_ lifecycleListener: MapViewLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>

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
  <td><code> </code><em><code>lifecycleListener</code></em><code> </code></td>
  <td><div>
  <p>An object to stop being notified of lifecycle events.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bJ6ResultCSgctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-pick-filter-inside-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bJ6ResultCSgctF" class="token"><code>pick(filter:</code><wbr></wbr><code>inside:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns all map content located inside the specified pick area. Content to be picked is specified by a pick content filter. The pick area is defined by a rectangle in map view coordinates in pixels, relative to the map view’s origin at (0, 0) which indicates the top-left corner of the map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func pick(filter: MapScene.MapPickFilter?, inside viewArea: Rectangle2D, completion: @escaping MapViewBase.PickMapHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscene">MapScene</a>
  - <a href="sdk-for-ios-navigate-structs-rectangle2d">Rectangle2D</a>
  - <a href="sdk-for-ios-navigate-protocols-mapviewbase#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04PickB7Handlera">PickMapHandler</a>

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
  <td><code> </code><em><code>filter</code></em><code> </code></td>
  <td><div>
  <p>Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewArea</code></em><code> </code></td>
  <td><div>
  <p>The rectangular pixel area of the view inside which map content will be picked. View area is relative to the map view’s origin at (0, 0) at the top-left corner of the map view.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback to call with the result. This will be called on a main thread when pick operation completes.</p>
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

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

