---
title: "MapMarker3D Class Reference"
slug: "sdk-for-ios-explore-classes-mapmarker3d"
---

# MapMarker3D

<div class="declaration">

<div class="language">

``` highlight
public class MapMarker3D
```

``` highlight
extension MapMarker3D: NativeBase
```

``` highlight
extension MapMarker3D: Hashable
```

</div>

</div>

Represents a 3D shape drawn on the map at specified geodetic coordinates.

It can have a solid color or be textured, depending on the data from <a href="sdk-for-ios-explore-classes-mapmarker3dmodel">`MapMarker3DModel`</a>.

By default, a 3D marker is drawn on top of all map content, including 3D map elements like extruded buildings or 3D landmarks. This can be changed by enabling depth check using <a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp">`MapMarker3D.isDepthCheckEnabled`</a>.

The display of a 3D marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects a 3D marker that is visually large and covers a sizeable part of the viewport.

# Sizing and scaling

Two aspects determine how big the `MapMarker3D` will be on the screen and how will it behave when the map is zoomed in and out.

The first, and most impactful is <a href="sdk-for-ios-explore-structs-rendersize-unit">`RenderSize.Unit`</a>, which specifies how the vertex coordinates of the 3D model are interpreted. Most importantly, it specifies whether the 3D model is placed in world or screen coordinate space.

<a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">`RenderSize.Unit.meters`</a> will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out.

<a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.

<a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">`RenderSize.Unit.densityIndependentPixels`</a> is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.

The second aspect that determines size of `MapMarker3D` is scale. It can be specified at construction time and can be changed later at any time using <a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC5scaleSdvp">`MapMarker3D.scale`</a>.

# Modifying at runtime

A 3D marker can be moved around a map by updating its coordinates using <a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp">`MapMarker3D.coordinates`</a>.

Altitude component of the coordinates, if set, controls 3D marker’s elevation above ground. If not set, the 3D marker is placed at ground level.

Its orientation is specified by bearing, pitch and roll and can be changed by using <a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC7bearingSdvp">`MapMarker3D.bearing`</a>, <a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC5pitchSdvp">`MapMarker3D.pitch`</a> and <a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC4rollSdvp">`MapMarker3D.roll`</a>.

# Flat marker

A flat marker is a special case of a 3D marker, where the 3D shape being drawn is a simple textured rectangle. In essence it’s an image drawn “on the ground”. Such 3D marker can be conveniently created using

    MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit)

