---
title: "LocationIndicator Class Reference"
slug: "sdk-for-ios-navigate-classes-locationindicator"
---

# LocationIndicator

<div class="declaration">

<div class="language">

``` highlight
public class LocationIndicator
```

``` highlight
extension LocationIndicator: NativeBase
```

``` highlight
extension LocationIndicator: Hashable
```

</div>

</div>

Graphical object to represent the location of the user on the map.

It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style. This style can be changed by <a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp">`LocationIndicator.locationIndicatorStyle`</a>

The location is made available to an instance of this class by calling

    LocationIndicator.updateLocation(Location)

or

    LocationIndicator.updateLocation(Location, MapCameraUpdate)

.
</p>

Use

    LocationIndicator.enable(...)

to add this object to the map and

    LocationIndicator.disable(...)

to remove it.
</p>

Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly disappear from the viewport due to the new perspective.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of LocationIndicator.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(for: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of LocationIndicator and adds it to provided <a href="sdk-for-ios-navigate-protocols-mapviewbase">`MapViewBase`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( for mapView : MapViewBase )
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
  <td><code> </code><em><code>mapView</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-protocols-mapviewbase"><code>MapViewBase</code></a> instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationIndicatorC20isAccuracyVisualizedSbvp"></span>` `<span id="//apple_ref/swift/Property/isAccuracyVisualized" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC20isAccuracyVisualizedSbvp" class="token"><code>isAccuracyVisualized</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo. By default, it is set to `false`. In this case the accuracy indicator halo has a fixed and zoom level independent size. When set to `true`, the radius of the halo corresponds to the value of <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">`Location.horizontalAccuracyInMeters`</a> passed to

      LocationIndicator.updateLocation(Location)

  and scales in world coordinates.
  </p>

  For values smaller than 20 meters the halo is hidden. The radius of the halo is limited to 500 meters and values higher than that or `nil` will keep the halo at that size.

  If the location indicator is set to inactive (which can be checked via <a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC8isActiveSbvp">`LocationIndicator.isActive`</a> flag), then the halo is always hidden. The value of this property remains unchanged regardless of the flag’s value. If the location indicator is set to active:

  - Built-in location indicators:
    - The halo is always shown.
    - If the accuracy visualization is set to `true`, the size of the halo scales with <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">`Location.horizontalAccuracyInMeters`</a> in world coordinates.
    - If the accuracy visualization is set to `false`, halo displays at a default size.
  - Custom location indicator:
    - If the accuracy visualization is set to `true`, halo is shown and the size of the halo scales with <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">`Location.horizontalAccuracyInMeters`</a> in world coordinates.
    - If the accuracy visualization is set to `false`, no halo is shown since it might not fit together with the custom 3d model.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isAccuracyVisualized: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp"></span>` `<span id="//apple_ref/swift/Property/locationIndicatorStyle" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp" class="token"><code>locationIndicatorStyle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The visual style of location indicator. By default, it is set to <a href="sdk-for-ios-navigate-classes-locationindicator-indicatorstyle#/s:7heresdk17LocationIndicatorC0C5StyleO10navigationyA2EmF">`LocationIndicator.IndicatorStyle.navigation`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var locationIndicatorStyle: LocationIndicator.IndicatorStyle { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationIndicatorC8isActiveSbvp"></span>` `<span id="//apple_ref/swift/Property/isActive" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC8isActiveSbvp" class="token"><code>isActive</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A Boolean value that determines whether the active on inactive version of location indicator is shown. By default, it is set to `true`.

  Set to `false` to show the inactive version of the indicator which is typically represented by a grayed out version of the indicator. This can be used in case the location of the indicator might be outdated or positioning on the device is disabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isActive: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationIndicatorC7opacitySdvp"></span>` `<span id="//apple_ref/swift/Property/opacity" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC7opacitySdvp" class="token"><code>opacity</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The factor applied to the alpha channel of both the location indicator’s texture and the accuracy indicator’s halo color. The value is clamped in range \[0.0, 1.0\]. Default value is 1.0 which means location indicator is displayed with the default alpha channel of the texture.

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

  ` `<span id="/s:7heresdk17LocationIndicatorC20materialReflectivityAA08MaterialE0VSgvp"></span>` `<span id="//apple_ref/swift/Property/materialReflectivity" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC20materialReflectivityAA08MaterialE0VSgvp" class="token"><code>materialReflectivity</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The material reflectivity properties of the location indicator. Enables per‑pixel lighting for all internal markers (navigation, pedestrian, inactive variants) and the halo when assigned. While `materialReflectivity` is non‑null the markers are shaded by scene lights using the provided ambient / diffuse factors. When set back to `nil`, lighting is disabled and markers revert to unlit (emissive) rendering. This value also applies to any custom markers set with `setMarker3dModel`. Default value is `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var materialReflectivity: MaterialReflectivity? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationIndicatorC0C5StyleO"></span>` `<span id="//apple_ref/swift/Enum/IndicatorStyle" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC0C5StyleO" class="token"><code>IndicatorStyle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The predefined styles for the location indicator which are pedestrian and navigation mode.

  <a href="sdk-for-ios-navigate-classes-locationindicator-indicatorstyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum IndicatorStyle : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationIndicatorC10MarkerTypeO"></span>` `<span id="//apple_ref/swift/Enum/MarkerType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC10MarkerTypeO" class="token"><code>MarkerType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enum to identify different types of markers of the location indicator.

  <a href="sdk-for-ios-navigate-classes-locationindicator-markertype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MarkerType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      enable(for: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables `LocationIndicator` for provided <a href="sdk-for-ios-navigate-protocols-mapviewbase">`MapViewBase`</a>. If `LocationIndicator` is already enabled (added to map view) for passed map view, this function does nothing. If `LocationIndicator` is added to different <a href="sdk-for-ios-navigate-protocols-mapviewbase">`MapViewBase`</a>, this function removes first `LocationIndicator` from previous map view before adding to new one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func enable ( for mapView : MapViewBase )
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
  <td><code> </code><em><code>mapView</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-protocols-mapviewbase"><code>MapViewBase</code></a> instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      disable()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This function removes `LocationIndicator` from map view. If `LocationIndicator` was not added to any map view yet, this function does nothing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func disable ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      updateLocation(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Updates the indicator to a new location. If accuracy visualized is set to `true` the field <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">`Location.horizontalAccuracyInMeters`</a> determines the size of the accuracy indicator halo.

  The altitude of the location is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateLocation ( _ location : Location )
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
  <td><code> </code><em><code>location</code></em><code> </code></td>
  <td><div>
  <p>The updated location of the user.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      updateLocation(_: cameraUpdate: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Updates the indicator to a new location and applies a camera update at the same time.

  Does nothing if the indicator instance is not enabled. If accuracy visualized is set to `true` the field <a href="sdk-for-ios-navigate-structs-location#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">`Location.horizontalAccuracyInMeters`</a> determines the size of the accuracy indicator halo.

  The altitude of the location is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateLocation ( _ location : Location , cameraUpdate : MapCameraUpdate )
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
  <td><code> </code><em><code>location</code></em><code> </code></td>
  <td><div>
  <p>The updated location of the user.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>cameraUpdate</code></em><code> </code></td>
  <td><div>
  <p>The update to apply to the camera.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setMarker3dModel(_: scale: type: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only MapMarker3DModel created from \*.obj files are supported. Models created from Mesh will be ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Please use the overloaded method with `RenderSize.Unit` instead.") public func setMarker3dModel ( _ model : MapMarker3DModel , scale : Double , type : LocationIndicator . MarkerType )
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
  <td><code> </code><em><code>model</code></em><code> </code></td>
  <td><div>
  <p>The MapMarker3DModel object to be displayed for the specified type. Only models created from obj files are supported. Those created from mesh will be ignored.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scale</code></em><code> </code></td>
  <td><div>
  <p>The scaling which will be applied to the marker model. As the size of the location marker should be aligned on devices with different resolutions the scale factor is applied relative to the ppi value and thus differs from the scale which is passed to <a href="sdk-for-ios-navigate-classes-mapmarker3d"><code>MapMarker3D</code></a> objects. Meter is used for the unit of the map marker 3d model coordinate system. For historical reason, the scale factor is internally devided by 6. To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>type</code></em><code> </code></td>
  <td><div>
  <p>The type of location marker for which the marker 3d model should be replaced.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setMarker3dModel(_: scale: type: renderSizeUnit: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the <a href="sdk-for-ios-navigate-classes-mapmarker3dmodel">`MapMarker3DModel`</a> asset to be displayed as location indicator for a specified type. The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only <a href="sdk-for-ios-navigate-classes-mapmarker3dmodel">`MapMarker3DModel`</a> created from `obj` files are supported. Models created from Mesh will be ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setMarker3dModel ( _ model : MapMarker3DModel , scale : Double , type : LocationIndicator . MarkerType , renderSizeUnit : RenderSize . Unit )
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
  <td><code> </code><em><code>model</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-classes-mapmarker3dmodel"><code>MapMarker3DModel</code></a> object to be displayed for the specified type. Only models created from <code>obj</code> files are supported. Those created from mesh will be ignored.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>scale</code></em><code> </code></td>
  <td><div>
  <p>A scale factor applied to the marker model.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>type</code></em><code> </code></td>
  <td><div>
  <p>The type of location marker for which the marker 3d model should be replaced.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>renderSizeUnit</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-structs-rendersize-unit"><code>RenderSize.Unit</code></a> specifying how the vertex coordinates of the 3D model are being interpreted. It specifies whether the 3D model is placed in world or screen coordinate space.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setHaloColor(_: color: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the color of the accuracy indicator halo for a given style.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setHaloColor ( _ style : LocationIndicator . IndicatorStyle , color : UIColor )
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
  <td><code> </code><em><code>style</code></em><code> </code></td>
  <td><div>
  <p>The type of IndicatorStyle for which the color should be assigned.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>The color to be applied to the halo for a specified IndicatorStyle. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getHaloColor(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle. The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getHaloColor ( _ style : LocationIndicator . IndicatorStyle ) -> UIColor
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
  <td><code> </code><em><code>style</code></em><code> </code></td>
  <td><div>
  <p>The type of IndicatorStyle for which the color should be returned.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The color of the halo for the specified IndicatorStyle. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

