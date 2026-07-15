---
title: "AutomotiveCameraBehavior Class Reference"
slug: "sdk-for-ios-navigate-classes-automotivecamerabehavior"
---

# AutomotiveCameraBehavior

<div class="declaration">

<div class="language">

``` highlight
public class AutomotiveCameraBehavior : CameraBehavior
```

``` highlight
extension AutomotiveCameraBehavior: NativeBase
```

``` highlight
extension AutomotiveCameraBehavior: Hashable
```

</div>

</div>

Provides a high-level camera controller for automotive navigation that manages both tracking and area camera behaviors. This class acts as a facade, delegating camera operations to either a <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">`TrackingCameraBehavior`</a> for following the vehicle during navigation or an <a href="sdk-for-ios-navigate-classes-areacamerabehavior">`AreaCameraBehavior`</a> for showing overview areas such as points of interest or route previews.

The controller supports three states: tracking mode (following the vehicle), area mode (showing geographic regions), or inactive (no automatic camera control). The inactive state allows external control of the camera, such as when responding to user touch events or when UI logic temporarily disables automatic camera behavior.

Camera configuration, including animation durations, zoom policies, and maneuver handling settings, can be provided through a JSON configuration string or file. The configuration is validated and parsed during construction.

Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  Creates a new instance of this class with default camera behaviors and configuration. This constructor automatically creates and configures the underlying <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">`TrackingCameraBehavior`</a> and <a href="sdk-for-ios-navigate-classes-areacamerabehavior">`AreaCameraBehavior`</a> instances with default settings.

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

      init(configJson: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class configured from a JSON string. The JSON configuration is validated during construction and applied to the underlying <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">`TrackingCameraBehavior`</a> and <a href="sdk-for-ios-navigate-classes-areacamerabehavior">`AreaCameraBehavior`</a> instances.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> <a href="sdk-for-ios-navigate-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> when the JSON is malformed or contains invalid values.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( configJson : String ) throws
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
  <td><code> </code><em><code>configJson</code></em><code> </code></td>
  <td><div>
  <p>A JSON string containing automotive camera configuration settings.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></span>` `<span id="//apple_ref/swift/Property/normalizedPrincipalPoint" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp" class="token"><code>normalizedPrincipalPoint</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var normalizedPrincipalPoint: Anchor2D { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC26isManeuverDetectionEnabledSbvp"></span>` `<span id="//apple_ref/swift/Property/isManeuverDetectionEnabled" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC26isManeuverDetectionEnabledSbvp" class="token"><code>isManeuverDetectionEnabled</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables or disables automatic camera adjustments during upcoming maneuvers. When enabled, the tracking camera automatically adjusts zoom and framing to provide better visibility of upcoming turns and maneuvers during navigation. The specific adjustments and their timing are defined in the camera configuration.

  If tracking is currently active when this property is changed, the setting takes effect immediately. Otherwise, it will apply the next time tracking is activated. The initial state is determined by the camera configuration provided during construction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isManeuverDetectionEnabled: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp"></span>` `<span id="//apple_ref/swift/Property/viewRectangle" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp" class="token"><code>viewRectangle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. This property is forwarded to both the tracking and area cameras, ensuring consistent viewport constraints across all camera modes. If not set, it uses the viewport bounds of the underlying map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var viewRectangle: Rectangle2D? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp"></span>` `<span id="//apple_ref/swift/Property/activeCameraType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp" class="token"><code>activeCameraType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The active camera type. Defines which camera behavior is currently active: <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4noneyA2EmF">`AutomotiveCameraBehavior.ActiveCameraType.none`</a> (free navigation), <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO8trackingyA2EmF">`AutomotiveCameraBehavior.ActiveCameraType.tracking`</a>, or <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4areayA2EmF">`AutomotiveCameraBehavior.ActiveCameraType.area`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var activeCameraType: AutomotiveCameraBehavior.ActiveCameraType { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC15orientationModeAC011OrientationF0Ovp"></span>` `<span id="//apple_ref/swift/Property/orientationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC15orientationModeAC011OrientationF0Ovp" class="token"><code>orientationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The current orientation mode of the camera. Defines the camera’s viewing angle and orientation for tracking mode. In <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-orientationmode#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO6mode2dyA2EmF">`AutomotiveCameraBehavior.OrientationMode.mode2d`</a>, the camera looks straight down and rotates with the vehicle heading. In <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-orientationmode#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO6mode3dyA2EmF">`AutomotiveCameraBehavior.OrientationMode.mode3d`</a>, the camera is tilted for a perspective view. In <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-orientationmode#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO11modeNorthUpyA2EmF">`AutomotiveCameraBehavior.OrientationMode.modeNorthUp`</a>, the camera maintains north-up orientation regardless of vehicle heading.

  Changes to this property take effect immediately on the tracking camera and are preserved when switching between tracking and area modes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var orientationMode: AutomotiveCameraBehavior.OrientationMode { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO"></span>` `<span id="//apple_ref/swift/Enum/OrientationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO" class="token"><code>OrientationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the visual presentation modes for the camera orientation.

  <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-orientationmode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum OrientationMode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO"></span>` `<span id="//apple_ref/swift/Enum/ActiveCameraType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO" class="token"><code>ActiveCameraType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the type of camera currently handling camera updates.

  <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ActiveCameraType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      setAreaCameraBehaviorVisiblePoints(points: includeCurrentPosition: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the Area camera to frame the specified points. The camera calculates the optimal zoom level and center position to display all provided coordinates within the viewport. Use this for showing a single point of interest or multiple points such as safety cameras.

  This function does not change <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">`AutomotiveCameraBehavior.activeCameraType`</a>. To display the configured area view, set <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">`AutomotiveCameraBehavior.activeCameraType`</a> to <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4areayA2EmF">`AutomotiveCameraBehavior.ActiveCameraType.area`</a>.

  Calling this function overrides any previously set geographic bounding box configured via

      AutomotiveCameraBehavior.setAreaCameraBehaviorGeobox(...)

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setAreaCameraBehaviorVisiblePoints ( points : [ GeoCoordinates ], includeCurrentPosition : Bool )
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
  <td><code> </code><em><code>points</code></em><code> </code></td>
  <td><div>
  <p>The list of geographic coordinates to display.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>includeCurrentPosition</code></em><code> </code></td>
  <td><div>
  <p>When true, the current vehicle position is included in the visible area calculation, ensuring the vehicle remains visible alongside the provided points.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setAreaCameraBehaviorGeobox(geobox: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the Area camera to frame the specified geographic bounding box. The camera automatically calculates the appropriate zoom level and center position to ensure the entire area is visible within the viewport.

  This function does not change <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">`AutomotiveCameraBehavior.activeCameraType`</a>. To display the configured area view, set <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">`AutomotiveCameraBehavior.activeCameraType`</a> to <a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4areayA2EmF">`AutomotiveCameraBehavior.ActiveCameraType.area`</a>.

  Calling this function overrides any previously set visible points configured via

      AutomotiveCameraBehavior.setAreaCameraBehaviorVisiblePoints(...)

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setAreaCameraBehaviorGeobox ( geobox : GeoBox )
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
  <td><code> </code><em><code>geobox</code></em><code> </code></td>
  <td><div>
  <p>The geographic bounding box to display.</p>
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

