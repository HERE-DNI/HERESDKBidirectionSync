---
title: "MapCameraKeyframeTrack Class Reference"
slug: "sdk-for-ios-explore-classes-mapcamerakeyframetrack"
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

  ` `<span id="/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22MapCameraKeyframeTrackC17interpolationModeAA0d13InterpolationG0Ovp"></span>` `<span id="//apple_ref/swift/Property/interpolationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC17interpolationModeAA0d13InterpolationG0Ovp" class="token"><code>interpolationMode</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22MapCameraKeyframeTrackC22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create a MapCameraKeyframeTrack.

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack-instantiationerrorcode" class="slightly-smaller">See more</a>

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

  </div>

  </div>

  </div>

- <div>

      getScalarKeyframes()

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
  public func getScalarKeyframes () -> [ ScalarKeyframe ]?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.

  </div>

  </div>

  </div>

- <div>

      getPoint2DKeyframes()

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
  public func getPoint2DKeyframes () -> [ Point2DKeyframe ]?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.

  </div>

  </div>

  </div>

- <div>

      getAnchor2DKeyframes()

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
  public func getAnchor2DKeyframes () -> [ Anchor2DKeyframe ]?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.

  </div>

  </div>

  </div>

- <div>

      getGeoCoordinatesKeyframes()

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
  public func getGeoCoordinatesKeyframes () -> [ GeoCoordinatesKeyframe ]?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.

  </div>

  </div>

  </div>

- <div>

      getGeoOrientationKeyframes()

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
  public func getGeoOrientationKeyframes () -> [ GeoOrientationKeyframe ]?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.

  </div>

  </div>

  </div>

- <div>

      lookAtDistance(keyframes: easing: interpolationMode: )

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

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Use `MapCameraKeyframeTrack.lookAtDistance(MapMeasure.Kind, [ScalarKeyframe], Easing, KeyframeInterpolationMode﹚` instead.") public static func lookAtDistance ( keyframes : [ ScalarKeyframe ], easing : Easing , interpolationMode : KeyframeInterpolationMode ) throws -> MapCameraKeyframeTrack
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

      lookAtDistance(ofKind: keyframes: easing: interpolationMode: )

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

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAtDistance ( ofKind distanceKind : MapMeasure . Kind , keyframes : [ ScalarKeyframe ], easing : Easing , interpolationMode : KeyframeInterpolationMode ) throws -> MapCameraKeyframeTrack
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

      lookAtTarget(keyframes: easing: interpolationMode: )

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

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAtTarget ( keyframes : [ GeoCoordinatesKeyframe ], easing : Easing , interpolationMode : KeyframeInterpolationMode ) throws -> MapCameraKeyframeTrack
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

      lookAtOrientation(keyframes: easing: interpolationMode: )

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

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAtOrientation ( keyframes : [ GeoOrientationKeyframe ], easing : Easing , interpolationMode : KeyframeInterpolationMode ) throws -> MapCameraKeyframeTrack
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

      principalPoint(keyframes: easing: interpolationMode: )

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

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func principalPoint ( keyframes : [ Point2DKeyframe ], easing : Easing , interpolationMode : KeyframeInterpolationMode ) throws -> MapCameraKeyframeTrack
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

      normalizedPrincipalPoint(keyframes: easing: interpolationMode: )

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

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func normalizedPrincipalPoint ( keyframes : [ Anchor2DKeyframe ], easing : Easing , interpolationMode : KeyframeInterpolationMode ) throws -> MapCameraKeyframeTrack
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

      fieldOfView(keyframes: easing: interpolationMode: )

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

  <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">`MapCameraKeyframeTrack.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fieldOfView ( keyframes : [ ScalarKeyframe ], easing : Easing , interpolationMode : KeyframeInterpolationMode ) throws -> MapCameraKeyframeTrack
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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

