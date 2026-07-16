---
title: "MapMarker Class Reference"
slug: "sdk-for-ios-navigate-classes-mapmarker"
---

# MapMarker

<div class="declaration">

<div class="language">

``` highlight
public class MapMarker
```

``` highlight
extension MapMarker: NativeBase
```

``` highlight
extension MapMarker: Hashable
```

</div>

</div>

`MapMarker` is used to draw images on the map, for example to mark a specific location. By default, the marker is centered on the given geographic coordinates. Markers keep their size regardless of the current zoom level of the map view.

The image to be displayed is represented by <a href="sdk-for-ios-navigate-classes-mapimage">`MapImage`</a> object. For performance reasons, it is highly recommended to reuse a single instance of the image when creating multiple identical markers.

To display the map marker, it needs to be added to the scene using <a href="sdk-for-ios-navigate-classes-mapscene#sdk-for-ios-navigate-s-7heresdk8MapSceneC03addB6MarkeryyAA0bE0CF">`MapScene.addMapMarker(...)`</a>. To stop displaying it, remove it from the scene using <a href="sdk-for-ios-navigate-classes-mapscene#sdk-for-ios-navigate-s-7heresdk8MapSceneC06removeB6MarkeryyAA0bE0CF">`MapScene.removeMapMarker(...)`</a>.

The display of a map marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects map markers which are visually large and cover a sizeable part of the viewport.

