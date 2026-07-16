---
title: "TrackingCameraBehavior Class Reference"
slug: "sdk-for-ios-navigate-classes-trackingcamerabehavior"
---

# TrackingCameraBehavior

<div class="declaration">

<div class="language">

``` highlight
public class TrackingCameraBehavior : CameraBehavior
```

``` highlight
extension TrackingCameraBehavior: NativeBase
```

``` highlight
extension TrackingCameraBehavior: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a>

</div>

Use this class to follow a moving target. The camera smoothly tracks the target’s position while adjusting heading, tilt, and zoom as needed. When tracking starts or resumes, the camera first animates a re-centering transition to align with the target.

Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are subject to change without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorCACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-normalizedPrincipalPoint" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp" class="token"><code>normalizedPrincipalPoint</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-navigate-structs-anchor2d">Anchor2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC25recenterAnimationDurationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-recenterAnimationDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC25recenterAnimationDurationSdvp" class="token"><code>recenterAnimationDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The duration of recenter animation in milliseconds. Time to recenter the camera reaching current car position. Defaults to 500 milliseconds, or half a second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var recenterAnimationDuration: TimeInterval { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-viewRectangle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp" class="token"><code>viewRectangle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to `nil`. If not set, it uses the viewport bounds of the underlying map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var viewRectangle: Rectangle2D? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-rectangle2d">Rectangle2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC31principalPointAnimationDurationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-principalPointAnimationDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC31principalPointAnimationDurationSdvp" class="token"><code>principalPointAnimationDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The duration of principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var principalPointAnimationDuration: TimeInterval { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC13tiltInDegreesSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tiltInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC13tiltInDegreesSdvp" class="token"><code>tiltInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The value of camera tilt in degrees. Camera tilt angle relative to the ground plane, in degrees. Defaults to 50.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tiltInDegrees: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC16bearingInDegreesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-bearingInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC16bearingInDegreesSdSgvp" class="token"><code>bearingInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The camera bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in “north up” mode. Defaults to `nil`, which means the camera derives the bearing from the <a href="sdk-for-ios-navigate-structs-location">`Location`</a>, so that it points to the direction of travel. If this property is `nil` and the device does not provide bearing, the last known value is used or zero otherwise.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var bearingInDegrees: Double? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34maxRotationSpeedInDegreesPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maxRotationSpeedInDegreesPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34maxRotationSpeedInDegreesPerSecondSdvp" class="token"><code>maxRotationSpeedInDegreesPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maximum rotation speed. Maximum bearing rotation speed in degrees per second, limiting how fast the camera turns. Defaults to 20 degrees per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxRotationSpeedInDegreesPerSecond: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC26zoomSpeedInLevelsPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-zoomSpeedInLevelsPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC26zoomSpeedInLevelsPerSecondSdvp" class="token"><code>zoomSpeedInLevelsPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The zoom level transition speed. Speed factor controlling how quickly the camera transitions between zoom levels Defaults to 0.5 zoom levels per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoomSpeedInLevelsPerSecond: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC10zoomPolicyAC04ZoomF0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-zoomPolicy" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC10zoomPolicyAC04ZoomF0Cvp" class="token"><code>zoomPolicy</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The strategy of computing the zoom level. Defines the strategy used to compute the zoom level based on scene heuristics. Defaults to a fixed zoom policy at zoom level 16.5.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoomPolicy: TrackingCameraBehavior.ZoomPolicy { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-zoompolicy">ZoomPolicy</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC26isManeuverDetectionEnabledSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isManeuverDetectionEnabled" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC26isManeuverDetectionEnabledSbvp" class="token"><code>isManeuverDetectionEnabled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Whether maneuver detection is enabled. When `true`, the camera detects adjacent maneuvers and reacts according to the <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration">`TrackingCameraBehavior.ManeuverModeConfiguration`</a> set via <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC28setManeuverModeConfiguration08maneuvergH0yAC0fgH0VSg_tF">`TrackingCameraBehavior.setManeuverModeConfiguration(...)`</a>. A valid <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration">`TrackingCameraBehavior.ManeuverModeConfiguration`</a> must be set for the camera to react. Defaults to `false`.

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

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC10ZoomPolicyC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-ZoomPolicy" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC10ZoomPolicyC" class="token"><code>ZoomPolicy</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines zoom behavior in different policy settings.

  Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are subject to change without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-zoompolicy" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class ZoomPolicy
  ```

  ``` highlight
  extension TrackingCameraBehavior.ZoomPolicy: NativeBase
  ```

  ``` highlight
  extension TrackingCameraBehavior.ZoomPolicy: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC14SpeedThresholdV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-SpeedThreshold" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC14SpeedThresholdV" class="token"><code>SpeedThreshold</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines a zoom level triggered when the vehicle reaches a specific speed.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedthreshold" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpeedThreshold
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-FunctionalRoadClassZoomPolicyOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV" class="token"><code>FunctionalRoadClassZoomPolicyOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configuration for mapping functional road classes to zoom levels. For correct default initialization, use <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ">`TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions(...)`</a>.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct FunctionalRoadClassZoomPolicyOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-SpeedBasedZoomPolicyOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV" class="token"><code>SpeedBasedZoomPolicyOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configuration for computing zoom levels from speed thresholds defined per road classification. For correct default initialization, use <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">`TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)`</a>.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedbasedzoompolicyoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SpeedBasedZoomPolicyOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-ManeuverZoomRange" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV" class="token"><code>ManeuverZoomRange</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the bounds within which the zoom level is constrained when approaching a maneuver. Used as part of <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions">`TrackingCameraBehavior.ManeuverRuleOptions`</a>.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverzoomrange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverZoomRange
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-ManeuverRuleOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV" class="token"><code>ManeuverRuleOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines a set of configurations specific to a <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverrule">`TrackingCameraBehavior.ManeuverRule`</a>.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverRuleOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-ManeuverRule" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV" class="token"><code>ManeuverRule</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines a single rule that determines how <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">`TrackingCameraBehavior`</a> reacts to nearby maneuvers when the current position matches this rule.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverrule" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverRule
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-ManeuverModeConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV" class="token"><code>ManeuverModeConfiguration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configuration that defines how <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">`TrackingCameraBehavior`</a> reacts to nearby maneuvers.

  On each frame, and based on the current position, the availability of its functional road class, and the availability of maneuver data for at least one adjacent maneuver, the camera checks for a match against the <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV13maneuverRulesSayAC0E4RuleVGvp">`TrackingCameraBehavior.ManeuverModeConfiguration.maneuverRules`</a> in the order they are listed. If a match is found, subsequent rules are not checked. If no match is found, if inputs are unavailable, or if the matched rule has `nil` options, the camera does not react.

  For correct default initialization, use <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ">`TrackingCameraBehavior.defaultManeuverModeConfiguration(...)`</a>.

  <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ManeuverModeConfiguration
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC33flagFixedDurationForNextAnimationyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-flagFixedDurationForNextAnimation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC33flagFixedDurationForNextAnimationyyF" class="token"><code>flagFixedDurationForNextAnimation()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables fixed-duration animation mode for the next property change. When called, the next setter call (e.g., tilt_in_degrees or bearing_in_degrees) will animate using a fast fixed-duration animation instead of the default speed-based animation. The flag is automatically reset after the next setter is called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func flagFixedDurationForNextAnimation()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC28setManeuverModeConfiguration08maneuvergH0yAC0fgH0VSg_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setManeuverModeConfiguration-maneuverModeConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC28setManeuverModeConfiguration08maneuvergH0yAC0fgH0VSg_tF" class="token"><code>setManeuverModeConfiguration(maneuverModeConfiguration:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the configuration for camera behavior near maneuvers. Defines how the camera reacts to nearby maneuvers when <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC26isManeuverDetectionEnabledSbvp">`TrackingCameraBehavior.isManeuverDetectionEnabled`</a> is `true`. When set to `nil`, the camera does not react to maneuvers. The configuration must contain at least one rule to be valid. Defaults to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setManeuverModeConfiguration(maneuverModeConfiguration: TrackingCameraBehavior.ManeuverModeConfiguration?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration">ManeuverModeConfiguration</a>

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
  <td><code> </code><em><code>maneuverModeConfiguration</code></em><code> </code></td>
  <td><div>
  <p>The maneuver mode configuration. Invalid configurations are rejected.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC28getManeuverModeConfigurationAC0fgH0VSgyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getManeuverModeConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC28getManeuverModeConfigurationAC0fgH0VSgyF" class="token"><code>getManeuverModeConfiguration()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the current maneuver mode configuration, or `nil` if not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getManeuverModeConfiguration() -> TrackingCameraBehavior.ManeuverModeConfiguration?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration">ManeuverModeConfiguration</a>

  </div>

  <div>

  #### Return Value

  The current maneuver mode configuration.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-defaultFunctionalRoadClassZoomPolicyOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ" class="token"><code>defaultFunctionalRoadClassZoomPolicyOptions()</code></a> 

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
  public static func defaultFunctionalRoadClassZoomPolicyOptions() -> TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">FunctionalRoadClassZoomPolicyOptions</a>

  </div>

  <div>

  #### Return Value

  The default <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">`TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions`</a>.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-defaultSpeedBasedZoomPolicyOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ" class="token"><code>defaultSpeedBasedZoomPolicyOptions()</code></a> 

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
  public static func defaultSpeedBasedZoomPolicyOptions() -> TrackingCameraBehavior.SpeedBasedZoomPolicyOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">SpeedBasedZoomPolicyOptions</a>

  </div>

  <div>

  #### Return Value

  The default <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">`TrackingCameraBehavior.SpeedBasedZoomPolicyOptions`</a>.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-defaultManeuverModeConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ" class="token"><code>defaultManeuverModeConfiguration()</code></a> 

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
  public static func defaultManeuverModeConfiguration() -> TrackingCameraBehavior.ManeuverModeConfiguration
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration">ManeuverModeConfiguration</a>

  </div>

  <div>

  #### Return Value

  The default <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuvermodeconfiguration">`TrackingCameraBehavior.ManeuverModeConfiguration`</a>.

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