constructor. Of course, once created, it can be rotated to face any direction.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(at: model: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of a 3D marker.

  The origin of the 3D model’s local coordinate system is placed at the specified geographical coordinates.

  Altitude component of the coordinates, if set, controls 3D marker’s elevation above ground. If not set, the 3D marker is placed at ground level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( at : GeoCoordinates , model : MapMarker3DModel )
  ```

  </pre>

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
  <td><code> </code><em><code>at</code></em><code> </code></td>
  <td><div>
  <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model’s local coordinate system.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>model</code></em><code> </code></td>
  <td><div>
  <p>The 3D model used to draw 3D marker.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(at: image: scale: unit: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a flat marker from provided map image.

  Such map marker is a flat 3D marker of rectangular shape textured with given image. Aspect ratio of the flat marker is determined by aspect ratio of the image.

  Only bitmap images are supported, using a <a href="sdk-for-ios-explore-classes-mapimage">`MapImage`</a> created from SVG data will result in distorted rendering of the flat marker.

  Altitude component of the coordinates, if set, controls 3D marker’s elevation above ground. If not set, the 3D marker is placed at ground level.

  Size of the rendered flat marker can be specified in either world or screen coordinate space.

  For <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a>, the flat marker will cover

      MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale

  \* image’s width pixels horizontally and
      MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale

  \* image’s height pixels vertically. The size of the flat marker remains constant on the screen.
  </p>

  For <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">`RenderSize.Unit.densityIndependentPixels`</a> the flat marker will cover

      MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale

  \* image’s width density independent pixels horizontally and
      MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale

  \* image’s height density independent pixels vertically. The size of the flat marker remains constant on the screen.
  </p>

  For <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">`RenderSize.Unit.meters`</a> the flat marker will cover

      MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale

  \* image’s width meters horizontally and
      MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale

  \* image’s height meters vertically. Unlike with pixels or density independent pixels the size of the flat marker will grow and shrink together with regular map content like streets or buildings.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( at : GeoCoordinates , image : MapImage , scale : Double , unit : RenderSize . Unit )
  ```

  </pre>

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
  <td><code> </code><em><code>at</code></em><code> </code></td>
  <td><div>
  <p>The geographical coordinates where the flat marker is placed corresponding to center of the provided map image.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>The MapImage containing the texture data of the flat marker. SVG images are not supported.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scale</code></em><code> </code></td>
  <td><div>
  <p>Scale factor applied to the dimensions of the image.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>unit</code></em><code> </code></td>
  <td><div>
  <p>Determines whether the size of the flat marker is represented in world or in screen space.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(at: model: scale: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of a 3D marker with scale factor.

  One unit of the 3D marker model will cover

      MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double).scale

  pixels. The size of the 3D marker remains constant on the screen.
  </p>

  The origin of the 3D model’s local coordinate system is placed at the specified geographical coordinates.

  Altitude component of the coordinates, if set, controls 3D marker’s elevation above ground. If not set, the 3D marker is placed at ground level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( at : GeoCoordinates , model : MapMarker3DModel , scale : Double )
  ```

  </pre>

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
  <td><code> </code><em><code>at</code></em><code> </code></td>
  <td><div>
  <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model’s local coordinate system.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>model</code></em><code> </code></td>
  <td><div>
  <p>The 3D model used to render the 3D marker.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scale</code></em><code> </code></td>
  <td><div>
  <p>Scale factor to apply to the 3D model.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(at: model: scale: unit: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new 3D marker at given world coordinates, using the supplied 3D model.

  The unit specifies how the 3D geometry of the model is interpreted (meters for world space, pixels or density independent pixels for screen space), while scale determines its relative size.

  For <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> one unit of the 3D marker model will cover

      MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double, RenderSize.Unit).scale

  pixels. The size of the 3D marker remains constant on the screen.
  </p>

  For <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">`RenderSize.Unit.densityIndependentPixels`</a> one unit of the 3D marker model will cover

      MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double, RenderSize.Unit).scale

  density independent pixels. The size of the 3D marker remains constant on the screen.
  </p>

  For <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">`RenderSize.Unit.meters`</a> one unit of the 3D marker model will cover

      MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double, RenderSize.Unit).scale

  meters in the real world. Unlike with pixels or density-independent pixels the size of the 3D marker will grow and shrink together with regular map content like streets or buildings.
  </p>

  The origin of the 3D model’s local coordinate system is placed at the specified geographical coordinates.

  Altitude component of the coordinates, if set, controls 3D marker’s elevation above ground. If not set, the 3D marker is placed at ground level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( at : GeoCoordinates , model : MapMarker3DModel , scale : Double , unit : RenderSize . Unit )
  ```

  </pre>

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
  <td><code> </code><em><code>at</code></em><code> </code></td>
  <td><div>
  <p>The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model’s local coordinate system.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>model</code></em><code> </code></td>
  <td><div>
  <p>The 3D model used to render the 3D marker.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scale</code></em><code> </code></td>
  <td><div>
  <p>Scale factor to apply to the 3D model.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>unit</code></em><code> </code></td>
  <td><div>
  <p>Determines the unit of the model vertices and whether the size of the 3D marker is expressed in world or screen space.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/coordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system. The altitude component of the coordinates, if set, controls 3D marker’s elevation above ground. If not set, the 3D marker is placed at ground level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC8metadataAA8MetadataCSgvp"></span>` `<span id="//apple_ref/swift/Property/metadata" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC8metadataAA8MetadataCSgvp" class="token"><code>metadata</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-classes-metadata">`Metadata`</a> instance attached to this 3D marker. The default value is `nil`

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var metadata: Metadata? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC7bearingSdvp"></span>` `<span id="//apple_ref/swift/Property/bearing" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC7bearingSdvp" class="token"><code>bearing</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The bearing of the 3D model in degrees, from the true North in clockwise direction. The bearing axis is perpendicular to the ground and passes through the 3D marker’s location. The Z-axis of the model is aligned with bearing axis.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var bearing: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC4rollSdvp"></span>` `<span id="//apple_ref/swift/Property/roll" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC4rollSdvp" class="token"><code>roll</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The roll angle of the 3D model in degrees. The roll axis is parallel to the ground, passes through the 3D marker’s location and is aligned initially with the true North. However, when the bearing changes, it rotates around the bearing axis with the 3D marker. Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis in the direction of the true North. The Y-axis of the model is aligned with the roll axis.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roll: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC5pitchSdvp"></span>` `<span id="//apple_ref/swift/Property/pitch" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC5pitchSdvp" class="token"><code>pitch</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The pitch of the 3D model in degrees. The pitch axis is parallel to the ground, passes through the location of the 3D marker and aligns with the longitude axis if the bearing is 0. However, this axis rotates with the 3D marker according to the bearing value. Negative values cause the top of the 3D marker to lean forward. The X-axis of the model is aligned with pitch axis.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pitch: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC5scaleSdvp"></span>` `<span id="//apple_ref/swift/Property/scale" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC5scaleSdvp" class="token"><code>scale</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Scale factor applied to the 3D model before rendering.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var scale: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp"></span>` `<span id="//apple_ref/swift/Property/isDepthCheckEnabled" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp" class="token"><code>isDepthCheckEnabled</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines whether the depth of the 3D marker’s vertices is considered during rendering. If set to `false`, the 3D marker will always appear in front of any other map objects. If set to `true` the 3D marker might be occluded by other map objects like extruded buildings.

  By default depth check is set to `false`.

  Use the altitude of the <a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp">`MapMarker3D.coordinates`</a> to position the 3D marker sufficiently high above the surface. Setting depth check to `true` will fix visual glitches where components of the marker 3D model unexpectedly shine through.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDepthCheckEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC24isRenderInternalsEnabledSbvp"></span>` `<span id="//apple_ref/swift/Property/isRenderInternalsEnabled" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC24isRenderInternalsEnabledSbvp" class="token"><code>isRenderInternalsEnabled</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons. Default value is `false`. Can be used with translucent 3D marker.

  Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two passes: first pass with front-face, second pass with back-face culling enabled. With this flag enabled for 3D marker with depth check disabled rendering is performed in a single pass with back-face culling disabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRenderInternalsEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC7opacitySdvp"></span>` `<span id="//apple_ref/swift/Property/opacity" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC7opacitySdvp" class="token"><code>opacity</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The opacity factor adjusting the opacity of a 3D marker. Provided value is clamped to the \[0.0, 1.0\] range. The factor is applied to the alpha channel of the resulting texture of the marker. Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the specified fill color specified in <a href="sdk-for-ios-explore-classes-mapmarker3dmodel">`MapMarker3DModel`</a>.

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

  ` `<span id="/s:7heresdk11MapMarker3DC16visibilityRangesSayAA0B12MeasureRangeVGvp"></span>` `<span id="//apple_ref/swift/Property/visibilityRanges" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarker3d#/s:7heresdk11MapMarker3DC16visibilityRangesSayAA0B12MeasureRangeVGvp" class="token"><code>visibilityRanges</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of visibility ranges. The 3D marker is visible only inside these map measure ranges. A range is half open - \<a href="sdk-for-ios-explore-classes-s">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

  When empty (the default), the 3D marker is visible without map measure restrictions. Only [MapMeasureRange</a> of <a href="sdk-for-ios-explore-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> type are supported. <a href="sdk-for-ios-explore-classes-s">MapMeasureRange</a> of other unsupported types will be ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var visibilityRanges: [MapMeasureRange] { get set }
  ```

  </div>

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

