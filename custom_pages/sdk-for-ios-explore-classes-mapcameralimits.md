---
title: "MapCameraLimits Class Reference"
slug: "sdk-for-ios-explore-classes-mapcameralimits"
---

# MapCameraLimits

<div class="declaration">

<div class="language">

``` highlight
public class MapCameraLimits
```

``` highlight
extension MapCameraLimits: NativeBase
```

``` highlight
extension MapCameraLimits: Hashable
```

</div>

</div>

Controls constraints on map camera parameters.

When constraints are set, they are enforced for current camera state and for all future changes to the camera.

When setting, limits are applied on next rendering loop.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ"></span>` `<span id="//apple_ref/swift/Variable/minTilt" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ" class="token"><code>minTilt</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Absolute minimum possible value of tilt angle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let minTilt: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC7maxTiltSdvpZ"></span>` `<span id="//apple_ref/swift/Variable/maxTilt" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC7maxTiltSdvpZ" class="token"><code>maxTilt</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Absolute maximum possible value of tilt angle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let maxTilt: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ"></span>` `<span id="//apple_ref/swift/Variable/minZoomLevel" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ" class="token"><code>minZoomLevel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Absolute minimum possible value of zoom level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let minZoomLevel: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC12maxZoomLevelSdvpZ"></span>` `<span id="//apple_ref/swift/Variable/maxZoomLevel" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12maxZoomLevelSdvpZ" class="token"><code>maxZoomLevel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Absolute maximum possible value of zoom level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let maxZoomLevel: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp"></span>` `<span id="//apple_ref/swift/Property/tiltRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp" class="token"><code>tiltRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The tilt range that can be applied to the camera. The supported values fall inside <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ">`code>`</a> range. Setting values outside the supported range will be ignored.

  By default, a <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC7minTiltSdvpZ">`code>`</a> tilt range is set during initialization.

  If the current camera tilt exceeds the new limit range, it will immediately be set to minimum or maximum, depending on which is closest.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tiltRange: AngleRange { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp"></span>` `<span id="//apple_ref/swift/Property/bearingRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp" class="token"><code>bearingRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The bearing range within which the camera can be rotated. If the current camera bearing exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.

  By default, a full circle is set during initialization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var bearingRange: AngleRange { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC9zoomRangeAA0b7MeasureF0Vvp"></span>` `<span id="//apple_ref/swift/Property/zoomRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC9zoomRangeAA0b7MeasureF0Vvp" class="token"><code>zoomRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The zoom range that can be applied to the camera. The supported values fall inside <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">`code>`</a> range. Values outside the supported zoom range are ignored.

  By default, a <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">`code>`</a> zoom range is set during initialization.

  If the current camera zoom exceeds the limit range, it will immediately be set to minimum or maximum, depending on which is closest.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoomRange: MapMeasureRange { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC10targetAreaAA6GeoBoxVSgvp"></span>` `<span id="//apple_ref/swift/Property/targetArea" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC10targetAreaAA6GeoBoxVSgvp" class="token"><code>targetArea</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographical area to which the camera target is limited. Absence of a value means that there is no limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var targetArea: GeoBox? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      setBearingRangeAtZoom(_: bearingRange: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the bearing range within which the camera can rotate at a given zoom.

  The resulting camera bearing at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no bearing range is specified for <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">`MapCameraLimits.minZoomLevel`</a>, the bearing range set through <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp">`MapCameraLimits.bearingRange`</a> is used for interpolation.

  Zoom values outside the supported zoom range are ignored. By default, the maximum bearing range for all zoom values is set during initialization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setBearingRangeAtZoom ( _ zoom : MapMeasure , bearingRange : AngleRange )
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
  <td><code> </code><em><code>zoom</code></em><code> </code></td>
  <td><div>
  <p>Zoom at which the range is set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bearingRange</code></em><code> </code></td>
  <td><div>
  <p>Bearing range.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      clearBearingRanges()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Clears bearing ranges for all zoom values and resets <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12bearingRangeAA05AngleF0Vvp">`MapCameraLimits.bearingRange`</a> to default.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func clearBearingRanges ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      setTiltRangeAtZoom(_: tiltRange: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets tilt ranges that can be set on the camera at given zoom.

  The resulting camera tilt at a zoom is an interpolated value of the ranges set for closest matching zoom values. When no tilt range is specified for <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC12minZoomLevelSdvpZ">`MapCameraLimits.minZoomLevel`</a>, the tilt range set through <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp">`MapCameraLimits.tiltRange`</a> is used for interpolation.

  Zoom or tilt values outside the supported zoom and tilt range are ignored. By default, the maximum tilt range for all zoom values is set during initialization.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setTiltRangeAtZoom ( _ zoom : MapMeasure , tiltRange : AngleRange )
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
  <td><code> </code><em><code>zoom</code></em><code> </code></td>
  <td><div>
  <p>Zoom at which the range is set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>tiltRange</code></em><code> </code></td>
  <td><div>
  <p>Tilt range.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      clearTiltRanges()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Clears tilt ranges for all zoom values and resets <a href="sdk-for-ios-explore-classes-mapcameralimits#/s:7heresdk15MapCameraLimitsC9tiltRangeAA05AngleF0Vvp">`MapCameraLimits.tiltRange`</a> to default.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func clearTiltRanges ()
  ```

  </pre>

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

