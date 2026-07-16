---
title: "MapCameraKeyframeTrack Class Reference"
slug: "sdk-for-ios-navigate-classes-mapcamerakeyframetrack"
---

# MapCameraKeyframeTrack

<div class="declaration">

<div class="language">

``` highlight
public class MapCameraKeyframeTrack
```

``` highlight
extension MapCameraKeyframeTrack: NativeBase
```

``` highlight
extension MapCameraKeyframeTrack: Hashable
```

</div>

</div>

Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode. Can only hold keyframes of a single type.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-InstantiationError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora" class="token"><code>InstantiationError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create `MapCameraKeyframeTrack`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack-instantiationerrorcode">InstantiationErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC17interpolationModeAA0d13InterpolationG0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC17interpolationModeAA0d13InterpolationG0Ovp" class="token"><code>interpolationMode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Interpolation mode affects the shape of the spline going through all keyframes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var interpolationMode: KeyframeInterpolationMode { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC22InstantiationErrorCodeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-InstantiationErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create a MapCameraKeyframeTrack.

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapCameraKeyframeTrack.InstantiationErrorCode : Error
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18getScalarKeyframesSayAA0gD0VGSgyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getScalarKeyframes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18getScalarKeyframesSayAA0gD0VGSgyF" class="token"><code>getScalarKeyframes()</code></a> 

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
  public func getScalarKeyframes() -> [ScalarKeyframe]?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a>

  </div>

  <div>

  #### Return Value

  a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC19getPoint2DKeyframesSayAA0G9DKeyframeVGSgyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getPoint2DKeyframes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC19getPoint2DKeyframesSayAA0G9DKeyframeVGSgyF" class="token"><code>getPoint2DKeyframes()</code></a> 

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
  public func getPoint2DKeyframes() -> [Point2DKeyframe]?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point2dkeyframe">Point2DKeyframe</a>

  </div>

  <div>

  #### Return Value

  a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC20getAnchor2DKeyframesSayAA0G9DKeyframeVGSgyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getAnchor2DKeyframes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC20getAnchor2DKeyframesSayAA0G9DKeyframeVGSgyF" class="token"><code>getAnchor2DKeyframes()</code></a> 

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
  public func getAnchor2DKeyframes() -> [Anchor2DKeyframe]?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-anchor2dkeyframe">Anchor2DKeyframe</a>

  </div>

  <div>

  #### Return Value

  a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC26getGeoCoordinatesKeyframesSayAA0ghD0VGSgyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getGeoCoordinatesKeyframes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC26getGeoCoordinatesKeyframesSayAA0ghD0VGSgyF" class="token"><code>getGeoCoordinatesKeyframes()</code></a> 

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
  public func getGeoCoordinatesKeyframes() -> [GeoCoordinatesKeyframe]?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>

  </div>

  <div>

  #### Return Value

  a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC26getGeoOrientationKeyframesSayAA0ghD0VGSgyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getGeoOrientationKeyframes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC26getGeoOrientationKeyframesSayAA0ghD0VGSgyF" class="token"><code>getGeoOrientationKeyframes()</code></a> 

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
  public func getGeoOrientationKeyframes() -> [GeoOrientationKeyframe]?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geoorientationkeyframe">GeoOrientationKeyframe</a>

  </div>

  <div>

  #### Return Value

  a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC14lookAtDistance9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-lookAtDistance-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC14lookAtDistance9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ" class="token"><code>lookAtDistance(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at in meters. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Use `MapCameraKeyframeTrack.lookAtDistance(MapMeasure.Kind, [ScalarKeyframe], Easing, KeyframeInterpolationMode﹚` instead.")
  public static func lookAtDistance(keyframes: [ScalarKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapCameraKeyframeTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A keyframe track over the distance from the map camera to its target.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC14lookAtDistance6ofKind9keyframes6easing17interpolationModeAcA0B7MeasureV0J0O_SayAA06ScalarD0VGAA6EasingCAA0d13InterpolationN0OtKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-lookAtDistance-ofKind-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC14lookAtDistance6ofKind9keyframes6easing17interpolationModeAcA0B7MeasureV0J0O_SayAA06ScalarD0VGAA6EasingCAA0d13InterpolationN0OtKFZ" class="token"><code>lookAtDistance(ofKind:</code><wbr></wbr><code>keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map camera look-at distance keyframe track. It enables animations of the distance from the map camera to the target point that the camera looks at. The measure kind of that distance can be specified. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAtDistance(ofKind distanceKind: MapMeasure.Kind, keyframes: [ScalarKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapCameraKeyframeTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasure">MapMeasure</a>
  - <a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>distanceKind</code></em><code> </code></td>
  <td><div>
  <p>The kind of measure of distance between camera and target point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A keyframe track over the distance from the map camera to its target.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC12lookAtTarget9keyframes6easing17interpolationModeACSayAA014GeoCoordinatesD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-lookAtTarget-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC12lookAtTarget9keyframes6easing17interpolationModeACSayAA014GeoCoordinatesD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ" class="token"><code>lookAtTarget(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map camera look-at target keyframe track. It enables animations over the geographical coordinates of the target point that the map camera is looking at. Altitude components of coordinates are ignored.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAtTarget(keyframes: [GeoCoordinatesKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapCameraKeyframeTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A keyframe track over the map camera target coordinates.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC17lookAtOrientation9keyframes6easing17interpolationModeACSayAA03GeohD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-lookAtOrientation-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC17lookAtOrientation9keyframes6easing17interpolationModeACSayAA03GeohD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ" class="token"><code>lookAtOrientation(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map camera look-at orientation keyframe track. It enables animations over the orientation of the map camera target (bearing and tilt).

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAtOrientation(keyframes: [GeoOrientationKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapCameraKeyframeTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geoorientationkeyframe">GeoOrientationKeyframe</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A keyframe track over the map camera target orientation.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC14principalPoint9keyframes6easing17interpolationModeACSayAA15Point2DKeyframeVG_AA6EasingCAA0d13InterpolationK0OtKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-principalPoint-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC14principalPoint9keyframes6easing17interpolationModeACSayAA15Point2DKeyframeVG_AA6EasingCAA0d13InterpolationK0OtKFZ" class="token"><code>principalPoint(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map camera principal point keyframe track. It enables animations on the pixel point where the map camera’s target is placed in view coordinates. (0,0) is top left of the viewport, (viewport width, viewport height) is bottom right.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func principalPoint(keyframes: [Point2DKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapCameraKeyframeTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point2dkeyframe">Point2DKeyframe</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the camera property is changed. Point values must be in screen (pixel) coordinates with origin (0,0) in the top left of the viewport. Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A keyframe track over the principal point.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC24normalizedPrincipalPoint9keyframes6easing17interpolationModeACSayAA16Anchor2DKeyframeVG_AA6EasingCAA0d13InterpolationL0OtKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-normalizedPrincipalPoint-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC24normalizedPrincipalPoint9keyframes6easing17interpolationModeACSayAA16Anchor2DKeyframeVG_AA6EasingCAA0d13InterpolationL0OtKFZ" class="token"><code>normalizedPrincipalPoint(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map camera principal point keyframe track. It enables animations on the point where the map camera’s target is placed in normalized view coordinates. (0,0) is top left of the viewport, (1, 1) is bottom right.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func normalizedPrincipalPoint(keyframes: [Anchor2DKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapCameraKeyframeTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-anchor2dkeyframe">Anchor2DKeyframe</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the camera property is changed. Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport. Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A keyframe track over the principal point.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC11fieldOfView9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-fieldOfView-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC11fieldOfView9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ" class="token"><code>fieldOfView(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map camera field-of-view keyframe track. It enables animations over the angle of the field of view captured by the map camera in degrees. Values will be clamped to a range from 1 to 150.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack#sdk-for-ios-navigate-s-7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fieldOfView(keyframes: [ScalarKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapCameraKeyframeTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A keyframe track over the map camera field-of-view.

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

