---
title: "ManeuverRuleOptions Structure Reference"
slug: "sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions"
---

# ManeuverRuleOptions

<div class="declaration">

<div class="language">

``` highlight
public struct ManeuverRuleOptions
```

</div>

</div>

Defines a set of configurations specific to a <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverrule">`TrackingCameraBehavior.ManeuverRule`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRangeAC0e4ZoomI0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-zoomRange" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRangeAC0e4ZoomI0Vvp" class="token"><code>zoomRange</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The zoom range for this rule. Defines the minimum and maximum zoom levels. Defaults to a default-constructed <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverzoomrange">`TrackingCameraBehavior.ManeuverZoomRange`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoomRange: TrackingCameraBehavior.ManeuverZoomRange
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverzoomrange">ManeuverZoomRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV08earlyPreE27ActivationThresholdInMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-earlyPreManeuverActivationThresholdInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV08earlyPreE27ActivationThresholdInMetersSdvp" class="token"><code>earlyPreManeuverActivationThresholdInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance in meters for early activation. If the current position enters this threshold of the upcoming maneuver while still within <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV04postE27ActivationThresholdInMetersSdvp">`TrackingCameraBehavior.ManeuverRuleOptions.postManeuverActivationThresholdInMeters`</a> of the previous maneuver, the camera behaves as though it were already in the upcoming maneuver’s pre-activation zone. Must be non-negative. Defaults to 0.0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var earlyPreManeuverActivationThresholdInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV03preE27ActivationThresholdInMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-preManeuverActivationThresholdInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV03preE27ActivationThresholdInMetersSdvp" class="token"><code>preManeuverActivationThresholdInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance in meters before the next maneuver point within which this rule becomes active. Must be non-negative. Defaults to 0.0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var preManeuverActivationThresholdInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV04postE27ActivationThresholdInMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-postManeuverActivationThresholdInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV04postE27ActivationThresholdInMetersSdvp" class="token"><code>postManeuverActivationThresholdInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance in meters after the previous maneuver point within which this rule remains active. Must be non-negative. Defaults to 0.0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var postManeuverActivationThresholdInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRange08earlyPreE27ActivationThresholdInMeters03preelmnO004postelmnO0AeC0e4ZoomI0V_S3dtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-zoomRange-earlyPreManeuverActivationThresholdInMeters-preManeuverActivationThresholdInMeters-postManeuverActivationThresholdInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverruleoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRange08earlyPreE27ActivationThresholdInMeters03preelmnO004postelmnO0AeC0e4ZoomI0V_S3dtcfc" class="token"><code>init(zoomRange:</code><wbr></wbr><code>earlyPreManeuverActivationThresholdInMeters:</code><wbr></wbr><code>preManeuverActivationThresholdInMeters:</code><wbr></wbr><code>postManeuverActivationThresholdInMeters:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(zoomRange: TrackingCameraBehavior.ManeuverZoomRange = TrackingCameraBehavior.ManeuverZoomRange(), earlyPreManeuverActivationThresholdInMeters: Double = 0.0, preManeuverActivationThresholdInMeters: Double = 0.0, postManeuverActivationThresholdInMeters: Double = 0.0)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-maneuverzoomrange">ManeuverZoomRange</a>

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