**Note:** Due to technical limitations using the MapMarkers API to add a very large number of markers (several thousands, especially 10000+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation the following approach can be used: Register to map camera updates using <a href="sdk-for-ios-navigate-classes-mapcamera#sdk-for-ios-navigate-s-7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF">`MapCamera.addDelegate(...)`</a>. Query the bounding box of the camera viewport using <a href="sdk-for-ios-navigate-classes-mapcamera#sdk-for-ios-navigate-s-7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">`MapCamera.boundingBox`</a> (it may be extended) and then use the method

    GeoBox.contains(GeoCoordinates)

in combination with <a href="sdk-for-ios-navigate-classes-mapcamera-state#sdk-for-ios-navigate-s-7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">`MapCamera.State.distanceToTargetInMeters`</a> to determine which MapMarkers are actually visible to the user in the current camera viewport and thus need to be added to the map.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC2at5imageAcA14GeoCoordinatesV_AA0B5ImageCtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-at-image" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC2at5imageAcA14GeoCoordinatesV_AA0B5ImageCtcfc" class="token"><code>init(at:</code><wbr></wbr><code>image:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of a marker at given coordinates, represented by specified image.

  The altitude component of the coordinates is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(at coordinates: GeoCoordinates, image: MapImage)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
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
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>The marker’s geographical coordinates.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC2at5image4textAcA14GeoCoordinatesV_AA0B5ImageCSStcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-at-image-text" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC2at5image4textAcA14GeoCoordinatesV_AA0B5ImageCSStcfc" class="token"><code>init(at:</code><wbr></wbr><code>image:</code><wbr></wbr><code>text:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a `MapMarker` instance at given coordinates with specified image and text and a default text style.

  The altitude component of the coordinates is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(at coordinates: GeoCoordinates, image: MapImage, text: String)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
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
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>The marker’s geographical coordinates.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>The image to draw on the map.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>text</code></em><code> </code></td>
  <td><div>
  <p>The text to draw on the map.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC2at5image6anchorAcA14GeoCoordinatesV_AA0B5ImageCAA8Anchor2DVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-at-image-anchor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC2at5image6anchorAcA14GeoCoordinatesV_AA0B5ImageCAA8Anchor2DVtcfc" class="token"><code>init(at:</code><wbr></wbr><code>image:</code><wbr></wbr><code>anchor:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of a marker at given coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the marker’s coordinates.

  The anchor is a way of specifying position offset relative to image’s dimensions on the screen. For example, (0, 0) places the top-left corner of the image at the marker’s coordinates. (1, 1) would place the bottom-right corner of the image at the marker’s coordinates. (0.5, 0.5) which is the default value would center the image at the marker’s coordinates. Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the marker’s coordinates at the distance in pixels that is equal to the height of the image.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(at coordinates: GeoCoordinates, image: MapImage, anchor: Anchor2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
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
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>The marker’s geographical coordinates.</p>
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
  <p>The anchor point for the marker image which specifies the position offset relative to the marker’s coordinates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC11coordinatesAA14GeoCoordinatesVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The point on the map where the map marker is drawn. The altitude component of the coordinates is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC8metadataAA8MetadataCSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-metadata" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC8metadataAA8MetadataCSgvp" class="token"><code>metadata</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The Metadata instance attached to this marker, see <a href="sdk-for-ios-navigate-classes-metadata">`Metadata`</a>. This will be `nil` if nothing has been attached before.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var metadata: Metadata? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-metadata">Metadata</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC16isOverlapAllowedSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isOverlapAllowed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC16isOverlapAllowedSbvp" class="token"><code>isOverlapAllowed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines whether or not the marker can overlap other markers. If `false`, it will disappear the moment it overlaps another marker that has a higher visibility priority. A marker that allows overlap will always be drawn. Among markers that don’t allow overlap, the one with the highest draw order has priority. Marker that is hidden due to overlapping with other markers is not pickable.

  Defaults to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isOverlapAllowed: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC14isTextOptionalSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isTextOptional" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC14isTextOptionalSbvp" class="token"><code>isTextOptional</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines if the marker can be displayed with icon and without text. Controls whenever `MapMarker` can be shown as icon only when <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC16isOverlapAllowedSbvp">`MapMarker.isOverlapAllowed`</a> is `false`, has no effect otherwise. If `false` then the `MapMarker` will not appear when icon or text are blocked by other labels. If `true`, icon will appear even if the text part is blocked by other labels.

  Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTextOptional: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC9drawOrders5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-drawOrder" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC9drawOrders5Int32Vvp" class="token"><code>drawOrder</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The draw order of this marker relative to other markers. Markers with higher draw order value are drawn on top of markers with lower draw order. In case multiple markers have the same draw order value then the order in which they were added to the scene matters. Last added marker is drawn on top.

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

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC5imageAA0B5ImageCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-image" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC5imageAA0B5ImageCvp" class="token"><code>image</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Image representing the marker on the screen.

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

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC6anchorAA8Anchor2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-anchor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC6anchorAA8Anchor2DVvp" class="token"><code>anchor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The anchor point for the marker image which specifies the position offset relative to the marker’s coordinates. For example, (0, 0) places the top-left corner of the image at the marker’s coordinates. (1, 1) would place the bottom-right corner of the image at the marker’s coordinates. (0.5, 0.5) which is the default value would center the image at the marker’s coordinates. Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the marker’s coordinates at the distance in pixels that is equal to the height of the image.

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

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC7opacitySdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-opacity" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC7opacitySdvp" class="token"><code>opacity</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Opacity, the factor applied to the alpha channel of the marker image. Provided value is clamped in range \[0.0, 1.0\]. Default value is 1.0, which means marker is displayed with the default opacity of the image.

  Markers with opacity value set to 0.0 are still on map and are considered for picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var opacity: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC12fadeDurationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-fadeDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC12fadeDurationSdvp" class="token"><code>fadeDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene. Provided value is clamped in range \[0.0, 10.0\] seconds. Default value is 0 seconds which means the effect is disabled and marker is added/removed immediately without any animation.

  Fade-in effect is also applied when marker leaves and then re-enters screen area.

  Change to this property is made asynchronously and is not guaranteed to take effect on the next rendered frame. In particular, changing fade duration and removing the marker immediately after may result in the new value being ignored for this removal.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fadeDuration: TimeInterval { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC4textSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-text" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC4textSSvp" class="token"><code>text</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text to be drawn on the map along with the image of the `MapMarker`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var text: String { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC9textStyleAC04TextE0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-textStyle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC9textStyleAC04TextE0Cvp" class="token"><code>textStyle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle">`TextStyle`</a> applied to the text of the `MapMarker`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textStyle: MapMarker.TextStyle { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle">TextStyle</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC16visibilityRangesSayAA0B12MeasureRangeVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-visibilityRanges" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC16visibilityRangesSayAA0B12MeasureRangeVGvp" class="token"><code>visibilityRanges</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of visibility ranges. The map marker is visible only inside these map measure ranges. A range is half open - \<a href="sdk-for-ios-navigate-structs-mapmeasurerange">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

  When empty (the default), the map marker is visible without map measure restrictions. Only [`MapMeasureRange`</a>(s) of <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#sdk-for-ios-navigate-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> type are supported. <a href="sdk-for-ios-navigate-structs-mapmeasurerange">`MapMeasureRange`</a>(s) of other unsupported types will be ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var visibilityRanges: [MapMeasureRange] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasurerange">MapMeasureRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC9TextStyleC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-TextStyle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC9TextStyleC" class="token"><code>TextStyle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Styling options for the text of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>.

  <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TextStyle
  ```

  ``` highlight
  extension MapMarker.TextStyle: NativeBase
  ```

  ``` highlight
  extension MapMarker.TextStyle: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_pSgtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-startAnimation-_-animationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_pSgtF" class="token"><code>startAnimation(_:</code><wbr></wbr><code>animationDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts animation of this map marker according to provided <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">`MapMarkerAnimation`</a>.

  The <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">`MapMarkerAnimation`</a> may be shared between multiple instances of `MapMarker`.

  Starting animation on one map marker does not influence any ongoing animations on other map markers. Any ongoing animation of this marker instance will get cancelled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func startAnimation(_ animation: MapMarkerAnimation, animationDelegate: AnimationDelegate?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">MapMarkerAnimation</a>
  - <a href="sdk-for-ios-navigate-protocols-animationdelegate">AnimationDelegate</a>

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
  <td><code> </code><em><code>animation</code></em><code> </code></td>
  <td><div>
  <p>The animation to start, may be used for multiple different map markers.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>animationDelegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to receive notifications about animation start, completion or cancellation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9MapMarkerC15cancelAnimationyyAA0bcE0CF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-cancelAnimation-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC15cancelAnimationyyAA0bcE0CF" class="token"><code>cancelAnimation(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Cancels single ongoing animation.

  Does nothing if animation was not started for this map marker.

  Does not cancel other animations if the same <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">`MapMarkerAnimation`</a> object was applied to multiple `MapMarker`s.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func cancelAnimation(_ animation: MapMarkerAnimation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">MapMarkerAnimation</a>

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
  <td><code> </code><em><code>animation</code></em><code> </code></td>
  <td><div>
  <p>The animation to cancel.</p>
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

